from Colors3D import *
from Point3D import Point3D
from Line3D import Line3D

import pygame

class Rect3D:    
    
    def __init__(self, p1=Point3D(), p2=Point3D(), p3=Point3D(), p4=Point3D(), stroke_color = WHITE, fill_color = WHITE, thickness = 1):
        self.stroke_color = stroke_color
        self.fill_color = fill_color
        self.thickness = thickness    

        self.l1 = Line3D(p1, p2, self.stroke_color, self.thickness)
        self.l2 = Line3D(p2, p3, self.stroke_color, self.thickness)
        self.l3 = Line3D(p3, p4, self.stroke_color, self.thickness)
        self.l4 = Line3D(p4, p1, self.stroke_color, self.thickness)        

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

    def project(self, win_width, win_height, fov, viewer_distance):
        return (self.l1.p1.project(win_width, win_height, fov, viewer_distance), 
                self.l1.p2.project(win_width, win_height, fov, viewer_distance),
                self.l3.p1.project(win_width, win_height, fov, viewer_distance)                
                )

    def draw(self, screen, fov, viewer_distance):
        #p_l1, p_l2, p_l3, p_l4 = self.project(screen.get_width(), screen.get_height(), fov, viewer_distance)
        
        #DRAW RECTANGLE LINES
        self.l1.draw(screen, fov, viewer_distance)
        self.l2.draw(screen, fov, viewer_distance)
        self.l3.draw(screen, fov, viewer_distance)
        self.l4.draw(screen, fov, viewer_distance)

        #DRAW RECTANGLE FILL
        p_p1, p_p2, p_p3 = self.l1.p1, self.l1.p2, self.l2.p2
        fill_line = Line3D(p_p1, p_p2, self.fill_color, 15)
        fill_line.draw(screen, fov, viewer_distance)
        #p_p1 = self.l1.p1
        #p_p2 = self.l1.p2
        #p_p3 = self.l3.p1
        #rect_width = p_p2.x - p_p1.x
        #rect_height = p_p3.y - p_p2.y
        #rect = (p_p1.x, p_p1.y, rect_width, rect_height)
        #pygame.draw.rect(screen, self.fill_color, rect, self.thickness)