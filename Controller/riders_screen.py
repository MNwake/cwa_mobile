import importlib
from datetime import datetime
from pprint import pprint

import View.RidersScreen.riders_screen
from database import DataModel

from database.utils import calculate_age_group, calculate_division

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.RidersScreen.riders_screen)


class RidersScreenController:
    def __init__(self, model, database):
        self.filters = None
        self.model = model
        self.database = database
        self.view = View.RidersScreen.riders_screen.RidersScreenView(controller=self, model=self.model)
        self.database.data.callback = self.set_rider_lists

    def get_view(self) -> View.RidersScreen.riders_screen:
        return self.view

    def update_rider_filters(self, filters, *args):
        print('contorller filters', filters)
        self.filters = filters
        self.set_rider_lists()
        # self.model.rider_stats = self.rankings.update_rider()

    def set_rider_lists(self):
        filtered_riders = self.filter_riders()

        # Sort and set the lists for each category
        self.model.overall_list = sorted(filtered_riders, key=lambda x: x.overall.sum if 'overall' in x and 'sum' in x.overall else 0, reverse=True)
        self.model.cwa_list = sorted(filtered_riders, key=lambda x: x.cwa.sum if 'cwa' in x and 'sum' in x.cwa else 0, reverse=True)
        self.model.best_trick_list = sorted(filtered_riders, key=lambda x: x.best_trick.sum if 'best_trick' in x and 'sum' in x.best_trick else 0, reverse=True)
        self.model.top_ten_list = sorted(filtered_riders, key=lambda x: x.top_10.sum if 'top_10' in x and 'sum' in x.top_10 else 0, reverse=True)


    def filter_riders(self):
        if not self.filters:
            print('filters not found')
            return []
        filtered_riders = []
        if not self.database.data.riders:
            print('no riders in database')
            return []

        for rider in self.database.data.riders:
            if self.filter_rider(rider):
                filtered_riders.append(rider)
        return filtered_riders

    def filter_rider(self, rider):
        for filter_item in self.filters:
            # Check if filter_item is a dictionary with exactly one key-value pair
            if isinstance(filter_item, dict) and len(filter_item) == 1:
                filter_type, filter_value = next(iter(filter_item.items()))
                if not self.apply_filter(rider, filter_type, filter_value):
                    return False
            else:
                print("Incorrect filter format:", filter_item)
                # Handle the case where the filter format is not as expected
                # For example, you might skip this filter, raise an error, or handle it differently

        return True

    def apply_filter(self, rider, filter_type, filter_value):
        if filter_value == 'all':
            return True

        if filter_type == 'age':
            rider_dob_str = rider.get('date_of_birth')
            if rider_dob_str:
                # Convert the string to a datetime object
                try:
                    rider_dob = datetime.strptime(rider_dob_str.split('T')[0], '%Y-%m-%d')
                    return filter_value.lower() == calculate_age_group(rider_dob).lower()
                except ValueError:
                    return False
        elif filter_type == 'gender':
            return rider.get('gender', '').lower() == filter_value.lower()
        elif filter_type == 'stance':
            return rider.get('stance', '').lower() == filter_value.lower()
        elif filter_type == 'divisions':
            division = calculate_division(rider.get('cwa', {}).get('division', 0))
            return division.lower() == filter_value.lower()
