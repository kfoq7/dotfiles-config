from ignis import widgets, utils
from ignis.services.fetch import FetchService

fetch = FetchService.get_default()


class DistroIcon(widgets.Button):
    def __init__(self):
        super().__init__(
            # Check the style for button
            css_classes=["distro-icon", "unset"],
            # child=widgets.Icon(
            #     image=fetch.os_logo,
            #     pixel_size=16,
            # ),
            child=widgets.Label(label="󰣇"),
            on_click=lambda _: utils.exec_sh("fuzzel"),  # Optional: open app launcher
        )

