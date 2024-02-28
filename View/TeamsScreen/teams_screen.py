from kivymd.uix.responsivelayout import MDResponsiveLayout

from View.TeamsScreen.components import (
    TeamsMobileScreen,
    TeamsTabletScreen,
    TeamsDesktopScreen,
)
from View.base_screen import BaseScreenView


class TeamsScreenView(MDResponsiveLayout, BaseScreenView):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.mobile_view = TeamsMobileScreen()
        self.tablet_view = TeamsTabletScreen()
        self.desktop_view = TeamsDesktopScreen()

    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
