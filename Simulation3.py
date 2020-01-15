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
    angle_x = 0    

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

    def __init__(self, size, color):
        self.size = float(size)
        self.color = color
        self.verticies = np.array(self.verticies) * size
        
    def draw(self):
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
        
    def rotateX(self, angle):
        rad = angle * math.pi / 180
        cosa = (math.cos(rad))
        sina = (math.sin(rad))
        
        r_y = np.array([[1.0,0.0,0.0],[0.0,cosa,-sina],[0,sina,cosa]])
        
        for vertex in self.verticies:
            v = r_y.dot(vertex)
            vertex[0] = v[0]
            vertex[1] = v[1]
            vertex[2] = v[2]
        
    def rotateY(self, angle):
        rad = angle * math.pi / 180
        cosa = (math.cos(rad))
        sina = (math.sin(rad))
        
        r_y = np.array([[cosa,0.0,sina],[0.0,1.0,0.0],[-sina,0.0,cosa]])
        
        for vertex in self.verticies:
            v = r_y.dot(vertex)
            vertex[0] = v[0]
            vertex[1] = v[1]
            vertex[2] = v[2]
        
    def rotateZ(self, angle):
        rad = angle * math.pi / 180
        cosa = (math.cos(rad))
        sina = (math.sin(rad))
        
        r_z = np.array([[cosa,-sina,0.0],[sina,cosa,0.0],[0.0,0.0,1.0]])
        
        for vertex in self.verticies:
            v = r_z.dot(vertex)
            vertex[0] = v[0]
            vertex[1] = v[1]
            vertex[2] = v[2]

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
        
        cube = Cube3D(3, RED)
        
        while True:
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    
                if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_LEFT):
                        cube.rotateY(10)
                    if (event.key == pygame.K_RIGHT):
                        cube.rotateY(-10)
                    if (event.key == pygame.K_UP):
                        cube.rotateX(-10)
                    if (event.key == pygame.K_DOWN):
                        cube.rotateX(10)
                                            
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
                        
            cube.draw()
            
            pygame.display.flip()
            pygame.time.wait(10)    