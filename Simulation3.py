import numpy as np
import sys, math, pygame, random
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL_Geometry import *
from OpenGL_Colors import *

LEFT = 1
RIGHT = 3

class Simulation3:   
   
    left_click_on = False
    right_click_on = False
    
    last_mouse_pos = (0,0)
    mouse_sensitivity = 50
    
    def __init__(self, win_width = 800, win_height = 600):
        self.win_width = win_width
        self.win_height = win_height

    def run(self):
        pygame.init()
        
        display = (self.win_width, self.win_height)
        pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
        glEnable(GL_DEPTH_TEST)

        gluPerspective(60, (self.win_width/self.win_height), 0.1, 100)
        glRotatef(45, 0.5, -0.5, -0.125)
        glTranslatef(-25,-25,-25)
        
        cube = Cube3D(4)
        grid = Grid3D(4, 64, 64)
        
        while True:       
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()                   
                elif event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_LEFT):
                        cube.animated_rotateY(-90)
                    if (event.key == pygame.K_RIGHT):
                        cube.animated_rotateY(90)
                    if (event.key == pygame.K_UP):
                        cube.animated_rotateX(-90)
                    if (event.key == pygame.K_DOWN):
                        cube.animated_rotateX(90)            
                elif event.type == pygame.MOUSEMOTION:
                    if (self.left_click_on):
                        cam_x = (event.pos[0] - self.last_mouse_pos[0])/self.mouse_sensitivity
                        cam_y = (event.pos[1] - self.last_mouse_pos[1])/self.mouse_sensitivity
                        glTranslatef(cam_x, 0, cam_y)
                        self.last_mouse_pos = event.pos
                    elif (self.right_click_on):
                        cam_y = -(event.pos[0] - self.last_mouse_pos[0])/self.mouse_sensitivity
                        cam_z = (event.pos[1] - self.last_mouse_pos[1])/self.mouse_sensitivity
                        glTranslatef(0, cam_y, cam_z)
                        self.last_mouse_pos = event.pos
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                    self.left_click_on = True
                    self.last_mouse_pos = event.pos                    
                elif event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
                    self.left_click_on = False
                    self.last_mouse_pos = (0,0)
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
                    self.right_click_on = True
                    self.last_mouse_pos = event.pos                    
                elif event.type == pygame.MOUSEBUTTONUP and event.button == RIGHT:
                    self.right_click_on = False
                    self.last_mouse_pos = (0,0)
                                            
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
                        
            grid.draw()
            cube.draw()
            
            pygame.display.flip()
            pygame.time.wait(1)