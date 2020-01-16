import numpy as np
import math, pygame, random

from OpenGL_Colors import *
from OpenGL.GL import *
from OpenGL.GLU import *

class Grid3D:
    def __init__(self, size = 1, depth_x = 50, depth_y = 50, color = GRAY):
        self.size = size
        self.color = color    
        self.depth_x = depth_x
        self.depth_y = depth_y
        
    def draw(self):
        glBegin(GL_LINES)                
        glColor3fv(self.color)
        size = self.size
        tran_matrix = np.array([self.depth_x/2 + size, 0, self.depth_y/2 + size])
        for x in range(0, self.depth_x, self.size):
            for y in range(0, self.depth_y, self.size):
                v0 = np.array([x, 0, y])
                v1 = np.array([x+self.size, 0, y])
                v2 = np.array([x, 0, y+self.size])
                glVertex3fv(v0 - tran_matrix)
                glVertex3fv(v1 - tran_matrix)                
                glVertex3fv(v0 - tran_matrix)
                glVertex3fv(v2 - tran_matrix)
        glEnd()
        
class Cube3D:
    angle_x = [0, 0]
    angle_y = [0, 0]
    angle_z = [0, 0]

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

    def __init__(self, size = 1, color_u=YELLOW, color_d=WHITE, color_f=BLUE, color_b=GREEN, color_l=ORANGE, color_r=RED):
        self.size = float(size)        
        self.verticies = np.array(self.verticies) * size
        self.color_d = color_d #WHITE
        self.color_u = color_u #YELLOW
        self.color_b = color_b #GREEN                
        self.color_f = color_f #BLUE                        
        self.color_l = color_l #ORANGE
        self.color_r = color_r #RED
        
    def getColorArray(self):
        return [            
            self.color_b, #GREEN
            self.color_l, #ORANGE             
            self.color_f, #BLUE 
            self.color_r, #RED                                              
            self.color_u, #YELLOW
            self.color_d, #WHITE            
        ]
        
    def draw(self):
        self.do_animations()
        
        glBegin(GL_QUADS)
        color_index = 0
        for surface in self.surfaces:
            glColor3fv(self.getColorArray()[color_index])
            color_index += 1
            for vertex in surface:
                glVertex3fv(self.verticies[vertex])
        glEnd()
    
        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                glColor3fv(GRAY)
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

    def translate_size(self, translate_matrix):
        self.translate(np.array(translate_matrix) * self.size)

    def translate(self, translate_matrix):
        for vertex in self.verticies:
            v = np.array(vertex) + np.array(translate_matrix)
            self.assing_vertex(vertex, v)
      
    def do_animations(self, speed=15):
        if (self.angle_x[0] < self.angle_x[1]):
            self.angle_x[0] += speed
            self.rotateX(speed)
        elif (self.angle_x[0] > self.angle_x[1]):
            self.angle_x[0] -= speed
            self.rotateX(-speed)
            
        if (self.angle_y[0] < self.angle_y[1]):
            self.angle_y[0] += speed
            self.rotateY(speed)
        elif (self.angle_y[0] > self.angle_y[1]):
            self.angle_y[0] -= speed
            self.rotateY(-speed)
            
        if (self.angle_z[0] < self.angle_z[1]):
            self.angle_y[0] += speed
            self.rotateY(speed)
        elif (self.angle_z[0] > self.angle_z[1]):
            self.angle_z[0] -= speed
            self.rotateZ(-speed)
            
    def is_on_animation(self):
        return (self.angle_x[0] == self.angle_x[1] and self.angle_y[0] == self.angle_y[1] and self.angle_z[0] == self.angle_z[1]) == False
        
    def animated_rotateX(self,angle):
        if (not self.is_on_animation()):
            self.angle_x[1] += angle
        
    def animated_rotateY(self,angle):
        if (not self.is_on_animation()):
            self.angle_y[1] += angle
        
    def animated_rotateZ(self,angle):
        if (not self.is_on_animation()):
            self.angle_z[1] += angle