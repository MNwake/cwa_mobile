
from Model.base_model import BaseScreenModel



class TeamsScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.TeamsScreen.teams_screen.TeamsScreenView` class.
    """

    def __init__(self):
        # Just an example of the data. Use your own values.
        self._data = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        # We notify the View -
        # :class:`~View.TeamsScreen.teams_screen.TeamsScreenView` about the
        # changes that have occurred in the data model.
        self.notify_observers("teams screen")

    def check_data(self):
        """Just an example of the method. Use your own code."""

        self.data = ["example item"]
