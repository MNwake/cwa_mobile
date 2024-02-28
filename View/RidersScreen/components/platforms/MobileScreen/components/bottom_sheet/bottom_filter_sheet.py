import asyncio

import asynckivy
from kivy.metrics import dp
from kivy.properties import ObjectProperty, NumericProperty, OptionProperty, StringProperty, ListProperty
from kivymd.uix.bottomsheet import MDBottomSheet
from kivymd.uix.chip import MDChip, MDChipText

from View.RidersScreen.components.platforms.MobileScreen.components import ExpansionPanelRider, ChipStack, MyChip
from database import Division, AgeGroup, Gender, Stance, Section
from database.utils import Filters, get_filter_enums


# noinspection SpellCheckingInspection
class BottomFilterSheet(MDBottomSheet):
    filters = ListProperty()
    model = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.filter_enums = None

    def on_kv_post(self, base_widget):
        self.filter_enums = get_filter_enums()

        # self.parks = self.model.parks
        self.create_chips_async()

    def create_chips_async(self):
        async def set_filter_chips():
            for filter_type in Filters:
                self.add_chipstack(filter_type.name, filter_type.value)
        asynckivy.start(set_filter_chips())

    def add_chipstack(self, label, enum_class):
        print('chipstack')
        print(enum_class)
        print(type(enum_class))
        chipstack = ChipStack(
            text=str(label),
            md_bg_color=self.md_bg_color,
            chip_list=enum_class,
            set_filter_callback=self.set_filter
        )
        chipstack.set_filter_callback = self.set_filter
        chipstack.bind(on_open=lambda instance: self.close_panels(chipstack))
        self.ids.content_container.add_widget(chipstack)


    def set_filter(self, chipstack: ChipStack, chip: MyChip, active: bool) -> None:
        '''Sets a list of tags for filtering icons.'''
        item = {chipstack.text.lower(): chip.text.lower()}
        if active:
            self.filters.append(item)
        else:
            if item in self.filters:
                self.filters.remove(item)
        print('sefl.filters', self.filters)


    def close_panels(self, panel):
        print('close panels')
        for item in self.ids.content_container.children:
            if item != panel and panel.is_open:
                item.set_chevron_up(
                    item.ids.chevron
                )
                item.close()

