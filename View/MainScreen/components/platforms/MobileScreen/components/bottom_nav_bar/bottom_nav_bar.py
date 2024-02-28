from kivy.properties import StringProperty
from kivymd.uix.navigationbar import MDNavigationItem, MDNavigationBar


class BaseMDNavigationItem(MDNavigationItem):
    icon = StringProperty()
    text = StringProperty()
    screen = StringProperty()

class BottomNavBar(MDNavigationBar):
    pass

