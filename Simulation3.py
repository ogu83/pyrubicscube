import numpy as np
import sys, math, pygame, random
from pygame.locals import *
# from OpenGL.GL import *
# from OpenGL.GLU import *
# from OpenGL_Geometry import *
# from OpenGL_Colors import *
from Cube222 import *

LEFT = 1
RIGHT = 3
PY_WAIT = 30
FONT_SIZE = 14

class Simulation3:   
   
    left_click_on = False
    right_click_on = False
    
    last_mouse_pos = (0, 0)
    mouse_sensitivity = 10
    
    on_key_w = False
    on_key_a = False
    on_key_s = False
    on_key_d = False
          
    def __init__(self, win_width = 800, win_height = 600):
        self.win_width = win_width
        self.win_height = win_height
        
    def drawText(self, x=0, y=0, z=0, text="Some text", font_size = 64):
        position = (x, y, z)
        # font = pygame.font.Font(None, font_size)
        all_fonts = pygame.font.get_fonts()
        first_console_font = list(filter(lambda f: "console" in f, all_fonts))
        if len(first_console_font)>0:
            first_console_font = first_console_font[0]
        font = pygame.font.SysFont(first_console_font, font_size)
        textSurface = font.render(text, True, (255,255,255,255), (0,0,0,0))
        textData = pygame.image.tostring(textSurface, "RGBA", True)
        glRasterPos3d(*position)
        glDrawPixels(textSurface.get_width(), textSurface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, textData)

    def isShiftPressed(self):
        return (pygame.key.get_mods() & pygame.KMOD_SHIFT)

    def run(self):
        pygame.init()
        
        display = (self.win_width, self.win_height)
        pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
        glEnable(GL_DEPTH_TEST)

        gluPerspective(60, (self.win_width / self.win_height), 0.1, 200)
        glRotatef(45, 0.5, -0.5, -0.125)
        glTranslatef(-25, -25, -25)
        
        grid = Grid3D(4, 32,32)
        
        #cube = Cube3D(4)        
        #cube.translate_size([0, 1, 0], True) 
        cube = Cube222(4)
        
        while True:       
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()                   
                elif event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_LEFT or event.key == pygame.K_l):
                        if self.isShiftPressed():
                            cube.do_notation("li")
                        else:
                            cube.do_notation("l")
                    elif (event.key == pygame.K_RIGHT or event.key == pygame.K_r):
                        if self.isShiftPressed():
                            cube.do_notation("ri")
                        else:
                            cube.do_notation("r")
                    elif (event.key == pygame.K_UP or event.key == pygame.K_u):
                        if self.isShiftPressed():
                            cube.do_notation("ui")
                        else:
                            cube.do_notation("u")
                    elif (event.key == pygame.K_DOWN or event.key == pygame.K_d):
                        if self.isShiftPressed():
                            cube.do_notation("di")
                        else:
                            cube.do_notation("d")
                    elif (event.key == pygame.K_PAGEUP or event.key == pygame.K_f):
                        if self.isShiftPressed():
                            cube.do_notation("fi")
                        else:
                            cube.do_notation("f")
                    elif (event.key == pygame.K_PAGEDOWN or event.key == pygame.K_b):
                        if self.isShiftPressed():
                            cube.do_notation("bi")
                        else:
                            cube.do_notation("b")
                    elif (event.key == pygame.K_F1):
                        if self.isShiftPressed():
                            cube.rollback_history(PY_WAIT/100)
                        else:
                            cube.scramble(20, PY_WAIT/100)
                    elif (event.key == pygame.K_F2):
                        cube.dfs()
                    elif (event.key == pygame.K_F3):
                        pass
                    
                    elif (event.key == pygame.K_SPACE):
                        print(cube.position_matrix_str())
                    elif (event.key == pygame.K_w):
                        self.on_key_w = True
                    elif (event.key == pygame.K_a):
                        self.on_key_a = True
                    elif (event.key == pygame.K_s):
                        self.on_key_s = True
                    elif (event.key == pygame.K_d):
                        self.on_key_d = True
                elif event.type == pygame.KEYUP:
                    if (event.key == pygame.K_w):
                        self.on_key_w = False
                    elif (event.key == pygame.K_a):
                        self.on_key_a = False
                    elif (event.key == pygame.K_s):
                        self.on_key_s = False
                    elif (event.key == pygame.K_d):
                        self.on_key_d = False
                elif event.type == pygame.MOUSEMOTION:
                    if (self.left_click_on):
                        cam_x = (event.pos[0] - self.last_mouse_pos[0]) / self.mouse_sensitivity
                        cam_y = (event.pos[1] - self.last_mouse_pos[1]) / self.mouse_sensitivity
                        glTranslatef(cam_x, 0, cam_y)
                        self.last_mouse_pos = event.pos
                    elif (self.right_click_on):
                        cam_y = (event.pos[0] - self.last_mouse_pos[0]) / self.mouse_sensitivity
                        cam_z = (event.pos[1] - self.last_mouse_pos[1]) / self.mouse_sensitivity
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
                    
            if (self.on_key_w):
                glTranslatef(1 / self.mouse_sensitivity, 0, 0)
            if (self.on_key_s):
                glTranslatef(-1 / self.mouse_sensitivity, 0, 0)
            if (self.on_key_d):
                glTranslatef(0, -1 / self.mouse_sensitivity, 0)
            if (self.on_key_a):
                glTranslatef(0, 1 / self.mouse_sensitivity, 0)
                                            
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)            
            
            self.drawText(10, 0, -15, "CM: " + cube.position_matrix_str(), FONT_SIZE)
            
            solved_text = "Scrambled"
            if cube.is_solved():
                solved_text = "Solved"
            self.drawText(10, 0, -10, solved_text, FONT_SIZE)

            self.drawText(-170, 0, -70, "F1: Scramble | Shift_F1: Rollback | F2: DFS |", FONT_SIZE);
            self.drawText(-150, 0, -50, "Hs:" + cube.notation_history_str(), FONT_SIZE);
            self.drawText(-130, 0, -40, f"Solution: {cube.solution_history_str()}", FONT_SIZE);
                        
            grid.draw()
            cube.draw(PY_WAIT/2*3)
            
            pygame.display.flip()
            pygame.time.wait(PY_WAIT)
