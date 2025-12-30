import datetime

from ignis import utils, widgets

class Clock(widgets.Label):
    __gtype_name__ = "Clock"

    def __init__(self):
        super().__init__(
            label=utils.Poll(
                1_000,
                lambda _: datetime.datetime.now().strftime("%a %d/%m - %H:%M")
            ).bind("output")
        )
