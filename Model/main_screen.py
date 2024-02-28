
from Model.base_model import BaseScreenModel


class MainScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.MainScreen.main_screen.MainScreenView` class.
    """

    def __init__(self):
        # Just an example of the data. Use your own values.
        self._parks = None
        self._data = None

    @property
    def parks(self):
        return self._parks

    @parks.setter
    def parks(self, value):
        print('parks setter')
        self._parks = value
        print('parks:', len(self._parks))
        self.notify_observers("riders screen")

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        # We notify the View -
        # :class:`~View.MainScreen.main_screen.MainScreenView` about the
        # changes that have occurred in the data model.
        self.notify_observers("main screen")

    def check_data(self):
        """Just an example of the method. Use your own code."""
        self.notify_observers('main screen')

        self.data = ["example item"]
