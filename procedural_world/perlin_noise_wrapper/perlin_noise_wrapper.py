from perlin_noise import PerlinNoise

from procedural_world.config import (
    PERLIN_NOISE_AMPLITUDE,
    PERLIN_NOISE_FREQUENCY,
    PERLIN_NOISE_OCTAVES,
    PERLIN_NOISE_SEED,
)


class PerlinNoiseWrapper:
    def __init__(self):
        self.perlin_noise = PerlinNoise(
            octaves=PERLIN_NOISE_OCTAVES,
            seed=PERLIN_NOISE_SEED,
        )

    def get_height(
        self,
        x: int,
        z: int,
    ) -> int:
        return self.perlin_noise(
            [x / PERLIN_NOISE_FREQUENCY, z / PERLIN_NOISE_FREQUENCY]
        ) * PERLIN_NOISE_AMPLITUDE
