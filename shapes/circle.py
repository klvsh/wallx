def draw_circle(x, y, r, color, draw):
    """Function to draw a circle at given center with given
    radius and colour
    """
    x, y, r = int(x), int(y), int(r)  # Converting possible floats to int
    draw.ellipse([x - r, y - r, x + r, y + r], fill=color)
