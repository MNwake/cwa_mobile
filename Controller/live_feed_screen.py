import asyncio
import importlib

import asynckivy

import View.LiveFeedScreen.live_feed_screen

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.LiveFeedScreen.live_feed_screen)




class LiveFeedScreenController:
    """
    The `LiveFeedScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model, database):
        self.scorecard_cursor = None
        self.model = model  # Model.live_feed_screen.LiveFeedScreenModel
        self.database = database
        self.view = View.LiveFeedScreen.live_feed_screen.LiveFeedScreenView(controller=self, model=self.model)
        # self.database.scorecards_callback = self.update_scorecards
        self.database.websocket_manager.scorecard_callback = self.receive_scorecard_ws_message
        # self.fetch_recent_feed()
        # self.model.scores = self.database.get_scorecards(cursor=self.cursor)
        # self.model.scorecards = self.database.get_scorecards()

    def get_view(self) -> View.LiveFeedScreen.live_feed_screen:
        return self.view

    def async_button(self):
        async def button():
            scorecards, cursor = await self.database.fetch_recent_scorecards(cursor=self.scorecard_cursor)
            print(scorecards)
            print(cursor)
            print()

        asynckivy.start(button())

    def receive_scorecard_ws_message(self, message):
        print("Received scorecard message:", message)

