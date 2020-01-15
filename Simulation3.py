import numpy as np
import sys, math, pygame, random
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

"""Colors"""
YELLOW = (1,1,0)
WHITE = (1,1,1)
BLUE = (0,0,1)
GREEN = (0,1,0)
RED = (1,0,0)
ORANGE = (1,0.5,0)
GRAY = (0.752941,0.752941,0.752941)
BLACK = (0,0,0)
MAGENTA = (1,0,1)
CYAN = (0,1,1)

class Vertex3D:
    def __init__(self, x = 0, y = 0, z = 0):
        self.x, self.y, self.z = float(x), float(y), float(z)
        
    def __repr__(self):
        return [self.x, self.y, self.z]
        
    def __str__(self):
        return self.__repr__()

    def rotateX(self, angle):
        """ Rotates the point around the X axis by the given angle in degrees. """
        rad = angle * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        y = self.y * cosa - self.z * sina
        z = self.y * sina + self.z * cosa
        return Vertex3D(self.x, y, z)
    
    def rotateY(self, angle):
        """ Rotates the point around the Y axis by the given angle in degrees. """
        rad = angle * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        z = self.z * cosa - self.x * sina
        x = self.z * sina + self.x * cosa
        return Vertex3D(x, self.y, z)

    def rotateZ(self, angle):
        """ Rotates the point around the Z axis by the given angle in degrees. """
        rad = angle * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        x = self.x * cosa - self.y * sina
        y = self.x * sina + self.y * cosa
        return Vertex3D(x, y, self.z)
        
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

    def __init__(self, size):
        self.size = float(size)        
        self.verticies = np.array(self.verticies) * size
        
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
        rotation_matrix = np.array([[1.0,0.0,0.0],[0.0,cosa,-sina],[0,sina,cosa]])
        self.assing_rotate_all_vertex(rotation_matrix)        
        
    def rotateY(self, angle):
        rad = angle * math.pi / 180
        cosa = (math.cos(rad))
        sina = (math.sin(rad))        
        rotation_matrix = np.array([[cosa,0.0,sina],[0.0,1.0,0.0],[-sina,0.0,cosa]])
        self.assing_rotate_all_vertex(rotation_matrix)
        
    def rotateZ(self, angle):
        rad = angle * math.pi / 180
        cosa = (math.cos(rad))
        sina = (math.sin(rad))        
        rotation_matrix = np.array([[cosa,-sina,0.0],[sina,cosa,0.0],[0.0,0.0,1.0]])
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

class Simulation3:   
    def __init__(self, win_width = 800, win_height = 600):
        self.win_width = win_width
        self.win_height = win_height

    def run(self):
        pygame.init()
        
        display = (self.win_width, self.win_height)
        pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
        glEnable(GL_DEPTH_TEST)

        gluPerspective(45, (display[0]/display[1]), 0.1, 50)
        # glRotatef(15, 1, 1, 0)
        glTranslatef(-4, -4, -25)
        
        cube = Cube3D(3)
        
        while True:
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    
                if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_LEFT):
                        cube.animated_rotateY(-90)
                    if (event.key == pygame.K_RIGHT):
                        cube.animated_rotateY(90)
                    if (event.key == pygame.K_UP):
                        cube.animated_rotateX(-90)
                    if (event.key == pygame.K_DOWN):
                        cube.animated_rotateX(90)
                                            
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
                        
            cube.draw()
            
            pygame.display.flip()
            pygame.time.wait(10)    