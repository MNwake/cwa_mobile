from kivy.properties import StringProperty
from kivymd.uix.tab import MDTabsItem


class MyTabs(MDTabsItem):
    tag = StringProperty()