from ignis.services.hyprland import HyprlandService
from ignis import widgets

hyprland = HyprlandService.get_default()

class CurrentPath(widgets.Label):
    __gtype_name__ = "CurrentPath"

    def __init__(self):
        super().__init__(
            style="font-weight: 500;",
            label=hyprland.bind(
                "active_window",
                transform=lambda w: self._parse_path(w.title) if w and w.title else ""
            )
        )

    def _parse_path(self, title: str) -> str:
        try:
            parts = title.split(" ")
            if len(parts) >= 4:
                path = parts[1].replace("(", "").replace(")", "")
                app = parts[3]
                return f"{app} {path}"

            return title
        except Exception:
            return ""
