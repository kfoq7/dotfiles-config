import asyncio
from typing import Literal

from ignis import widgets, utils
from ignis.services.audio import AudioService, Stream

from ..menu import Menu

audio = AudioService.get_default()

AUDIO_TYPES = {
    "speaker":{
        "menu_icon": "audio-headphones-symbolic",
        "menu_label": "Sound output",
    },
    "microphone": {
        "menu_icon": "microphone-sensitivity-high-symbolic",
        "menu_label": "Sound input",
    }
}


class DeviceItem(widgets.Button):
    def __init__(
        self,
        stream: Stream,
        _type: Literal["speaker", "microphone"]
    ) -> None:
        super().__init__(
            css_classes=["volume-entry", "unset"],
            hexpand=True,
            setup=lambda self: stream.connect(
                "removed",
                lambda x: self.unparent()
            ),
            on_click=lambda x: setattr(audio, _type, stream),
            child=widgets.Box(
                child=[
                    widgets.Icon(image="audio-card-symbolic"),
                    widgets.Label(
                        label=stream.description,
                        ellipze="end",
                        max_width_chars=30,
                        halign="start",
                    ),
                    widgets.Icon(
                        image="object-select-symbolic",
                        halign="end",
                        hexpand=True,
                        visible=stream.bind("is_default")
                    )

                ]
            ),
        )


class DeviceMenu(Menu):
    def __init__(
        self,
        _type: Literal["speaker", "microphone"],
    ) -> None:
        data = AUDIO_TYPES[_type]

        super().__init__(
            name=f"volume-{_type}",
            child=[
                widgets.Box(
                    css_classes=["volume-entry-list-header-box"],
                    child=[
                        widgets.Icon(
                            image=data["menu_icon"],
                            pixel_size=24
                        ),
                        widgets.Label(
                            label=data["menu_label"],
                            halign="start",
                            css_classes=["volume-entry-list-header-label"],
                        ),
                    ],
                ),
                widgets.Box(
                    vertical=True,
                    setup=lambda self: audio.connect(
                        f"{_type}-added",
                        lambda x, stream: self.append(DeviceItem(stream, _type))
                    ),
                ),
                widgets.Separator(css_classes=["volume-entry-list-separator"]),
                widgets.Button(
                    child=widgets.Box(
                        css_classes=["volume-entry", "unset"],
                        style="margin-bottom: 0;",
                        on_click=lambda x: asyncio.create_task(
                            utils.exec_sh_async("pavucontrol"),
                        ),
                        child=[
                            widgets.Icon(image='preferences-system-symbolic'),
                            widgets.Label(
                                label="Sound settings",
                                halign="start",
                                css_classes=["volume-entry-label"],
                            )
                        ],
                    ),
                ),
            ],
        )

        self.box.add_css_class(f"volume-menubox-{_type}")


class VolumeSlider(widgets.Box):
    def __init__(
        self,
        _type: Literal["speaker", "microphone"],
    ):
        stream = getattr(audio, _type)

        icon = widgets.Button(
            css_classes=["material-slider-icon", "unset", "hover"],
            on_click=lambda x: stream.set_is_muted(not stream.is_muted),
            child=widgets.Icon(
                image=stream.bind("icon_name"),
                pixel_size=18,
            ),
        )

        device_menu = DeviceMenu(_type=_type)

        # scale = MaterialVolumeSlider(
        #     stream=stream
        # )

