from kivy.properties import StringProperty
from kivymd.uix.fitimage import FitImage


class RiderThumb(FitImage):
    profile_image = StringProperty('assets/images/default-avatar.png')
