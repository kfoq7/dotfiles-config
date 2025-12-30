from ignis import widgets, utils
from ignis.services.fetch import FetchService

fetch = FetchService.get_default()


class SystemStats(widgets.Box):
    def __init__(self):
        self._cpu_usage = 0.0
        self._prev_total = 0
        self._prev_idle = 0

        super().__init__(
            css_classes=["system-stats", "bar-widget"],
            spacing=8,
            child=[
                widgets.Label(
                    label="",
                    css_classes=["system-icon"],
                ),
                widgets.Label(
                    label=self._get_stats_label(),
                    css_classes=["system-label"],
                    setup=lambda label: utils.Poll(2000, lambda _: label.set_label(self._get_stats_label())),
                ),
            ],
        )

    def _get_cpu_usage(self) -> float:
        """Calculate CPU usage percentage."""
        try:
            with open("/proc/stat", "r") as f:
                line = f.readline()
                values = [float(x) for x in line.split()[1:]]
                total = sum(values)
                idle = values[3]

                total_diff = total - self._prev_total
                idle_diff = idle - self._prev_idle

                self._prev_total = total
                self._prev_idle = idle

                if total_diff == 0:
                    return 0.0

                usage = (1 - idle_diff / total_diff) * 100
                return round(usage, 1)
        except:
            return 0.0

    def _get_stats_label(self) -> str:
        """Get formatted stats string."""
        cpu = self._get_cpu_usage()
        mem_info = fetch.mem_info

        # Calculate used memory: Total - Available (most accurate method)
        mem_used = mem_info["MemTotal"] - mem_info["MemAvailable"]
        mem_used_gb = mem_used / (1024 * 1024)  # Convert KB to GB
        mem_total_gb = mem_info["MemTotal"] / (1024 * 1024)  # Convert KB to GB
        mem_percent = (mem_used / mem_info["MemTotal"]) * 100

        return f"CPU {cpu:.0f}% | RAM {mem_used_gb:.1f}/{mem_total_gb:.1f}GB {int(mem_percent)}%"
