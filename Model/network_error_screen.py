from Model.base_model import BaseScreenModel


class NetworkErrorModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.MainScreen.main_screen.MainScreenView` class.
    """

    def __init__(self):
        # Just an example of the data. Use your own values.
        self.connection = None
        self._data = None

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

    def check_data(self, dt=None):
        """Just an example of the method. Use your own code."""
        print('check data')
        self.connection = self.database.check_network_connection()
        self.notify_observers('network error screen')
