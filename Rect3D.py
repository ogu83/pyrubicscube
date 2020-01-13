from Colors3D import *
from Point3D import Point3D
from Line3D import Line3D

class Rect3D:
    p1 = Point3D()
    p2 = Point3D()
    p3 = Point3D()
    p4 = Point3D()

    l1 = Line3D()
    l2 = Line3D()
    l3 = Line3D()
    l4 = Line3D()

    def __init__(self, p1, p2, p3, p4, color = WHITE, thickness = 1):
        self.p1 = p1
        self.p2 = p2
        self.p1 = p3
        self.p2 = p4
        self.color = color
        self.thickness = thickness
