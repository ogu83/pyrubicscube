from Colors3D import *
from Point3D import Point3D

import pygame

class Line3D:    
    def __init__(self, p1=Point3D(), p2=Point3D(), color = WHITE, thickness = 1):
        self.p1 = p1
        self.p2 = p2
        self.color = color
        self.thickness = thickness

    def rotateX(self, angle):
        self.p1 = self.p1.rotateX(angle)
        self.p2 = self.p2.rotateX(angle)
        return self

    def rotateY(self, angle):
        self.p1 = self.p1.rotateY(angle)
        self.p2 = self.p2.rotateY(angle)
        return self
    
    def rotateZ(self, angle):
        self.p1 = self.p1.rotateZ(angle)
        self.p2 = self.p2.rotateZ(angle)
        return self

    def project(self, win_width, win_height, fov, viewer_distance):
        return (self.p1.project(win_width,win_height,fov,viewer_distance), 
                self.p2.project(win_width,win_height,fov,viewer_distance))

    def draw(self, screen, fov, viewer_distance):
        p_p1, p_p2 = self.project(screen.get_width(), screen.get_height(), fov, viewer_distance)
        pygame.draw.line(screen, self.color, (p_p1.x, p_p1.y), (p_p2.x, p_p2.y), self.thickness)