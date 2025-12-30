from gi.repository import GObject # pyright: ignore[]

from ignis import widgets
from ignis.base_widget import BaseWidget
from ignis.variable import Variable

opened_menu = Variable()


class Menu(widgets.Revealer):
    def __init__(self, name: str, child: list[BaseWidget], **kwargs):
        self.__name = name
        self.__box = widgets.Box(
            vertical=True,
            css_classes=["control-center-menu"],
            child=child
        )

        super().__init__(
            transition_type="slide_down",
            transition_duration=300,
            reveal_child=opened_menu.bind(
                "value",
                lambda value: value == self.__name
            ),
            child=self.__box,
            **kwargs
        )

    def toggle(self):
        if self.reveal_child:
            opened_menu.set_value("")
            return

        opened_menu.set_value(self.__name)

    @GObject.Property
    def box(self):
        return self.__box
