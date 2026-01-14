from ignis import widgets
from ignis.services.hyprland import HyprlandService

hyprland = HyprlandService.get_default()


class WorkspacesButton(widgets.Button):
    def __init__(self, workspace_id: int, is_active: bool, exists: bool):
        css_classes = ["workspace", "unset"]
        if is_active:
            css_classes.append("active")

        if not exists:
            css_classes.append("empty")

        # ⬤ - ○ - ◦
        label = str(workspace_id) if exists else "•"

        super().__init__(
            css_classes=css_classes,
            child=widgets.Label(label=label),
            halign="start",
            valign="center",
            on_click=lambda _: hyprland.switch_to_workspace(workspace_id) if hyprland.is_available else None,
        )


class Workspaces(widgets.Box):
    def __init__(self):
        child = []

        if hyprland.is_available:
            child = [
                widgets.EventBox(
                    css_classes=["workspaces"],
                    child=hyprland.bind_many(
                        ["workspaces", "active_workspace"],
                        transform=self.__create_workspace_buttons
                    )
                )
            ]

        super().__init__(child=child)

    def __create_workspace_buttons(self, workspaces, active_workspace):
        existing_ids = {ws.id for ws in workspaces}
        active_id = active_workspace.id if active_workspace else None

        min_workspaces = 10
        max_id = max(existing_ids) if existing_ids else min_workspaces
        workspace_range = max(max_id, min_workspaces)

        return [
            WorkspacesButton(i, i == active_id, i in existing_ids)
            for i in range(1, workspace_range + 1)
        ]
