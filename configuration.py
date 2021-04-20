import random

class Backdrop:
    def __init__(self, start_rgba, stop_rgba):
        self.start_rgba = start_rgba
        self.stop_rgba = stop_rgba


POSSIBLE_PHASES_DAY = "day"
POSSIBLE_PHASES_NIGHT = "night"

POSSIBLE_PHASES = [
    POSSIBLE_PHASES_DAY,
    POSSIBLE_PHASES_NIGHT
]

POSSIBLE_STARS_NO_STARS = "no"
POSSIBLE_STARS_DENSE = "dense"
POSSIBLE_STARS_SPARSE = "sparse"

POSSIBLE_STARS = [
    POSSIBLE_STARS_NO_STARS,
    POSSIBLE_STARS_DENSE,
    POSSIBLE_STARS_SPARSE,
]

POSSIBLE_BACKDROP_DAY_1 = Backdrop((56, 182, 255, 255), (255, 255, 255, 255))
POSSIBLE_BACKDROP_DAY = [
    POSSIBLE_BACKDROP_DAY_1,
]

POSSIBLE_BACKDROP_NIGHT_1 = Backdrop((0, 0, 0, 255), (70, 70, 70, 255))
POSSIBLE_BACKDROP_NIGHT = [
    POSSIBLE_BACKDROP_NIGHT_1,
]


POSSIBLE_TERRAINS_DAY_1 = Backdrop((165, 92, 27, 255), (0, 0, 0, 255))
POSSIBLE_TERRAINS_DAY = [
    POSSIBLE_TERRAINS_DAY_1,
]

POSSIBLE_TERRAINS_NIGHT_1 = Backdrop((165, 92, 27, 255), (0, 0, 0, 255))
POSSIBLE_TERRAINS_NIGHT = [
    POSSIBLE_TERRAINS_NIGHT_1,
]

class ImageConfiguration:
    def __init__(self, phase="day", stars=False, backdrop=None, terrain_shade=None):
        self.phase = phase
        self.stars = stars
        self.backdrop = backdrop
        self.terrain_shade = terrain_shade

class ConfigurationGenerator:
    def __init__(self):
        pass

    def generate(self, seed):
        print("seed", seed)
        random.seed(seed)
        phase = random.choice(POSSIBLE_PHASES)

        stars = random.choice(POSSIBLE_STARS) \
                    if phase == POSSIBLE_PHASES_NIGHT \
                        else POSSIBLE_STARS_NO_STARS
        
        if phase == POSSIBLE_PHASES_NIGHT:
            backdrop = random.choice(POSSIBLE_BACKDROP_NIGHT)
            terrain_shade = random.choice(POSSIBLE_TERRAINS_NIGHT)
        elif phase == POSSIBLE_PHASES_DAY:
            backdrop = random.choice(POSSIBLE_BACKDROP_DAY)
            terrain_shade = random.choice(POSSIBLE_TERRAINS_DAY)
        else:
            backdrop = random.choice(POSSIBLE_BACKDROP_NIGHT)
            terrain_shade = random.choice(POSSIBLE_TERRAINS_DAY)

        params = {
            "phase": phase,
            "stars": stars,
            "backdrop": backdrop,
            "terrain_shade": terrain_shade,
        }

        return ImageConfiguration(**params)
