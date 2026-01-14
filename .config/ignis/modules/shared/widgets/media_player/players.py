import os

import ignis
from ignis import  widgets, utils
from ignis.css_manager import CssManager, CssInfoString
from ignis.services.mpris import MprisPlayer

from jinja2 import Template

from services.material import MaterialService

material = MaterialService.get_default()
css_manager = CssManager.get_default()

MEDIA_TEMPLATE = utils.get_current_dir() + "/media.scss"
MEDIA_SCSS_CACHE_DIR = ignis.CACHE_DIR + '/media'
MEDIA_ART_FALLBACK = utils.get_current_dir() + '/../../../../misc/media-art-fallback.png'

os.makedirs(MEDIA_SCSS_CACHE_DIR, exist_ok=True)


class PlayerBar(widgets.Box):
    def __init__(self, player: MprisPlayer) -> None:
        self._player = player
        self._colors_path = f"{MEDIA_SCSS_CACHE_DIR}/{self.clean_desktop_entry()}.scss"

        self._player.connect("closed", lambda x: self.destroy())
        self._player.connect("notify::art-url", lambda x, y: self.load_colors())
        self.load_colors()

        super().__init__(
            css_classes=["player-bar", self.get_css("media-image-gradient")],
            child=[
                widgets.Label(
                    label=self._player.bind(
                        "title",
                        transform=lambda title: f"󰓇 {title}",
                    ),
                    justify="left",
                    ellipsize="end",
                    max_width_chars=12,
                ),
            ]
        )

    def destroy(self) -> None:
        super().unparent()
        # utils.Timeout(self.transition_duration, super().unparent)

    def load_colors(self) -> None:
        art_url = self._player.art_url if self._player.art_url else MEDIA_ART_FALLBACK

        colors = material.get_colors_from_img(art_url)
        colors["art_url"] = art_url
        colors["desktop_entry"] = self.clean_desktop_entry()

        with open(MEDIA_TEMPLATE) as file:
            template_rendered = Template(file.read()).render(colors)

        if self._player.desktop_entry in css_manager.list_css_info_names():
            css_manager.remove_css(self._player.desktop_entry)

        css_manager.apply_css(
            CssInfoString(
                name=self._player.desktop_entry,
                compiler_function=lambda x: utils.sass_compile(string=x),
                string=template_rendered,
            )
        )

    def get_css(self, class_name: str) -> str:
        return f"{class_name}-{self.clean_desktop_entry()}"

    def clean_desktop_entry(self) -> str:
        return self._player.desktop_entry.replace(".", "-")
