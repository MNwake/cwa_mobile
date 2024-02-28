from kivy.properties import StringProperty, ColorProperty, ObjectProperty, BooleanProperty
from kivymd.uix.chip import MDChip
from kivymd.uix.expansionpanel import MDExpansionPanel

from View.RidersScreen.components.platforms.MobileScreen.components import MyChip
from View.components import TrailingPressedIconButton


class ChipStack(MDExpansionPanel):
    text = StringProperty()
    chip_list = ObjectProperty()
    md_bg_color = ColorProperty()
    set_filter_callback = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_chips()

    def create_chips(self):
        for chip_value in self.chip_list:
            chip = MyChip(text=chip_value.value, type='filter')
            chip.bind(active=self.uncheck_chip)
            if chip.text.lower() == 'all':
                chip.active = True

            self.ids.chip_stack.add_widget(chip)

    def uncheck_chip(self, current_chip: MDChip, active: bool) -> None:
        '''Removes a mark from an already marked chip.'''

        if active:
            # Deactivate all other chips
            for chip in self.ids.chip_stack.children:
                if current_chip is not chip and chip.active:
                    chip.active = False

            # Check if any chip is active
        any_chip_active = any(chip.active for chip in self.ids.chip_stack.children if isinstance(chip, MyChip))

        # If no chip is active, activate 'all' chip
        if not any_chip_active:
            all_chip = next((chip for chip in self.ids.chip_stack.children if
                             isinstance(chip, MyChip) and chip.text.lower() == 'all'), None)
            if all_chip:
                all_chip.active = True

        # Call the callback
        if self.set_filter_callback:
            self.set_filter_callback(self, current_chip, active)
    def tap_expansion_chevron(
        self, panel: MDExpansionPanel, chevron: TrailingPressedIconButton
    ):
        panel.open() if not panel.is_open else panel.close()
        panel.set_chevron_down(
            chevron
        ) if not panel.is_open else panel.set_chevron_up(chevron)


