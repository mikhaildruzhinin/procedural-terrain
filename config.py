from typing import (
    Dict,
    Tuple,
)

# update
GENERATE_TERRAIN_FREQUENCY: int = 2
TERRAIN_MARGIN_SIZE: int = 4
STEP_SIZE: int = 2
HEIGHT: float = 1.86
GRAVITATIONAL_ACCELERATION: float = 9.8

# main
SKY_COLOR_RGB: Tuple[int] = (0, 200, 255)
SUBJECT_GRAVITY: float = 0.0

# MeshTerrain
BLOCK_MODEL: str = 'block.obj'
TEXTURE_ATLAS: str = 'texture_atlas.png'
NUMBER_CHUNKS: int = 256
CHUNK_WIDTH: int = 10 # must be an even number
TEXTURE_SCALE: int = 64
TINT_OFFSET: float = 0.5
TEXTURE_ATLAS_COORDINATES: Dict[str, Tuple[int]] = {
    'grass' : (8, 7),
    'snow': (8, 6),
}

#PerlinNoiseWrapper
PERLIN_NOISE_SEED: int = 123
PERLIN_NOISE_OCTAVES: int = 4
PERLIN_NOISE_FREQUENCY: int = 256
PERLIN_NOISE_AMPLITUDE: int = 24
