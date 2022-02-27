from ursina import (
    color,
    Ursina,
    window,
)
from ursina.prefabs.first_person_controller import FirstPersonController

from mesh_terrain import MeshTerrain


def update():
    pass


def input(key):
    if key == 'escape':
        exit()


def main():
    app = Ursina()

    window.color = color.rgb(200,0,255)
    subject = FirstPersonController()
    subject.gravity = 0.0
    terrain = MeshTerrain()
    terrain.generate_terrain()

    app.run()


if __name__ == '__main__':
    main()
