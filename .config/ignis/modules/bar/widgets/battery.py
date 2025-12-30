from ignis import widgets
from ignis.services.upower import UPowerService, UPowerDevice

upower = UPowerService.get_default()


class BatteryItem(widgets.Box):
    def __init__(self, device: UPowerDevice):
        self._device = device

        super().__init__(
            setup=lambda self: device.connect("removed", lambda _: self.unparent()),
            vertical=False,
            # style="--progress:15;",
            style=device.bind(
                "percent",
                lambda percent: f"--progress:{percent};"
            ),
            css_classes=device.bind_many(
                ["charging", "percent"],
                lambda charging, percent: self._get_css_classes(charging, percent),
            ),
            child=[
                # widgets.Icon(
                    # image=device.bind("icon_name", lambda icon: Utils.get_paintable(icon, device.icon_name, size=32)),
                #     image=device.bind("icon_name"),
                #     css_classes=["battery-icon"]
                # ),
                widgets.Label(
                    # label=device.bind("percent", lambda x: f"{int(x)}%"),
                    label=self._get_battery_charging(),
                    css_classes=["battery-percent"]
                )
            ]
        )

    def _get_battery_charging(self):
        label= self._device.bind_many(
            ["charging", "percent"],
            lambda charging, percent: f"{"󱐋" if self._is_charging(charging) else ""}{int(percent)}%"
        )

        return label

    def _is_charging(self, charging):
        return charging in (1, 4)

    def _get_css_classes(self, charging, percent):
        classes = ["battery"]
        if charging in (1, 4):
            classes.append("charging")
        if percent <= 20:
            classes.append("battery-low")
        return classes


class Battery(widgets.Box):
    def __init__(self):
        super().__init__(
            setup=lambda self: upower.connect(
                "battery-added", lambda _, device: self.append(BatteryItem(device))
            )
        )
