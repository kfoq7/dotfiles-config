from ignis import widgets
from ignis.window_manager import WindowManager
from ignis.services.network import NetworkService
from ignis.services.audio import AudioService
from ..indicator_icon import  IndicatorIcon, NetworkIndicatorIcon

network =  NetworkService.get_default()
window_manager = WindowManager.get_default()
audio = AudioService.get_default()


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


class EthernetIcon(NetworkIndicatorIcon):
    def __init__(self):
        super().__init__(
            device_type=network.ethernet,
            other_device_type=network.wifi
        )


class VolumeIcon(IndicatorIcon):
    def __init__(self):
        super().__init__(
            image=audio.speaker.bind("icon-name")
        )


class StatusPill(widgets.Button):
    def __init__(self, on_click = None):
        super().__init__(
            css_classes=["unset"],
            valign="center",
            halign="fill",
            style="background-color: #262424; padding: 0.01rem 0.3rem; border-radius: 12px;",
            on_click=toggle_control_panel,
            child=widgets.Box(
                spacing=8,
                child=[
                    WifiIcon(),
                    EthernetIcon(),
                    VolumeIcon(),
                ]
            )
        )
