from Colors3D import *
from Point3D import Point3D
from Line3D import Line3D

class Rect3D:    
    l1 = Line3D()
    l2 = Line3D()
    l3 = Line3D()
    l4 = Line3D()

    def __init__(self, p1, p2, p3, p4, color = WHITE, thickness = 1):
        self.color = color
        self.thickness = thickness    

        self.l1 = Line3D(p1, p2, self.color, self.thickness)
        self.l2 = Line3D(p2, p3, self.color, self.thickness)
        self.l3 = Line3D(p3, p4, self.color, self.thickness)
        self.l4 = Line3D(p4, p1, self.color, self.thickness)        

    def rotateX(self, angle):        
        self.l1 = self.l1.rotateX(angle)
        self.l2 = self.l2.rotateX(angle)
        self.l3 = self.l3.rotateX(angle)
        self.l4 = self.l4.rotateX(angle)
        return self

    def rotateY(self, angle):
        self.l1 = self.l1.rotateY(angle)
        self.l2 = self.l2.rotateY(angle)
        self.l3 = self.l3.rotateY(angle)
        self.l4 = self.l4.rotateY(angle)        
        return self
    
    def rotateZ(self, angle):
        self.l1 = self.l1.rotateZ(angle)
        self.l2 = self.l2.rotateZ(angle)
        self.l3 = self.l3.rotateZ(angle)
        self.l4 = self.l4.rotateZ(angle)        
        return self
