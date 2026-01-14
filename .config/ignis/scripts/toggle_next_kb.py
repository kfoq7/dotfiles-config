from ignis.services.hyprland import HyprlandService

hyprland = HyprlandService.get_default()

if hyprland.is_available:
    hyprland.main_keyboard.switch_layout("next")

