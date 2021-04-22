#
# References:
#   - https://note.nkmk.me/en/python-numpy-generate-gradation-image/
#

import random
import numpy as np

from PIL import Image

from elements.moon import draw_moon
from elements.stars import draw_stars
from elements.terrain import draw_terrain
from elements.backdrop import draw_backdrop

from configuration import ConfigurationGenerator


img_width = 1280
img_height = 720


def generate_image():
    assert img_width >= img_height >= 360
    generator = ConfigurationGenerator()
    configuration = generator.generate(theme="Pitch Black")

    img_data = draw_backdrop(img_width, img_height, configuration)

    img_data = draw_stars(img_data)

    total_terrains = random.randint(1, configuration.theme.max_terrains)
    terrains = random.sample(
        configuration.theme.possible_terrains,
        total_terrains)

    max_terrain_height = int((0.4 + random.random() * 0.2) * img_height)
    elevation = int(random.random() * 0.2 * img_height)
    shift = 0
    for terrain in terrains:
        img_data = draw_terrain(
            img_data, terrain, terrain_height=max_terrain_height, elevation=elevation, shift=shift)
        max_terrain_height = int(
            (0.5 + random.random() * 0.2) * max_terrain_height)
        shift = shift * -1 if shift else random.choice([-1, 1])
        elevation = (0.1 + random.random() * 0.5) * elevation

    img_data = draw_moon(img_data)

    img = Image.fromarray(np.uint8(img_data))
    img.save('wallpaper.png')


generate_image()
