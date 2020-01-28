from OpenGL_Geometry import *
from threading import Timer

class Cube1(Cube3D):
    def __init__(self, size):
        super().__init__(size, YELLOW, BLACK, BLUE, BLACK, ORANGE, BLACK)
        self.translate_size([-1,1,1], True)

class Cube2(Cube3D):
    def __init__(self, size):
        super().__init__(size, YELLOW, BLACK, BLUE, BLACK, BLACK, RED)
        self.translate_size([1,1,1], True)

class Cube3(Cube3D):
    def __init__(self, size):
        super().__init__(size, YELLOW, BLACK, BLACK, GREEN, ORANGE, BLACK)
        self.translate_size([-1,1,-1], True)

class Cube4(Cube3D):
    def __init__(self, size):
        super().__init__(size, YELLOW, BLACK, BLACK, GREEN, BLACK, RED)
        self.translate_size([1,1,-1], True)

class Cube5(Cube3D):
    def __init__(self, size):
        super().__init__(size, BLACK, WHITE, BLUE, BLACK, ORANGE, BLACK)
        self.translate_size([-1,-1,1], True)

class Cube6(Cube3D):
    def __init__(self, size):
        super().__init__(size, BLACK, WHITE, BLUE, BLACK, BLACK, RED)
        self.translate_size([1,-1,1], True)

class Cube7(Cube3D):
    def __init__(self, size):
        super().__init__(size, BLACK, WHITE, BLACK, GREEN, ORANGE, BLACK)
        self.translate_size([-1,-1,-1], True)

class Cube8(Cube3D):    
    def __init__(self, size):
        super().__init__(size, BLACK, WHITE, BLACK, GREEN, BLACK, RED)
        self.translate_size([1,-1,-1], True)


