from kivy.clock import Clock
from kivymd.uix.navigationbar import MDNavigationBar, MDNavigationItem
from kivymd.uix.responsivelayout import MDResponsiveLayout

from View.MainScreen.components import (
    MobileScreenView,
    TabletScreenView,
    DesktopScreenView,
)
from View.base_screen import BaseScreenView


class MainScreenView(MDResponsiveLayout, BaseScreenView):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.mobile_view = MobileScreenView(model=self.model, controller=self.controller)
        self.tablet_view = TabletScreenView()
        self.desktop_view = DesktopScreenView()
        self.current_view = None

    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """


    def on_change_screen_type(self, screen_type):
        if screen_type == 'mobile':
            self.current_view = self.mobile_view
        elif screen_type == 'tablet':
            self.current_view = self.tablet_view
        elif screen_type == 'desktop':
            self.current_view = self.desktop_view


    def on_enter(self):
        Clock.schedule_once(self.set_landing_screen, 1)

    def switch_tabs(
            self,
            bar: MDNavigationBar,
            item: MDNavigationItem,
            item_icon: str,
            item_text: str,
    ):
        if self.current_view.ids.screen.children:
            current_screen = self.current_view.ids.screen.children[0]
            current_screen.on_leave()
            self.current_view.ids.screen.clear_widgets()
        screen = self.manager_screens.get_screen(item.screen)
        self.current_view.ids.screen.add_widget(screen)
        self.controller.current_view = screen
        screen.on_enter()


    def set_landing_screen(self, dt):
        self.mobile_view.ids.screen.add_widget(self.manager_screens.get_screen('live feed screen'))
