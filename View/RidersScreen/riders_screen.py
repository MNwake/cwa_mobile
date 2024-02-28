import asyncio
from pprint import pprint

from kivy.clock import Clock
from kivy.properties import DictProperty
from kivymd.uix.responsivelayout import MDResponsiveLayout

from View.RidersScreen.components import (
    RidersMobileScreen,
    RidersTabletScreen,
    RidersDesktopScreen,
)
from View.base_screen import BaseScreenView


class RidersScreenView(MDResponsiveLayout, BaseScreenView):
    rider_filters = DictProperty()
    stat_filters = DictProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.mobile_view = RidersMobileScreen(controller=self.controller, model=self.model)
        self.tablet_view = RidersTabletScreen()
        self.desktop_view = RidersDesktopScreen()
        self.current_view = self.mobile_view


    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
        self.mobile_view.model_is_changed()
        self.tablet_view.model_is_changed()
        self.desktop_view.model_is_changed()

    def on_change_screen_type(self, screen_type):
        if screen_type == 'mobile':
            self.current_view = self.mobile_view
        elif screen_type == 'tablet':
            self.current_view = self.tablet_view
        elif screen_type == 'desktop':
            self.current_view = self.desktop_view

    def on_enter(self):
        self.model_is_changed()
        self.current_view.ids.tabs.switch_tab('Overall')
        print('enter')

    def on_leave(self):
        print('leaving', self.name)

    def open_filter_sheet(self):
        if self.current_view.ids.filter_sheet:
            self.current_view.ids.filter_sheet.set_state('toggle')