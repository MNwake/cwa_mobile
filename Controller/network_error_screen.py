from kivy.clock import Clock

import View.NetworkErrorScreen.network_error


class NetworkErrorController:
    """
    The `RidersScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model, database):
        self.model = model  # Model.riders_screen.RidersScreenModel
        self.database = database
        self.view = View.NetworkErrorScreen.network_error.NetworkErrorScreen(controller=self, model=self.model)

    def get_view(self) -> View.NetworkErrorScreen.network_error:
        return self.view
