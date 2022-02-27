import math

from ursina import (
    color,
    lerp,
    Sky,
    time,
    Ursina,
    window,
)
from ursina.prefabs.first_person_controller import FirstPersonController

from mesh_terrain import MeshTerrain


def input(key):
    if key == 'escape':
        exit()


def update():
    is_block_found = False

    step = 2
    height = 1.86
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
        subject.y = lerp(subject.y, target, 6 * time.dt)
    else:
        subject.y -= 9.8 * time.dt


def main():
    global subject, terrain

    app = Ursina()

    window.color = color.rgb(0,200,255)
    sky = Sky()
    sky.color = window.color

    subject = FirstPersonController()
    subject.gravity = 0.0

    terrain = MeshTerrain()
    terrain.generate_terrain()

    app.run()


if __name__ == '__main__':
    main()
