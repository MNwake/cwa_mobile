from kivymd.uix.responsivelayout import MDResponsiveLayout

from View.LiveFeedScreen.components import (
    LiveFeedMobileScreen,
    LiveFeedTabletScreen,
    LiveFeedDesktopScreen,
)
from View.base_screen import BaseScreenView


class LiveFeedScreenView(MDResponsiveLayout, BaseScreenView):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.mobile_view = LiveFeedMobileScreen(controller=self.controller)
        self.tablet_view = LiveFeedTabletScreen()
        self.desktop_view = LiveFeedDesktopScreen()

    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
