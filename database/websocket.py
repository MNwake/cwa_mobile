import asyncio
import json

import websockets


class WebSocketManager:
    def __init__(self, base_url):
        self.base_url = base_url
        self.parks_callback = None
        self.rider_callback = None
        self.stat_callback = None
        self.scorecard_callback = None
        self.rider = None
        self.running = False
        self.parks_websocket = None
        self.stat_websocket = None
        self.rider_websocket = None
        self.scorecard_websocket = None

    async def stat_client(self):
        uri = f"ws://{self.base_url}/stats/ws/rider"
        try:
            async with websockets.connect(uri) as websocket:
                self.stat_websocket = websocket
                self.running = True
                while self.running:
                    message = await websocket.recv()
                    message = json.loads(message)
                    if self.stat_callback:
                        self.stat_callback(message)
        except Exception as e:
            print(f"Error in Rider Stats WebSocket client: {e}")

    async def rider_client(self):
        uri = f"ws://{self.base_url}/riders/ws"
        try:
            async with websockets.connect(uri) as websocket:
                self.rider_websocket = websocket
                self.running = True
                while self.running:
                    message = await websocket.recv()
                    message = json.loads(message)
                    if self.rider_callback:
                        self.rider_callback(message)
        except Exception as e:
            print(f"Error in New Rider WebSocket client: {e}")

    async def scorecard_client(self):
        uri = f"ws://{self.base_url}/scorecards/ws"
        try:
            async with websockets.connect(uri) as websocket:
                self.scorecard_websocket = websocket
                self.running = True
                while self.running:
                    message = await websocket.recv()
                    message = json.loads(message)
                    if self.scorecard_callback:
                        self.scorecard_callback(message)
        except Exception as e:
            print(f"Error in Scorecard WebSocket client: {e}")

    async def parks_client(self):
        uri = f"ws://{self.base_url}/parks/ws"
        try:
            async with websockets.connect(uri) as websocket:
                self.parks_websocket = websocket
                self.running = True
                while self.running:
                    message = await websocket.recv()
                    message = json.loads(message)
                    if self.parks_callback:
                        self.parks_callback(message)
        except Exception as e:
            print(f"Error in Parks WebSocket client: {e}")

    def start_websocket_clients(self):
        print('Starting websocket clients')
        self.running = True
        self.event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.event_loop)
        self.event_loop.run_until_complete(
            asyncio.gather(
                self.stat_client(),
                self.rider_client(),
                self.scorecard_client()
            )
        )

    def stop_websocket_clients(self):
        print('Stopping websocket clients')
        self.running = False
        if self.stat_websocket:
            self.stat_websocket.close()
        if self.rider_websocket:
            self.rider_websocket.close()
        if self.scorecard_websocket:
            self.scorecard_websocket.close()
