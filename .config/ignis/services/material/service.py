from ignis.base_service import BaseService

from PIL import Image
from materialyoucolor.quantize import QuantizeCelebi
from materialyoucolor.hct import Hct
from materialyoucolor.scheme.scheme_tonal_spot import SchemeTonalSpot
from materialyoucolor.dynamiccolor.material_dynamic_colors import MaterialDynamicColors
from materialyoucolor.score.score import Score

from .utils import rgba_to_hex, calculate_optimal_size


class MaterialService(BaseService):
    def __init__(self):
        super().__init__()

    def get_colors_from_img(self, path: str) -> dict[str, str]:
        image = Image.open(path)
        w_size, h_size =  image.size

        w_size_new, h_size_new = calculate_optimal_size(w_size, h_size, 128)

        if w_size_new < w_size or h_size_new < h_size:
            image = image.resize((w_size_new, h_size_new),  Image.Resampling.BICUBIC)

        pixel_len = image.width * image.height
        image_data = image.get_flattened_data()
        pixel_array = [image_data[_] for _ in range(0, pixel_len, 1)]

        colors = QuantizeCelebi(pixel_array, 128)
        argb = Score.score(colors)[0]

        hct = Hct.from_int(argb)
        scheme = SchemeTonalSpot(hct, True, 0.0)

        material_colors = {}

        for color in vars(MaterialDynamicColors).keys():
            color_name = getattr(MaterialDynamicColors, color)

            if hasattr(color_name, "get_hct"):
                rgba = color_name.get_hct(scheme).to_rgba()
                material_colors[color] = rgba_to_hex(rgba)

        return material_colors

    def generate_colors(self, path: str) -> None:
        colors = self.get_colors_from_img(path) # Dark mode is set it by default
        # dark_colors = self.get_colors_from_img()
