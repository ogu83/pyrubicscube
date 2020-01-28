import numpy as np
import math, pygame, random

from OpenGL_Colors import *
from OpenGL.GL import *
from OpenGL.GLU import *

UNIT_CUBE_VERTICIES=[
    [1.0, -1.0, -1.0],
    [1.0, 1.0, -1.0],
    [-1.0, 1.0, -1.0],
    [-1.0, -1.0, -1.0],
    [1.0, -1.0, 1.0],
    [1.0, 1.0, 1.0],
    [-1.0, -1.0, 1.0],
    [-1.0, 1.0, 1.0]
]

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
        
        self.translate_matrix = [0, 0, 0]
        
        self.verticies = UNIT_CUBE_VERTICIES
        
        self.verticies = np.array(self.verticies) * size
        
        self.color_d = color_d #WHITE
        self.color_u = color_u #YELLOW
        self.color_b = color_b #GREEN                
        self.color_f = color_f #BLUE                        
        self.color_l = color_l #ORANGE
        self.color_r = color_r #RED
        
        self.angle_x = [0, 0, False]
        self.angle_y = [0, 0, False]
        self.angle_z = [0, 0, False]        
        
    def getColorArray(self):
        return [            
            self.color_b, #GREEN
            self.color_l, #ORANGE             
            self.color_f, #BLUE 
            self.color_r, #RED                                              
            self.color_u, #YELLOW
            self.color_d, #WHITE            
        ]
        
    def draw(self, animation_speed=15):
        self.do_animations(animation_speed)
        
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

    def assing_rotate_all_vertex(self, rotation_matrix):
        for vertex in self.verticies:
            v = rotation_matrix.dot(vertex)
            self.assing_vertex(vertex, v)    
        
    def rotateX(self, angle, use_self_center=False):        
        rad = angle * math.pi / 180
        cosa = (math.cos(rad))
        sina = (math.sin(rad))        
        rotation_matrix = np.array([[1.0, 0.0, 0.0],
                                    [0.0, cosa, -sina],
                                    [0.0, sina, cosa]])

        if (use_self_center):
            tran_matrix = self.translate_matrix
            self.translate_size(-1*np.array(tran_matrix), False)
            self.assing_rotate_all_vertex(rotation_matrix)            
            self.translate_size(tran_matrix, False)
        else:
            self.assing_rotate_all_vertex(rotation_matrix)
        
    def rotateY(self, angle, use_self_center=False):
        rad = angle * math.pi / 180
        cosa = (math.cos(rad))
        sina = (math.sin(rad))        
        rotation_matrix = np.array([[cosa, 0.0, sina],
                                    [0.0, 1.0, 0.0],
                                    [-sina, 0.0, cosa]])
        
        if (use_self_center):
            tran_matrix = self.translate_matrix
            self.translate_size(-1*np.array(tran_matrix), False)
            self.assing_rotate_all_vertex(rotation_matrix)            
            self.translate_size(tran_matrix, False)
        else:
            self.assing_rotate_all_vertex(rotation_matrix)
        
    def rotateZ(self, angle, use_self_center=False):
        rad = angle * math.pi / 180
        cosa = (math.cos(rad))
        sina = (math.sin(rad))
        rotation_matrix = np.array([[cosa, -sina, 0.0],
                                    [sina, cosa, 0.0],
                                    [0.0, 0.0, 1.0]])
        
        if (use_self_center):
            tran_matrix = self.translate_matrix
            self.translate_size(-1*np.array(tran_matrix), False)
            self.assing_rotate_all_vertex(rotation_matrix)            
            self.translate_size(tran_matrix, False)
        else:
            self.assing_rotate_all_vertex(rotation_matrix)

    def translate_size(self, translate_matrix, permanent):        
        if permanent:
            self.translate_matrix = list(np.array(self.translate_matrix) + np.array(translate_matrix))

        self.translate(np.array(translate_matrix) * self.size, False)

    def translate(self, translate_matrix, permanent):
        if permanent:
            self.translate_matrix = list(np.array(self.translate_matrix) + np.array(translate_matrix))

        for vertex in self.verticies:
            v = np.array(vertex) + np.array(translate_matrix)
            self.assing_vertex(vertex, v)
      
    def do_animations(self, speed=15):
        if (self.angle_x[0] < self.angle_x[1]):
            self.angle_x[0] += speed
            self.rotateX(speed, self.angle_x[2])
        elif (self.angle_x[0] > self.angle_x[1]):
            self.angle_x[0] -= speed
            self.rotateX(-speed, self.angle_x[2])
            
        if (self.angle_y[0] < self.angle_y[1]):
            self.angle_y[0] += speed
            self.rotateY(speed, self.angle_y[2])
        elif (self.angle_y[0] > self.angle_y[1]):
            self.angle_y[0] -= speed
            self.rotateY(-speed, self.angle_y[2])
            
        if (self.angle_z[0] < self.angle_z[1]):
            self.angle_z[0] += speed
            self.rotateZ(speed, self.angle_z[2])
        elif (self.angle_z[0] > self.angle_z[1]):
            self.angle_z[0] -= speed
            self.rotateZ(-speed, self.angle_z[2])
            
    def is_on_animation(self):
        return (self.angle_x[0] == self.angle_x[1] 
            and self.angle_y[0] == self.angle_y[1] 
            and self.angle_z[0] == self.angle_z[1]) == False
        
    def animated_rotateX(self, angle, use_self_center):
        if (not self.is_on_animation()):
            self.angle_x[1] += angle
            self.angle_x[2] = use_self_center
        
    def animated_rotateY(self, angle, use_self_center):
        if (not self.is_on_animation()):
            self.angle_y[1] += angle
            self.angle_y[2] = use_self_center
        
    def animated_rotateZ(self, angle, use_self_center):
        if (not self.is_on_animation()):
            self.angle_z[1] += angle
            self.angle_z[2] = use_self_center