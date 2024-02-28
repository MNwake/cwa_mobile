from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.chip import MDChip


class MyChip(MDChip):
    text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        app = MDApp.get_running_app()
        # self.md_bg_color = app.theme_cls.onPrimaryColorContainer
        # self.selected_color = self.app.theme_cls.primaryColor
