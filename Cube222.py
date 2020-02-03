from OpenGL_Geometry import *
from threading import Timer
from HelperFunctions import *
import pickle as pk

class SNode():
    def __init__(self, from_matrix, to_matrix, notation, distance):
        self.from_matrix = from_matrix
        self.to_matrix = to_matrix
        self.notation = notation
        self.distance = distance

    @staticmethod
    def matrix_hash(matrix):
        return int(''.join(map(str,matrix)))

    @property
    def from_hash(self):
        return SNode.matrix_hash(self.from_matrix)

    @property
    def to_hash(self):
        return SNode.matrix_hash(self.to_matrix)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f'{str(self.from_hash)}|{self.notation}|{self.to_hash}|{self.distance}'

    def inverse(self):
        notation = self.notation
        if (len(notation) > 1):
            notation = notation[0]
        else: 
            notation = notation + "i"

        return SNode(self.to_matrix, self.from_matrix, notation, self.distance)

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
        self.notation_history = []
        self.solution_history = []
        self.nodes = []
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
        retval = [SNode.matrix_hash(self.position_matrix)]
        for cube in self.cube_array():
            retval.append(SNode.matrix_hash(cube.get_angle_matrix()))
        retval = SNode.matrix_hash(retval);        
        return str(retval)

    def draw(self, animation_speed=15):
        for cube in self.cube_array():
            cube.draw(animation_speed)
            
    def is_solved(self):
        first = ""
        for cube in self.cube_array():
            if first == "":
                first = SNode.matrix_hash(cube.get_angle_matrix())
            elif first != SNode.matrix_hash(cube.get_angle_matrix()):
                return False
        return True


    def is_on_animation(self):
        for cube in self.cube_array():
            if cube.is_on_animation():
                return True

        return False
            
    def do_notation(self, notation, historyOff = False):
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

        if (not historyOff):
            self.notation_history.append(notation)

    def notation_history_str(self):
        return ' '.join(self.notation_history)
        

    def solution_history_str(self):
        return ' '.join(self.solution_history)

    @staticmethod
    def apply_action(matrix, notation):
        if notation == "u":
            p1 = matrix[0]
            p2 = matrix[1]
            p3 = matrix[2]
            p4 = matrix[3]            
            matrix[0] = p2
            matrix[1] = p4
            matrix[2] = p1
            matrix[3] = p3                    
        elif notation == "ui":
            p1 = matrix[0]
            p2 = matrix[1]
            p3 = matrix[2]
            p4 = matrix[3]
            matrix[0] = p3
            matrix[1] = p1
            matrix[2] = p4
            matrix[3] = p2
        elif notation == "d":
            p5 = matrix[4]
            p6 = matrix[5]
            p7 = matrix[6]
            p8 = matrix[7]            
            matrix[4] = p6
            matrix[5] = p8
            matrix[6] = p5
            matrix[7] = p7
        elif notation == "di":
            p5 = matrix[4]
            p6 = matrix[5]
            p7 = matrix[6]
            p8 = matrix[7]            
            matrix[4] = p7
            matrix[5] = p5
            matrix[6] = p8
            matrix[7] = p6
        elif notation == "l":
            p1 = matrix[0]
            p3 = matrix[2]
            p5 = matrix[4]
            p7 = matrix[6]            
            matrix[0] = p5
            matrix[2] = p1
            matrix[4] = p7
            matrix[6] = p3
        elif notation == "li":
            p1 = matrix[0]
            p3 = matrix[2]
            p5 = matrix[4]
            p7 = matrix[6]        
            matrix[0] = p3
            matrix[2] = p7
            matrix[4] = p1
            matrix[6] = p5
        elif notation == "r":
            p2 = matrix[1]
            p4 = matrix[3]
            p6 = matrix[5]
            p8 = matrix[7]            
            matrix[1] = p6
            matrix[3] = p2
            matrix[5] = p8
            matrix[7] = p4
        elif notation == "ri":
            p2 = matrix[1]
            p4 = matrix[3]
            p6 = matrix[5]
            p8 = matrix[7]            
            matrix[1] = p4
            matrix[3] = p8
            matrix[5] = p2
            matrix[7] = p6
        elif notation == "f":
            p1 = matrix[0]
            p2 = matrix[1]
            p5 = matrix[4]
            p6 = matrix[5]            
            matrix[0] = p5
            matrix[1] = p1
            matrix[4] = p6
            matrix[5] = p2
        elif notation == "fi":
            p1 = matrix[0]
            p2 = matrix[1]
            p5 = matrix[4]
            p6 = matrix[5]            
            matrix[0] = p2
            matrix[1] = p6
            matrix[4] = p1
            matrix[5] = p5
        elif notation == "b":
            p3 = matrix[2]
            p4 = matrix[3]
            p7 = matrix[6]
            p8 = matrix[7]            
            matrix[2] = p7
            matrix[3] = p3
            matrix[6] = p8
            matrix[7] = p4
        elif notation == "bi":
            p3 = matrix[2]
            p4 = matrix[3]
            p7 = matrix[6]
            p8 = matrix[7]            
            matrix[2] = p4
            matrix[3] = p8
            matrix[6] = p3
            matrix[7] = p7

        return matrix
    
    def do_ui(self):
        for i in self.u_matrix():
            c = self.cube_array()[i-1]
            c.animated_rotateY(90, False)
        
        Cube222.apply_action(self.position_matrix,"ui")

    def do_u(self):
        for i in self.u_matrix():
            c = self.cube_array()[i-1]
            c.animated_rotateY(-90, False)

        Cube222.apply_action(self.position_matrix,"u")
                
    def do_di(self):
        for i in self.d_matrix():
            c = self.cube_array()[i-1]
            c.animated_rotateY(90, False)
        
        Cube222.apply_action(self.position_matrix,"di")

    def do_d(self):
        for i in self.d_matrix():
            c = self.cube_array()[i-1]
            c.animated_rotateY(-90, False)

        Cube222.apply_action(self.position_matrix,"d")
        
    def do_li(self):
        for i in self.l_matrix():
            c = self.cube_array()[i-1]
            c.animated_rotateX(90, False)

        Cube222.apply_action(self.position_matrix,"li")

    def do_l(self):
        for i in self.l_matrix():
            c = self.cube_array()[i-1]
            c.animated_rotateX(-90, False)

        Cube222.apply_action(self.position_matrix,"l")
        
    def do_ri(self):
        for i in self.r_matrix():
            c = self.cube_array()[i-1]
            c.animated_rotateX(90, False)

        Cube222.apply_action(self.position_matrix,"ri")

    def do_r(self):
        for i in self.r_matrix():
            c = self.cube_array()[i-1]
            c.animated_rotateX(-90, False)
        
        Cube222.apply_action(self.position_matrix,"r")

    def do_fi(self):
        for i in self.f_matrix():
            c = self.cube_array()[i-1]
            c.animated_rotateZ(90, False)

        Cube222.apply_action(self.position_matrix,"fi")

    def do_f(self):
        for i in self.f_matrix():
            c = self.cube_array()[i-1]
            c.animated_rotateZ(-90, False)

        Cube222.apply_action(self.position_matrix,"f")
    
    def do_bi(self):
        for i in self.b_matrix():
            c = self.cube_array()[i-1]
            c.animated_rotateZ(90, False)

        Cube222.apply_action(self.position_matrix,"bi")

    def do_b(self):
        for i in self.b_matrix():
            c = self.cube_array()[i-1]
            c.animated_rotateZ(-90, False)
        
        Cube222.apply_action(self.position_matrix,"b")

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

    def rollback_history(self, speed=0.2):               
        def rollback_history_func(m):
            if len(self.notation_history) > 0:
                n = self.notation_history.pop()
                if (len(n) > 1):
                    n = n[0]
                else: 
                    n = n + "i"
            
                self.do_notation(n, True)                
                Timer(speed * m, rollback_history_func, [1]).start()
                
        rollback_history_func(1)
        
    def learn(self, sEpoch = 0, eEpoch=6, save_pickle=True, load_pickle=True, file_name="222nodes.pkl"):
        if not self.is_solved():
            print('Its not solved, to learn solved cube is needed')
        notations = self.notations()

        if load_pickle:
            try:
                with open('222nodes.pkl', 'rb') as handle:
                    self.nodes = pk.load(handle)
            except:
                self.nodes = []

        for n in notations:            
            tm = self.position_matrix.copy()
            Cube222.apply_action(tm, n)
            tm_hash = SNode.matrix_hash(tm)
            allowed_add = not any(filter(lambda node: (tm_hash == node.to_hash) or (tm_hash == node.from_hash), self.nodes))                                    
            if allowed_add:
                fm = self.position_matrix.copy()
                snode = SNode(fm, tm, n, 0)
                snode = snode.inverse()
                self.nodes.append(snode)

        for e in range(sEpoch, eEpoch):
            epoch_nodes = filter(lambda node: (node.distance == e), self.nodes)
            for snode in epoch_nodes:                
                #print(f".", end="", flush=False)                
                for n in notations:                    
                    tm = snode.from_matrix.copy()                    
                    Cube222.apply_action(tm, n)
                    tm_hash = SNode.matrix_hash(tm)
                    allowed_add = not any(filter(lambda node: (tm_hash == node.to_hash) or (tm_hash == node.from_hash), self.nodes))                                    
                    if allowed_add:
                        fm = snode.from_matrix.copy()
                        new_snode = SNode(fm, tm, n, snode.distance + 1)                        
                        new_snode = new_snode.inverse()
                        self.nodes.append(new_snode)
                        print(f"Epoch: {e}, Node Count: {len(self.nodes)}, LastNode:{self.nodes[len(self.nodes)-1]}")                                
                
                
        if save_pickle:
            with open(file_name, 'wb') as handle:
                pk.dump(self.nodes, handle, protocol=pk.HIGHEST_PROTOCOL)            
            
    def solve(self, speed=0.2, load_pickle=True, file_name="222nodes.pkl"):
        self.solution_history = []
        if self.is_solved():
            return
        
        notations = self.notations()

        if load_pickle:
            try:
                with open('222nodes.pkl', 'rb') as handle:
                    self.nodes = pk.load(handle)
            except:
                self.learn()
        else:
            self.learn(load_pickle = False)

        def find_best_notation():
            pos_hash = SNode.matrix_hash(self.position_matrix) 
            n = filter(lambda node: (node.from_hash == pos_hash), self.nodes)
            n = sorted(n, key = lambda node: node.distance)
            n = first(n)
            if (not n):
                n = notations[random.randint(0, len(notations)-1)]
            else:
                n = n.notation

            return n

        def solve_func(m):            
            n = find_best_notation()
            self.do_notation(n, True)
            if not self.is_solved():
                Timer(speed * m, solve_func, [1]).start()
                self.solution_history.append(n)

        solve_func(1)

    def dfs(self, max_move = 20):
        self.solution_history = []
        if self.is_solved():
            return
        
        notations = self.notations()

        

        pass

                
    def animated_rotateY(self, angle, use_self_center):
        pass
        
    def animated_rotateX(self, angle, use_self_center):
        pass                