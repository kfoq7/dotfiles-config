from ignis import widgets
from ignis.services.network import NetworkService

from .widgets import User

network = NetworkService.get_default()

# class WifiIcon():
#     def __init__(self) -> None:
#         super().__init__(
#             device_type=network.wifi
#         )


class ControCenter(widgets.RevealerWindow):
    def __init__(self):
        revealer = widgets.Revealer(
            transition_type="slide_left",
            transition_duration=300,
            reveal_child=True,
            child=widgets.Box(
                vertical=True,
                css_classes=["control-center"],
                child=[
                    widgets.Box(
                        vertical=True,
                        css_classes=["control-center-widget"],
                        child=[User()]
                    )
                ]
            )
        )

        super().__init__(
            visible=False,
            popup=True,
            kb_mode="on_demand",
            layer="top",
            css_classes=["unset"],
            anchor=["top", "right", "bottom", "left"],
            namespace="ignis_CONTROL_CENTER",
            revealer=revealer,
            # setup=lambda self: self.connect(
            #     "notify::visible",
            #     lambda x, y: opened_menu.set_value("")
            # ),
            child=widgets.Box(
                child=[
                    widgets.Button(
                        vexpand=True,
                        hexpand=True,
                        css_classes=["unset"]
                    ),
                    revealer
                ]
            )
        )
