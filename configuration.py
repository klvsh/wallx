import random

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

class ImageConfiguration:
    def __init__(self, phase="day", stars=False):
        self.phase = phase
        self.stars = stars


class ConfigurationGenerator:
    def __init__(self):
        pass

    def generate(self, seed):
        print("seed", random.seed(seed))
        phase = random.choice(POSSIBLE_PHASES)

        stars = random.choice(POSSIBLE_STARS) \
                    if phase == POSSIBLE_PHASES_NIGHT \
                        else POSSIBLE_STARS_NO_STARS

        params = {
            "phase": phase,
            "stars": stars,
        }

        return ImageConfiguration(**params)
