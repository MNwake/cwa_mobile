"""
Script for managing hot reloading of the project.
For more details see the documentation page -

https://kivymd.readthedocs.io/en/latest/api/kivymd/tools/patterns/create_project/

To run the application in hot boot mode, execute the command in the console:
DEBUG=1 python main.py
"""
import threading

import asynckivy
from kivy.clock import Clock

from database.database import DataBase

# TODO: You may know an easier way to get the size of a computer display.


# Place the application window on the right side of the computer screen.

from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager

from View.screens import screens


class app(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.websocket_thread = None
        self.load_all_kv_files(self.directory)
        # This is the screen manager that will contain all the screens of your
        # application.
        self.manager_screens = MDScreenManager()
        self.database = DataBase()

    def build(self) -> MDScreenManager:
        self.theme_cls.primary_palette = 'Aliceblue'
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.dynamic_color = True
        self.generate_application_screens()
        Clock.schedule_interval(self.start_http, 60)
        self.start_http()
        self.start_websockets()
        return self.manager_screens

    def generate_application_screens(self) -> None:
        """
        Creating and adding screens to the screen manager.
        You should not change this cycle unnecessarily. He is self-sufficient.

        If you need to add any screen, open the `View.screens.py` module and
        see how new screens are added according to the given application
        architecture.
        """
        for i, name_screen in enumerate(screens.keys()):
            model = screens[name_screen]["model"]()
            controller = screens[name_screen]["controller"](model, self.database)
            view = controller.get_view()
            view.manager_screens = self.manager_screens
            view.name = name_screen
            self.manager_screens.add_widget(view)

    def start_http(self, dt=None):
        self.http_thread = threading.Thread(target=self.fetch_all_data)
        self.http_thread.daemon = True
        self.http_thread.start()

    def start_websockets(self):
        self.websocket_thread = threading.Thread(target=self.database.websocket_manager.start_websocket_clients)
        self.websocket_thread.daemon = True
        self.websocket_thread.start()

    def fetch_all_data(self, dt=None):
        async def fetch_all_data_async():
            self.database.data.parks = await self.database.fetch_all_parks()
            self.database.data.stats = await self.database.fetch_all_stats()
            self.database.data.riders = await self.database.fetch_all_riders()

        asynckivy.start(fetch_all_data_async())


if __name__ == '__main__':
    app().run()
