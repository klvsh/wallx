from elements.gradient import generate_gradient


def draw_backdrop(img_width, img_height, configuration):
    return generate_gradient(
        img_width,
        img_height,
        configuration.backdrop.start_rgba,
        configuration.backdrop.stop_rgba,
        is_horizontal=False
    )
