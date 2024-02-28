from kivymd.uix.screen import MDScreen

from View.base_screen import BaseScreenView


class NetworkErrorScreen(BaseScreenView):

    def __init__(self, **kw):
        super().__init__(**kw)

    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """

        if self.model.connection:
            self.manager_screens.current = 'main screen'
            
    def on_enter(self):
        self.controller.check_for_network()