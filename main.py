import math

from ursina import (
    color,
    lerp,
    Sky,
    time,
    Ursina,
    Vec2,
    window,
)
from ursina.prefabs.first_person_controller import FirstPersonController

from procedural_world.config import (
    FULLSCREEN,
    GENERATE_TERRAIN_FREQUENCY,
    GRAVITATIONAL_ACCELERATION,
    HEIGHT,
    IS_EXIT_BUTTON_ENABLED,
    IS_SUBJECT_CURSOR_VISIBLE,
    LERP_FACTOR,
    SKY_COLOR_RGB,
    STEP_SIZE,
    SUBJECT_GRAVITY,
    TERRAIN_MARGIN_SIZE,
)
from procedural_world.mesh_terrain import MeshTerrain


def input(key: str):
    if key == 'escape':
        exit()


def update():
    global count, previous_position
    count += 1
    if count == GENERATE_TERRAIN_FREQUENCY:
        terrain.generate_terrain()
        count = 0

    if abs(subject.x - previous_position.x) > TERRAIN_MARGIN_SIZE or \
        abs(subject.z - previous_position.y) > TERRAIN_MARGIN_SIZE:
            previous_position = Vec2(subject.x, subject.z)
            terrain.swirl_engine.reset(previous_position)

    is_block_found = False

    step = STEP_SIZE
    height = HEIGHT
    step_x = math.floor(subject.x + 0.5)
    step_y = math.floor(subject.y + 0.5)
    step_z = math.floor(subject.z + 0.5)

    for i in range(-step, step):
        step_coordinates = f'x{step_x}y{step_y + i}z{step_z}'
        if terrain.terrain_coordinates.get(step_coordinates) == 't':
            target = step_y + i + height
            is_block_found = True
            break

    if is_block_found:
        subject.y = lerp(subject.y, target, LERP_FACTOR * time.dt)
    else:
        subject.y -= GRAVITATIONAL_ACCELERATION * time.dt


def main():
    global subject, terrain, count, previous_position

    count = 0
    previous_position = Vec2(0,0)

    app = Ursina()

    window.color = color.rgb(*SKY_COLOR_RGB)

    sky = Sky()
    sky.color = window.color

    subject = FirstPersonController()
    subject.gravity = SUBJECT_GRAVITY
    subject.cursor.visible = IS_SUBJECT_CURSOR_VISIBLE

    terrain = MeshTerrain()
    terrain.generate_terrain()

    window.fullscreen = FULLSCREEN
    window.exit_button.enabled = IS_EXIT_BUTTON_ENABLED

    app.run()


if __name__ == '__main__':
    main()
