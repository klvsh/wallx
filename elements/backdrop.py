import random

from colors.gradient import generate_gradient


def draw_backdrop(img_width, img_height, configuration):
    backdrop = random.choice(configuration.theme.possible_backdrops)
    return generate_gradient(
        img_width,
        img_height,
        backdrop.start_rgba,
        backdrop.stop_rgba,
        is_horizontal=False
    )
