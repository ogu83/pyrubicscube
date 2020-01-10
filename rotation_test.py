import pygame
from Paint import *
from Physical import *

X, Y, Z = 0, 1, 2


def main():
    from pygame import K_q, K_w, K_a, K_s, K_z, K_x

    cube = Physical(  # 0         1            2            3           4            5            6            7
        vertices=((1, 1, 1), (1, 1, -1), (1, -1, 1), (1, -1, -1), (-1, 1, 1), (-1, 1, -1), (-1, -1, 1), (-1, -1, -1)),
        edges=({0, 1}, {0, 2}, {2, 3}, {1, 3},
               {4, 5}, {4, 6}, {6, 7}, {5, 7},
               {0, 4}, {1, 5}, {2, 6}, {3, 7})
    )

    counter_clockwise = 0.05  # radians
    clockwise = -counter_clockwise

    params = {
        K_q: (X, clockwise),
        K_w: (X, counter_clockwise),
        K_a: (Y, clockwise),
        K_s: (Y, counter_clockwise),
        K_z: (Z, clockwise),
        K_x: (Z, counter_clockwise),
    }

    def keys_handler(keys):
        for key in params:
            if keys[key]:
                cube.rotate(*params[key])

    pygame.init()
    pygame.display.set_caption('Control -   q,w : X    a,s : Y    z,x : Z')
    Paint(cube, keys_handler)

if __name__ == '__main__':
    main()