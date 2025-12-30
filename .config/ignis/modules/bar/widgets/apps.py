from ignis import widgets
from ignis.services.applications import ApplicationsService

applications = ApplicationsService.get_default()

# for i in applications.apps:
    # print(i.icon)


class AppItem(widgets.Button):
    def __init__(self, app):
        print(app.icon)
        super().__init__(
            child=widgets.Box(
                child=[widgets.Icon(image=app.icon, pixel_size=32)]
            )
        )


def get_apps(app):
    print("Hello :D", app.icon)
    return []


class Apps(widgets.Box):
    def __init__(self):
        super().__init__(
            child=applications.bind(
                "pinned",
                transform=lambda apps: [AppItem(app) for app in apps]
                # + [
                #     widgets.Button(
                #             child=widgets.Icon(image="start-here-symbolic", pixel_size=16),
                #             css_classes=["pinned-app", "unset"]
                #         )
                #     ]
            )
        )

