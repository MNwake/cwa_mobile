from pprint import pprint

from Model.base_model import BaseScreenModel
from database.utils import calculate_age_group, calculate_division


class RidersScreenModel(BaseScreenModel):
    def __init__(self):
        self._top_ten_list = []
        self._best_trick_list = []
        self._cwa_list = []
        self._overall_list = []

    # Setter and property for top_ten_list
    @property
    def top_ten_list(self):
        return self._top_ten_list

    @top_ten_list.setter
    def top_ten_list(self, sorted_riders):
        sort_key = lambda x: x.top_10.sum if 'top_10' in x and 'sum' in x.top_10 else 0  # Corrected
        self._top_ten_list = self.process_riders(sorted_riders, sort_key)
        self.notify_observers('riders screen')
    # Setter and property for best_trick_list
    @property
    def best_trick_list(self):
        return self._best_trick_list

    @best_trick_list.setter
    def best_trick_list(self, sorted_riders):
        sort_key = lambda x: x.best_trick.sum if 'best_trick' in x and 'sum' in x.best_trick else 0
        self._best_trick_list = self.process_riders(sorted_riders, sort_key)
        self.notify_observers('riders screen')

    # Setter and property for cwa_list
    @property
    def cwa_list(self):
        return self._cwa_list

    @cwa_list.setter
    def cwa_list(self, sorted_riders):
        sort_key = lambda x: x.cwa.sum if 'cwa' in x and 'sum' in x.cwa else 0  # Corrected
        self._cwa_list = self.process_riders(sorted_riders, sort_key)
        self.notify_observers('riders screen')

    # Setter and property for overall_list
    @property
    def overall_list(self):
        return self._overall_list

    @overall_list.setter
    def overall_list(self, sorted_riders):
        sort_key = lambda x: x.overall.sum if 'overall' in x and 'sum' in x.overall else 0
        self._overall_list = self.process_riders(sorted_riders, sort_key)
        self.notify_observers('riders screen')


    def process_riders(self, sorted_riders, sort_key):
        rider_cards = []
        for index, rider in enumerate(sorted_riders, start=1):
            score = round(sort_key(rider), 1)

            division_score = rider.cwa.division
            division = calculate_division(division_score)

            rank = rider.get('ranking', 0)

            rv_data = {
                'viewclass': 'RiderCard',
                'place': str(index),
                'first_name': rider.first_name,
                'last_name': rider.last_name,
                'profile_image': rider.profile_image,
                'home_park': rider.home_park.abbreviation,
                'division': division,
                'rank': str(rank),
                'score': str(score)  # Convert the rounded score to a string
            }
            rider_cards.append(rv_data)

        return rider_cards