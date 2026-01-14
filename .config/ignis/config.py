import os

from ignis import utils
from ignis.app import IgnisApp
from ignis.services.wallpaper import WallpaperService
from ignis.options import options
from ignis.css_manager import CssInfoPath, CssManager

from modules import Bar, ControCenter, NotificationPopup
from user_options import user_options

app = IgnisApp.get_initialized()
css_manager = CssManager.get_default()

WallpaperService.get_default()


def format_scss_var(name: str, val: str) -> str:
    return f"${name}: {val};\n"


def patch_style_scss(path: str) -> str:
    with open(path) as file:
        contents = file.read()

    scss_colors = ""

    for key, value in user_options.material.colors.items():
        scss_colors += format_scss_var(key, value)

    string = (
        format_scss_var("darkmode", str(user_options.material.dark_mode).lower())
        + scss_colors
        + contents
    )

    return utils.sass_compile(
        string=string,
        extra_args=["--load-path", utils.get_current_dir()]
    )

css_manager.apply_css(
    CssInfoPath(
        name="main",
        compiler_function=patch_style_scss,
        path=os.path.join(utils.get_current_dir(), "styles.scss"),
    )
)

options.wallpaper.set_wallpaper_path(os.path.expanduser('~/Pictures/anime-girl-wink-katana-4k-wallpaper.jpg'))


NotificationPopup(0)
Bar()


ControCenter()
