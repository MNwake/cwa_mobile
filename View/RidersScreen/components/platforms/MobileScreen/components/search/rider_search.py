from kivy.properties import StringProperty, ObjectProperty
from kivymd.uix.textfield import MDTextField


class RiderSearch(MDTextField):
    rider = StringProperty()
    clear = ObjectProperty()

    def clear_text(self):
        if self.clear:
            self.clear(self, self.text)

