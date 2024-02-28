from kivy.properties import StringProperty, NumericProperty
from kivymd.uix.appbar import MDActionTopAppBarButton, MDTopAppBarTitle
from kivymd.uix.behaviors import RotateBehavior
from kivymd.uix.expansionpanel import MDExpansionPanel
from kivymd.uix.slider import MDSlider


class CustomSlider(MDSlider):
    tag = StringProperty()


class ExpansionPanelRider(MDExpansionPanel):
    title = StringProperty(defaultvalue='')
    min_value = NumericProperty(defaultvalue=0)
    max_value = NumericProperty(defaultvalue=100)
    gender = StringProperty()

    def tap_expansion_chevron(
            self, panel: MDExpansionPanel, chevron
    ):
        panel.open() if not panel.is_open else panel.close()
        panel.set_chevron_down(
            chevron
        ) if not panel.is_open else panel.set_chevron_up(chevron)


    def value_change(self, instance, value):
        if instance.tag == 'min':
            self.min_value = value
            # self.adjust_max_value(value)
        else:
            self.max_value = value
        #     self.adjust_min_value(value)


    def release_slider(self, instance, touch):
        if instance.tag == 'min' and instance.value > self.max_value:
            self.max_value = self.min_value
        if instance.tag == 'max' and instance.value < self.min_value:
            self.min_value = self.max_value



