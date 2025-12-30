from ignis import widgets
from ignis.window_manager import WindowManager
from ignis.services.network import NetworkService
from ..indicator_icon import  NetworkIndicatorIcon

network =  NetworkService.get_default()
window_manager = WindowManager.get_default()

def toggle_control_panel(_):
    window = window_manager.get_window("ignis_CONTROL_CENTER")
    if window:
        window.set_visible(not window.visible)


class WifiIcon(NetworkIndicatorIcon):
    def __init__(self):
        super().__init__(
            device_type=network.wifi,
            other_device_type=network.ethernet
        )

class StatusPill(widgets.Button):
    def __init__(self):
        super().__init__(
            css_classes=["unset"],
            on_click=toggle_control_panel,
            child=widgets.Box(
                child=[
                    WifiIcon(),
                    # widgets.Label(
                    #     label="Hello :D"
                    # )
                ]
            )
        )
