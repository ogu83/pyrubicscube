import numpy as np
import sys, math, pygame, random
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL_Geometry import *
from OpenGL_Colors import *

class Simulation3:   
    def __init__(self, win_width = 640, win_height = 480):
        self.win_width = win_width
        self.win_height = win_height

    def run(self):
        pygame.init()
        
        display = (self.win_width, self.win_height)
        pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
        glEnable(GL_DEPTH_TEST)

        gluPerspective(45, (display[0]/display[1]), 0.1, 100)
        glRotatef(45, 0.5, -0.5, -0.125)
        glTranslatef(-25, -25, -25)
        
        cube = Cube3D(4)
        grid = Grid3D(4, 64, 64)
                
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
                        
            grid.draw()
            cube.draw()
            
            pygame.display.flip()
            pygame.time.wait(1)