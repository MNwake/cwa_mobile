import time

from box import Box


class DataModel:
    def __init__(self):
        self._rider_stats = None
        self._riders = None
        self._scorecards = None
        self._parks = None
        self._stats = None
        self.callback = None

    @property
    def parks(self):
        return self._parks

    @parks.setter
    def parks(self, value):
        print('parks setter')
        processed = self.update_parks(value)
        self._parks = processed

        print('parks:', len(self._parks))

    @property
    def riders(self):
        return self._riders

    @riders.setter
    def riders(self, value):
        print('riders setter')
        processed = self.update_rider(value)
        if isinstance(processed, list):
            self._riders = [Box(rider) for rider in processed]  # Convert each dict to a Box
            if self.callback:
                self.callback()
        else:
            print('Error: Processed data is not a list')

    @property
    def stats(self):
        return self._stats

    @stats.setter
    def stats(self, value):
        print('stats setter')
        processed = self.update_stats(value)
        self._stats = processed
        print(len(value))

    @property
    def scorecards(self):
        return self._scorecards

    @scorecards.setter
    def scorecards(self, value):
        print('scorecards setter')
        processed = self.update_scorecards(value)
        self._scorecards = value

    def update_rider(self, value):
        riders = self.add_additional_stats(value)
        riders = self.add_home_park(riders)
        if riders:
            print('update rider final rider:')
            print(len(riders))

        return self.calculate_rankings(riders)

    def calculate_rankings(self, rider_list):
        # Sort the riders based on 'cwa.division' in descending order
        sorted_riders = sorted(rider_list, key=lambda r: r.get('cwa', {}).get('division', 0), reverse=True)

        # Assign rankings based on sorted order
        for index, rider in enumerate(sorted_riders, start=1):
            rider['ranking'] = index

        return sorted_riders

    def find_matching_stat(self, rider_id):
        if self.stats:
            for stat in self.stats:
                if isinstance(stat, dict) and stat.get('rider') == rider_id:
                    return stat
            return None

    def extract_additional_stats(self, category, stats, method):
        if category not in stats:
            print(f"Invalid category {category}")
            return {}

        # Initialize variables to store aggregated values
        execution_value = difficulty_value = creativity_value = division_value = 0
        airtrick_value = rail_value = kicker_value = 0

        # Assuming each item in stats[category] is a dictionary
        for stat_item in stats[category]:
            if 'score' in stat_item:
                score_data = stat_item['score']
                execution_value += score_data.get('execution', {}).get(method, 0)
                difficulty_value += score_data.get('difficulty', {}).get(method, 0)
                creativity_value += score_data.get('creativity', {}).get(method, 0)
                division_value += score_data.get('division', {}).get(method, 0)

            if 'section' in stat_item:
                section_data = stat_item['section']
                airtrick_value += section_data.get('air trick', {}).get(method, 0)
                rail_value += section_data.get('rail', {}).get(method, 0)
                kicker_value += section_data.get('kicker', {}).get(method, 0)

        # Assuming you want to return the sum/aggregate of the values
        return {
            category: {
            'execution': execution_value,
            'difficulty': difficulty_value,
            'creativity': creativity_value,
            'division': division_value,
            'air_trick': airtrick_value,
            'rail': rail_value,
            'kicker': kicker_value,
            'sum': execution_value + difficulty_value + creativity_value + difficulty_value + airtrick_value + rail_value + kicker_value
            }
        }

        return True  # Return True for any other filter type

    def add_additional_stats(self, riders):
        for rider in riders:
            rider_id = rider.get('id')
            matched_stats = self.find_matching_stat(rider_id)  # Use a different variable
            if matched_stats:
                # Update the rider with stats
                rider.update(self.extract_additional_stats('overall', matched_stats, 'mean'))
                rider.update(self.extract_additional_stats('cwa', matched_stats, 'mean'))
                rider.update(self.extract_additional_stats('top_10', matched_stats, 'mean'))
                rider.update(self.extract_additional_stats('best_trick', matched_stats, 'max'))
        return riders

    def add_home_park(self, riders):
        for rider in riders:
            # Check if 'home_park' is already a dict and skip if it is
            if isinstance(rider.get('home_park'), dict):
                continue

            home_park_id = rider.get('home_park')
            matched_park = self.find_matching_park(home_park_id)
            if matched_park:
                # Update the rider's 'home_park' to be the matched park dict
                rider['home_park'] = matched_park

        if riders:
            print(riders[0])
        return riders

    def find_matching_park(self, park_id):
        if self.parks:
            for park in self.parks:
                if isinstance(park, dict) and park.get('id') == park_id:
                    return park
            return None

    def update_parks(self, value):
        return value

    def update_stats(self, value):
        return value

    def update_scorecards(self, value):
        return value