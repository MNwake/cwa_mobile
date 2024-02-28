
from Model.base_model import BaseScreenModel


class LiveFeedScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.LiveFeedScreen.live_feed_screen.LiveFeedScreenView` class.
    """

    def __init__(self):
        super().__init__()
        self._scorecards = []  # Initialize with default empty list
        self._events = []  # Initialize with default empty list
        self._ads = []  # Initialize with default empty list

    @property
    def scorecards(self):
        return self._scorecards

    @scorecards.setter
    def scorecards(self, value):
        self._scorecards = value
        self.notify_observers("live feed screen")  # Notify observers of the update

    @property
    def events(self):
        return self._events

    @events.setter
    def events(self, value):
        self._events = value
        self.notify_observers("live feed screen")  # Notify observers of the update

    @property
    def adcards(self):
        return self._ads

    @adcards.setter
    def adcards(self, value):
        self._ads = value
        self.notify_observers("live feed screen")