class Cube222:
    
    def __init__(self, size=4):
        self.position_matrix = [1, 2, 3, 4, 5, 6, 7, 8]
        self.Cube1 = Cube1(size / 2)
        self.Cube2 = Cube2(size / 2)
        self.Cube3 = Cube3(size / 2)
        self.Cube4 = Cube4(size / 2)
        self.Cube5 = Cube5(size / 2)
        self.Cube6 = Cube6(size / 2)
        self.Cube7 = Cube7(size / 2)
        self.Cube8 = Cube8(size / 2)

    def cube_array(self):
        return [self.Cube1, self.Cube2, self.Cube3, self.Cube4, self.Cube5, self.Cube6, self.Cube7, self.Cube8]
        
    def u_matrix(self):
        position_matrix = self.position_matrix
        return [position_matrix[0], position_matrix[1], position_matrix[2], position_matrix[3]]
        
    def d_matrix(self):
        position_matrix = self.position_matrix
        return [position_matrix[4], position_matrix[5], position_matrix[6], position_matrix[7]]
        
    def l_matrix(self):
        position_matrix = self.position_matrix
        return [position_matrix[0], position_matrix[2], position_matrix[4], position_matrix[6]]
        
    def r_matrix(self):
        position_matrix = self.position_matrix
        return [position_matrix[1], position_matrix[3], position_matrix[5], position_matrix[7]]
        
    def f_matrix(self):
        position_matrix = self.position_matrix
        return [position_matrix[0], position_matrix[1], position_matrix[4], position_matrix[5]]
        
    def b_matrix(self):
        position_matrix = self.position_matrix
        return [position_matrix[2], position_matrix[3], position_matrix[6], position_matrix[7]]
        
    def position_matrix_str(self):
        retval = "CubeMatrix:"
        retval += ("".join(str(self.position_matrix))) 
        return retval

    def draw(self, animation_speed=15):
        for cube in self.cube_array():
            cube.draw(animation_speed)
            
    def is_solved(self):
        return self.position_matrix == [1, 2, 3, 4, 5, 6, 7, 8]

    def is_on_animation(self):
        for cube in self.cube_array():
            if cube.is_on_animation():
                return True

        return False
            
    def do_notation(self, notation):
        if self.is_on_animation():
            return
    
        if notation == "u":
            self.do_u()
        elif notation == "ui":
            self.do_ui()
        elif notation == "d":
            self.do_d()
        elif notation == "di":
            self.do_di()
        elif notation == "l":
            self.do_l()
        elif notation == "li":
            self.do_li()
        elif notation == "r":
            self.do_r()
        elif notation == "ri":
            self.do_ri()
        elif notation == "f":
            self.do_f()
        elif notation == "fi":
            self.do_fi()
        elif notation == "b":
            self.do_b()
        elif notation == "bi":
            self.do_bi()
    
    def do_ui(self):
        for i in self.u_matrix():
            c = self.cube_array()[i-1]
            c.animated_rotateY(90, False)
            
        p1 = self.position_matrix[0]
        p2 = self.position_matrix[1]
        p3 = self.position_matrix[2]
        p4 = self.position_matrix[3]
        
        self.position_matrix[0] = p3
        self.position_matrix[1] = p1
        self.position_matrix[2] = p4
        self.position_matrix[3] = p2

    def do_u(self):
        for i in self.u_matrix():
            c = self.cube_array()[i-1]
            c.animated_rotateY(-90, False)
            
        p1 = self.position_matrix[0]
        p2 = self.position_matrix[1]
        p3 = self.position_matrix[2]
        p4 = self.position_matrix[3]
        
        self.position_matrix[0] = p2
        self.position_matrix[1] = p4
        self.position_matrix[2] = p1
        self.position_matrix[3] = p3
                

    def do_di(self):
        for i in self.d_matrix():
            c = self.cube_array()[i-1]
            c.animated_rotateY(90, False)
            
        p5 = self.position_matrix[4]
        p6 = self.position_matrix[5]
        p7 = self.position_matrix[6]
        p8 = self.position_matrix[7]
        
        self.position_matrix[4] = p7
        self.position_matrix[5] = p5
        self.position_matrix[6] = p8
        self.position_matrix[7] = p6

    def do_d(self):
        for i in self.d_matrix():
            c = self.cube_array()[i-1]
            c.animated_rotateY(-90, False)
            
        p5 = self.position_matrix[4]
        p6 = self.position_matrix[5]
        p7 = self.position_matrix[6]
        p8 = self.position_matrix[7]
        
        self.position_matrix[4] = p6
        self.position_matrix[5] = p8
        self.position_matrix[6] = p5
        self.position_matrix[7] = p7
        

    def do_li(self):
        for i in self.l_matrix():
            c = self.cube_array()[i-1]
            c.animated_rotateX(90, False)
            
        p1 = self.position_matrix[0]
        p3 = self.position_matrix[2]
        p5 = self.position_matrix[4]
        p7 = self.position_matrix[6]
        
        self.position_matrix[0] = p3
        self.position_matrix[2] = p7
        self.position_matrix[4] = p1
        self.position_matrix[6] = p5

    def do_l(self):
        for i in self.l_matrix():
            c = self.cube_array()[i-1]
            c.animated_rotateX(-90, False)
            
        p1 = self.position_matrix[0]
        p3 = self.position_matrix[2]
        p5 = self.position_matrix[4]
        p7 = self.position_matrix[6]
        
        self.position_matrix[0] = p5
        self.position_matrix[2] = p1
        self.position_matrix[4] = p7
        self.position_matrix[6] = p3
        

    def do_ri(self):
        for i in self.r_matrix():
            c = self.cube_array()[i-1]
            c.animated_rotateX(90, False)
            
        p2 = self.position_matrix[1]
        p4 = self.position_matrix[3]
        p6 = self.position_matrix[5]
        p8 = self.position_matrix[7]
        
        self.position_matrix[1] = p4
        self.position_matrix[3] = p8
        self.position_matrix[5] = p2
        self.position_matrix[7] = p6

    def do_r(self):
        for i in self.r_matrix():
            c = self.cube_array()[i-1]
            c.animated_rotateX(-90, False)
            
        p2 = self.position_matrix[1]
        p4 = self.position_matrix[3]
        p6 = self.position_matrix[5]
        p8 = self.position_matrix[7]
        
        self.position_matrix[1] = p6
        self.position_matrix[3] = p2
        self.position_matrix[5] = p8
        self.position_matrix[7] = p4


    def do_fi(self):
        for i in self.f_matrix():
            c = self.cube_array()[i-1]
            c.animated_rotateZ(90, False)
            
        p1 = self.position_matrix[0]
        p2 = self.position_matrix[1]
        p5 = self.position_matrix[4]
        p6 = self.position_matrix[5]
        
        self.position_matrix[0] = p2
        self.position_matrix[1] = p6
        self.position_matrix[4] = p1
        self.position_matrix[5] = p5

    def do_f(self):
        for i in self.f_matrix():
            c = self.cube_array()[i-1]
            c.animated_rotateZ(-90, False)
            
        p1 = self.position_matrix[0]
        p2 = self.position_matrix[1]
        p5 = self.position_matrix[4]
        p6 = self.position_matrix[5]
        
        self.position_matrix[0] = p5
        self.position_matrix[1] = p1
        self.position_matrix[4] = p6
        self.position_matrix[5] = p2
    

    def do_bi(self):
        for i in self.b_matrix():
            c = self.cube_array()[i-1]
            c.animated_rotateZ(90, False)
            
        p3 = self.position_matrix[2]
        p4 = self.position_matrix[3]
        p7 = self.position_matrix[6]
        p8 = self.position_matrix[7]
        
        self.position_matrix[2] = p4
        self.position_matrix[3] = p8
        self.position_matrix[6] = p3
        self.position_matrix[7] = p7

    def do_b(self):
        for i in self.b_matrix():
            c = self.cube_array()[i-1]
            c.animated_rotateZ(-90, False)
            
        p3 = self.position_matrix[2]
        p4 = self.position_matrix[3]
        p7 = self.position_matrix[6]
        p8 = self.position_matrix[7]
        
        self.position_matrix[2] = p7
        self.position_matrix[3] = p3
        self.position_matrix[6] = p8
        self.position_matrix[7] = p4    

    def notations(self):
        def addi(elem):
            return elem + 'i'

        notations = ['u','d','f','b','l','r']
        rn = list(map(addi, notations))
        notations += rn
        return notations

    def scramble(self, moves = 20, speed=0.2):        
        notations = self.notations()
        
        def do_n():
            notation = notations[random.randint(0, len(notations)-1)]
            self.do_notation(notation)
        
        for i in range(moves):
            Timer(speed * i, do_n).start()     
            
    def solve(self, max_iterations = 20):
        pass
                
    def animated_rotateY(self, angle, use_self_center):
        pass
        
    def animated_rotateX(self, angle, use_self_center):
        pass
                