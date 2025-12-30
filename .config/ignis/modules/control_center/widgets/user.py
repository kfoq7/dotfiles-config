import os
from ignis import utils, widgets
from ignis.services.fetch import FetchService

fetch = FetchService.get_default()

def format_uptime(value: tuple[int, int, int, int]) -> str:
    days, hours, minutes, _ = value
    if days:
        return f"up {days:02}:{hours:02}:{minutes:02}"

    return f"up {hours:02}:{minutes:02}"


class User(widgets.Box):
    def __init__(self):
        user_image = widgets.Picture(
            image="https://avatars.githubusercontent.com/u/83372435?v=4",
            width=44,
            height=44,
            content_fit="cover",
            style="border-radius: 10rem;"
        )

        username = widgets.Box(
            child=[
                widgets.Label(
                    label=os.getenv("USER"),
                    css_classes=["user-name"],
                    halign="start"
                ),
                widgets.Label(
                    halign="start",
                    css_classes=["user-name-secondarg"],
                    label=utils.Poll(
                        timeout=60 * 100,
                        callback=lambda _: fetch.uptime
                    ).bind(
                        "output",
                        lambda value: format_uptime(value)
                    )
                )
            ]
        )

        super().__init__(
            child=[
                user_image,
                username
            ],
            css_classes=["user"]
        )
