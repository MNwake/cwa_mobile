from typing import Optional, Dict, List, Tuple

import requests
from requests import RequestException

from database import DataModel

from database import WebSocketManager
from database.utils import BASE_URL


class HttpManager:
    @staticmethod
    def get_request(url: str, params: Optional[Dict] = None) -> Optional[Dict]:
        try:
            response = requests.get(url, params=params)
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Failed to retrieve data. Status code: {response.status_code}")
                return None
        except Exception as e:
            print(f"An error occurred while making the request: {e}")
            return None


    def fetch_riders(self, cursor=None, **kwargs):
        url = f"http://{BASE_URL}/riders"
        params = {'cursor': cursor, **kwargs}
        return self.get_request(url, params=params)

    def fetch_rider_stats(self, cursor=None, **kwargs):
        url = f"http://{BASE_URL}/stats/riders"
        params = {'cursor': cursor, **kwargs}
        return self.get_request(url, params=params)

    def fetch_scorecards(self, **kwargs):
        url = f"http://{BASE_URL}/scorecards"
        return self.get_request(url, params=kwargs)

    def fetch_parks(self, cursor=None, **kwargs):
        url = f"http://{BASE_URL}/parks"
        params = {'cursor': cursor, **kwargs}
        return self.get_request(url, params=params)


class DataBase:


    def __init__(self):
        self.parks_callback = None
        self.scorecards_callback = None
        self.stats_callback = None
        self.riders_callback = None
        self.data = DataModel()
        self.stats = None
        self.parks = None
        self.scorecards = None
        self.base_url = BASE_URL
        self.http = HttpManager()
        self.websocket_manager = WebSocketManager(base_url=BASE_URL)


    def check_network_connection(self):
        """Check if the API server is reachable."""
        try:
            response = requests.get(f"http://{self.base_url}/ping", timeout=5)
            return response.status_code == 200
        except (ConnectionError, RequestException):
            return False

    async def fetch_all_riders(self, **kwargs):
        all_data = []
        next_cursor = None
        while True:
            response = self.http.fetch_riders(cursor=next_cursor, **kwargs)

            if not response:
                break  # Exit the loop if no riders are returned

            # Assuming response is a dict with 'data' and 'next_cursor' keys
            data = response.get('data')
            next_cursor = response.get('cursor')

            all_data.extend(data)
            if next_cursor is None:
                break  # Exit the loop if there's no next cursor

        if self.riders_callback:
            self.riders_callback(all_data)

        self.data.riders = all_data
        return all_data

    async def fetch_all_stats(self, **kwargs):
        all_data = []
        next_cursor = None

        while True:
            data, next_cursor = self.http.fetch_rider_stats(cursor=next_cursor, **kwargs)

            if not data:
                break  # Exit the loop if no riders are returned

            all_data.extend(data)
            if next_cursor is None:
                break  # Exit the loop if there's no next cursor

        if self.stats_callback:
            self.stats_callback(all_data)
        self.data.stats = all_data
        return all_data

    async def fetch_all_parks(self, **kwargs):
        """
        Fetch all parks data from the API.

        This method continuously fetches parks using pagination until all parks are retrieved.

        Args:
            **kwargs: Additional keyword arguments to be passed for filtering parks.

        """
        all_data = []
        next_cursor = None
        while True:
            data, next_cursor = self.http.fetch_parks(cursor=next_cursor, **kwargs)

            if not data:
                break  # Exit the loop if no parks are returned

            all_data.extend(data)
            if next_cursor is None:
                break  # Exit the loop if there's no next cursor
        if self.parks_callback:
            self.parks_callback(all_data)
        self.data.parks = all_data
        return all_data

    async def fetch_recent_scorecards(self, cursor=None, limit=10, **kwargs):
        all_data = []
        fetched_count = 0

        try:
            result = await self.http.fetch_scorecards(cursor=cursor, limit=limit, **kwargs)
            if result is None:
                raise ValueError("fetch_scorecards returned None")

            data, next_cursor = result

            if data:
                all_data.extend(data)
                fetched_count += len(data)

            if not data or fetched_count < limit:
                next_cursor = None

        except ValueError as e:
            print(f"Error occurred: {e}")
            next_cursor = None

        if self.scorecards_callback:
            self.scorecards_callback(all_data, next_cursor)
        self.data.scorecards = all_data
        return all_data, next_cursor
