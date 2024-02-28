# The screen's dictionary contains the objects of the models and controllers
# of the screens of the application.
from Controller.network_error_screen import NetworkErrorController
from Model.base_model import BaseScreenModel
from Model.main_screen import MainScreenModel
from Controller.main_screen import MainScreenController
from Model.riders_screen import RidersScreenModel
from Controller.riders_screen import RidersScreenController
from Model.teams_screen import TeamsScreenModel
from Controller.teams_screen import TeamsScreenController
from Model.live_feed_screen import LiveFeedScreenModel
from Controller.live_feed_screen import LiveFeedScreenController
from Model.network_error_screen import NetworkErrorModel




screens = {
    'main screen': {
        'model': MainScreenModel,
        'controller': MainScreenController,
    },
    'teams screen': {
        'model': TeamsScreenModel,
        'controller': TeamsScreenController,
    },
    'riders screen': {
        'model': RidersScreenModel,
        'controller': RidersScreenController,
    },
    'live feed screen': {
        'model': LiveFeedScreenModel,
        'controller': LiveFeedScreenController
    },
    'network error screen': {
        'model': NetworkErrorModel,
        'controller': NetworkErrorController,
    }
}