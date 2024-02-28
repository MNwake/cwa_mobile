from pprint import pprint

from kivy.properties import ObjectProperty, BooleanProperty
from kivymd.uix.screen import MDScreen
from kivymd.uix.tab import MDTabsItem, MDTabsItemText, MDTabsPrimary

from View.RidersScreen.components.platforms.MobileScreen.components import RiderCard, MyTabs  # NOQA


class RidersMobileScreen(MDScreen):
    controller = ObjectProperty()
    model = ObjectProperty()
    network_connection = BooleanProperty(defaultvalue=False)
    rider_filters = ObjectProperty()
    stat_filters = ObjectProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.error_card = None
        self.lists_by_category = {
            'Overall': [],
            'CWA': [],
            'Best Trick': [],
            'Top 10': []
        }

        # Create tabs based on the keys of lists_by_category
        for tab_name in self.lists_by_category.keys():
            widget = MyTabs(MDTabsItemText(text=tab_name), tag=tab_name)
            self.ids.tabs.add_widget(widget)

        if self.ids.tabs.get_tabs_list():
            self.ids.tabs.current_tab = self.ids.tabs.get_tabs_list()[0]

    def change_ranking_list(self, tabs: MDTabsPrimary, item: MDTabsItem, unknown=None):
        tab_text = item.tag
        if tab_text in self.lists_by_category:
            self.ids.rv.data = self.lists_by_category[tab_text]

    def model_is_changed(self):
        # When the model changes, update all lists
        self.lists_by_category['Overall'] = self.model.overall_list
        self.lists_by_category['CWA'] = self.model.cwa_list
        self.lists_by_category['Best Trick'] = self.model.best_trick_list
        self.lists_by_category['Top 10'] = self.model.top_ten_list
        # Update the RV with the current tab's data
        current_tab = self.ids.tabs.current_tab.tag
        self.ids.rv.data = self.lists_by_category[current_tab]

    def view_rider(self, rider):
        print(rider['first_name'], rider['profile_image'])



    def clear_search(self, instance, text):
        instance.rider_on_deck = ''
        instance.text = instance.rider

    def focus_rider_search(self, instance, focus):
        if focus and instance.text == 'Select Rider':
            instance.text = ''
        elif not focus and instance.text == '':
            instance.text = 'Select Rider'

    def toggle_bottom_sheet(self):
        self.ids.filter_sheet.set_state('toggle')



