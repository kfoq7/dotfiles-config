from ignis.widgets import Widget
from ignis.services.hyprland import HyprlandService

hyprland = HyprlandService.get_default()

def select_next_kb(_):
    hyprland.main_keyboard.switch_layout("next")


class HyprlandKbLayout(Widget.Button):
    def __init__(self):
        super().__init__(
            css_classes=["kb-layout", "unset"],
            on_click=select_next_kb,
            visible=hyprland.is_available,
            child=Widget.Label(
                label=hyprland.main_keyboard.bind(
                    "active_keymap",
                    transform=lambda value: value[:2].lower()
                )
            )
        )
