from ignis.services.hyprland import HyprlandService
from ignis.widgets import Widget


class CurrentPath(Widget.Label):
    __gtype_name__ = "CurrentPath"

    def __init__(self):
        # hyprland = HyprlandService.get_default()

        super().__init__(
            style="font-weight: lighter;",
            label="asdf"
            # label=hyprland.bind("active_window", lambda w: w.class_name if w else "")
        )
