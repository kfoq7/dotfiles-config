from ignis.services.hyprland import HyprlandService

hyprland = HyprlandService.get_default()

hyprland.main_keyboard.switch_layout("next")
