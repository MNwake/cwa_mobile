import importlib
from pprint import pprint

import View.TeamsScreen.teams_screen

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.TeamsScreen.teams_screen)


class TeamsScreenController:
    """
    The `TeamsScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model, database):
        self.model = model  # Model.teams_screen.TeamsScreenModel
        self.database = database
        self.view = View.TeamsScreen.teams_screen.TeamsScreenView(controller=self, model=self.model)
    def get_view(self) -> View.TeamsScreen.teams_screen:
        return self.view

    def utility_button(self):
        pprint(self.database.parks)

