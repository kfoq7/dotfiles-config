from ignis import widgets
from ignis.services.notifications import NotificationService

from .widgets import (
    Workspaces,
    Battery,
    HyprlandKbLayout,
    StatusPill,
    SystemStats
)
from .widgets.distro_icon import DistroIcon
from modules.shared import Clock

notifications = NotificationService.get_default()


class Bar(widgets.Window):
    __gtype_name__ = "Bar"

    def __init__(self):
        super().__init__(
            css_classes=["bar-widget"],
            anchor=["left", "top", "right"],
            exclusivity="exclusive",
            monitor=0,
            namespace="ignis_BAR",
            layer="top",
            kb_mode="none",
            margin_left=4,
            margin_right=4,
            margin_top=4,
            margin_bottom=2,
            child=widgets.CenterBox(
                css_classes=["bar-widget"],
                start_widget=self.__left(),
                center_widget=self.__center(),
                end_widget=self.__right()
            )
        )

    def __left(self):
        return widgets.Box(
            spacing=10,
            child=[
                DistroIcon(),
                SystemStats(),
                # CurrentPath(),
            ]
        )

    def __center(self):
        return widgets.Box(
            spacing=10,
            child=[
                Workspaces(),
                Clock(),
                Battery(),
            ],
        )

    def __right(self):
        return widgets.Box(
            spacing=10,
            child=[
                HyprlandKbLayout(),
                # self.__current_notification(),
                StatusPill(),
            ],
        )

    def __current_notification(self):
        return widgets.Label(
            ellipsize="end",
            max_width_chars=20,
            label=notifications.bind(
                "notifications",
                lambda value: value[-1].summary if len(value) > 0 else None
            )
        )
