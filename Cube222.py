from OpenGL_Geometry import *

class Cube1(Cube3D):
    def __init__(self, size):
        Cube3D.__init__(self, size, YELLOW, BLACK, BLUE, BLACK, ORANGE, BLACK)
        self.translate_size([-1,1,1], True)

class Cube2(Cube3D):
    def __init__(self, size):
        Cube3D.__init__(self, size, YELLOW, BLACK, BLUE, BLACK, BLACK, RED)
        self.translate_size([1,1,1], True)

class Cube3(Cube3D):
    def __init__(self, size):
        Cube3D.__init__(self, size, YELLOW, BLACK, BLACK, GREEN, ORANGE, BLACK)
        self.translate_size([-1,1,-1], True)

class Cube4(Cube3D):
    def __init__(self, size):
        Cube3D.__init__(self, size, YELLOW, BLACK, BLACK, GREEN, BLACK, RED)
        self.translate_size([1,1,-1], True)

class Cube5(Cube3D):
    def __init__(self, size):
        Cube3D.__init__(self, size, BLACK, WHITE, BLUE, BLACK, ORANGE, BLACK)
        self.translate_size([-1,-1,1], True)

class Cube6(Cube3D):
    def __init__(self, size):
        Cube3D.__init__(self, size, BLACK, WHITE, BLUE, BLACK, BLACK, RED)
        self.translate_size([1,-1,1], True)

class Cube7(Cube3D):
    def __init__(self, size):
        Cube3D.__init__(self, size, BLACK, WHITE, BLACK, GREEN, ORANGE, BLACK)
        self.translate_size([-1,-1,-1], True)

class Cube8(Cube3D):    
    def __init__(self, size):
        Cube3D.__init__(self, size, BLACK, WHITE, BLACK, GREEN, BLACK, RED)
        self.translate_size([1,-1,-1], True)


class Cube222:    
    def __init__(self, size=4):
        self.Cube1 = Cube1(size/2)
        self.Cube2 = Cube2(size/2)
        self.Cube3 = Cube3(size/2)
        self.Cube4 = Cube4(size/2)
        self.Cube5 = Cube5(size/2)
        self.Cube6 = Cube6(size/2)
        self.Cube7 = Cube7(size/2)
        self.Cube8 = Cube8(size/2)

    def cube_array(self):
        return [
            self.Cube1,
            self.Cube2,
            self.Cube3,
            self.Cube4,
            self.Cube5,
            self.Cube6,
            self.Cube7,
            self.Cube8,
        ]

    def draw(self):
        for cube in self.cube_array():
            cube.draw()

    def animated_rotateY(self,angle,use_self_center):
        pass
    def animated_rotateX(self,angle,use_self_center):
        pass
