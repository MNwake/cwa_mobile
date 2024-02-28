from kivy.properties import StringProperty, OptionProperty, NumericProperty
from kivymd.uix.card import MDCard


class RiderCard(MDCard):
    place = StringProperty()
    first_name = StringProperty()
    last_name = StringProperty()
    profile_image = StringProperty()
    home_park = StringProperty()
    score = StringProperty()
    division = StringProperty()
    rank = StringProperty()