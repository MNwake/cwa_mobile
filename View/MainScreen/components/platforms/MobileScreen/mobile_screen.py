from kivymd.uix.navigationbar import MDNavigationBar, MDNavigationItem
from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty, StringProperty
from View.MainScreen.components.platforms.MobileScreen.components import BottomNavBar  # NOQA


class MobileScreenView(MDScreen):
    model = ObjectProperty()
    controller = ObjectProperty()
    title = StringProperty()


    def update_rider_filters(self, filters):
        self.controller.update_rider_filters(filters)



