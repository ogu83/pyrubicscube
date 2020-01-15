import numpy as np
import math, pygame, random

from OpenGL_Colors import *
from OpenGL.GL import *
from OpenGL.GLU import *

class Cube3D:
    angle_x = [0,0]
    angle_y = [0,0]
    angle_z = [0,0]

    verticies=[
    [1.0, -1.0, -1.0],
    [1.0, 1.0, -1.0],
    [-1.0, 1.0, -1.0],
    [-1.0, -1.0, -1.0],
    [1.0, -1.0, 1.0],
    [1.0, 1.0, 1.0],
    [-1.0, -1.0, 1.0],
    [-1.0, 1.0, 1.0],
    ]
    
    edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7),
    )
       
    surfaces = (
        (0,1,2,3),
        (3,2,7,6),
        (6,7,5,4),
        (4,5,1,0),
        (1,5,7,2),
        (4,0,3,6),
    )

    def __init__(self, size, color_u=YELLOW, color_d=WHITE, color_f=BLUE, color_b=GREEN, color_l=ORANGE, color_r=RED):
        self.size = float(size)        
        self.verticies = np.array(self.verticies) * size
        self.color_u = color_u
        self.color_d = color_d
        self.color_f = color_f
        self.color_b = color_b
        self.color_l = color_l
        self.color_r = color_r
        
    def draw(self):
        self.do_animations()
        
        # glBegin(GL_QUADS)
        # glColor3fv(self.color)
        # for surface in self.surfaces:
            # for vertex in surface:
                # glVertex3fv(self.verticies[vertex])
        # glEnd()
    
        glBegin(GL_LINES)                
        for edge in self.edges:
            for vertex in edge:
                glColor3fv(WHITE)
                glVertex3fv(self.verticies[vertex])        
        glEnd()


    def assing_vertex(self, vertex, v):
        for i in range(len(vertex)):
            vertex[i] = v[i]    

    def assing_rotate_all_vertex(self,rotation_matrix):
        for vertex in self.verticies:
            v = rotation_matrix.dot(vertex)
            self.assing_vertex(vertex,v)
        
    def rotateX(self, angle):
        rad = angle * math.pi / 180
        cosa = (math.cos(rad))
        sina = (math.sin(rad))        
        rotation_matrix = np.array([[1.0, 0.0, 0.0],
                                    [0.0, cosa, -sina],
                                    [0.0, sina, cosa]])
        self.assing_rotate_all_vertex(rotation_matrix)        
        
    def rotateY(self, angle):
        rad = angle * math.pi / 180
        cosa = (math.cos(rad))
        sina = (math.sin(rad))        
        rotation_matrix = np.array([[cosa, 0.0, sina],
                                    [0.0, 1.0, 0.0],
                                    [-sina, 0.0, cosa]])
        self.assing_rotate_all_vertex(rotation_matrix)
        
    def rotateZ(self, angle):
        rad = angle * math.pi / 180
        cosa = (math.cos(rad))
        sina = (math.sin(rad))        
        rotation_matrix = np.array([[cosa, -sina, 0.0],
                                    [sina, cosa, 0.0],
                                    [0.0, 0.0, 1.0]])
        self.assing_rotate_all_vertex(rotation_matrix)
        
    def do_animations(self):
        if (self.angle_x[0] < self.angle_x[1]):
            self.angle_x[0] += 1
            self.rotateX(1)
        elif (self.angle_x[0] > self.angle_x[1]):
            self.angle_x[0] -= 1
            self.rotateX(-1)
            
        if (self.angle_y[0] < self.angle_y[1]):
            self.angle_y[0] += 1
            self.rotateY(1)
        elif (self.angle_y[0] > self.angle_y[1]):
            self.angle_y[0] -= 1
            self.rotateY(-1)
            
        if (self.angle_z[0] < self.angle_z[1]):
            self.angle_y[0] += 1
            self.rotateY(1)
        elif (self.angle_z[0] > self.angle_z[1]):
            self.angle_z[0] -= 1
            self.rotateZ(-1)
            
    def is_on_animation(self):
        return (self.angle_x[0] == self.angle_x[1] and self.angle_y[0] == self.angle_y[1] and self.angle_z[0] == self.angle_z[1]) == False
        
    def animated_rotateX(self,angle):
        if (not self.is_on_animation()):
            self.angle_x[1]+=angle
        
    def animated_rotateY(self,angle):
        if (not self.is_on_animation()):
            self.angle_y[1]+=angle
        
    def animated_rotateZ(self,angle):        
        if (not self.is_on_animation()):
            self.angle_z[1]+=angle