from OpenGL_Geometry import *
from threading import Timer
from HelperFunctions import *
import pickle as pk
import sys
import datetime

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

    
    
    def __init__(self, 
                size=4, 
                position_matrix = [1, 2, 3, 4, 5, 6, 7, 8],
                notation_history = [],
                solution_history = [],
                cube1 = None,
                cube2 = None,
                cube3 = None,
                cube4 = None,
                cube5 = None,
                cube6 = None,
                cube7 = None,
                cube8 = None,
                ):
        self.size = size
        self.position_matrix = position_matrix.copy()
        self.notation_history = notation_history.copy()
        self.solution_history = solution_history.copy()
        
        if cube1 == None:
            self.Cube1 = Cube1(size / 2)
        else:
            self.Cube1 = cube1
        
        if cube2 == None:
            self.Cube2 = Cube2(size / 2)
        else:
            self.Cube2 = cube2
            
        if cube3 == None:
            self.Cube3 = Cube3(size / 2)
        else:
            self.Cube3 = cube3
            
        if cube4 == None:
            self.Cube4 = Cube4(size / 2)
        else:
            self.Cube4 = cube4
            
        if cube5 == None:
            self.Cube5 = Cube5(size / 2)
        else:
            self.Cube5 = cube5
            
        if cube6 == None:
            self.Cube6 = Cube6(size / 2)
        else:
            self.Cube6 = cube6
            
        if cube7 == None:
            self.Cube7 = Cube7(size / 2)
        else:
            self.Cube7 = cube7
            
        if cube8 == None:
            self.Cube8 = Cube8(size / 2)
        else:
            self.Cube8 = cube8
            
        self.solutions = []
        self.solutions_dictionary = dict()
        
    def copy(self):
        obj = Cube222(self.size,
                      self.position_matrix,
                      self.notation_history,
                      self.solution_history,
                      self.Cube1.copy(),
                      self.Cube2.copy(),
                      self.Cube3.copy(),
                      self.Cube4.copy(),
                      self.Cube5.copy(),
                      self.Cube6.copy(),
                      self.Cube7.copy(),
                      self.Cube8.copy())
        return obj

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
        retval = (self.position_matrix) + [SNode.matrix_hash(cube.get_angle_matrix()) for cube in self.cube_array()]
        retval = str(SNode.matrix_hash(retval))            
        return retval

    def draw(self, animation_speed=15):
        for cube in self.cube_array():
            cube.draw(animation_speed)
            
    def is_solved(self):
        possible_solutions = [
            '1234567800000000',
            '5173628433333333',
            '6587214322222222',
            '2648153711111111',
            '3142758611111111',
            '7384516200000000',
            '5768132433333333',
            '1526374822222222',
            '241368573030303030303030',
            '432187652020202020202020',
            '314275861010101010101010',
            '56127834300300300300300300300300',
            '78563412200200200200200200200200',
            '34781256100100100100100100100100',            
            '75318642303303303303303303303303',
            '87436521302302302302302302302302',
            '68245713301301301301301301301301',
            '37154826203203203203203203203203',
            '43218765202202202202202202202202',
            '84627351201201201201201201201201',            
            '13572468103103103103103103103103',
            '21654387102102102102102102102102',
            '42863175101101101101101101101101',            
            '43218765301301301301301301301301',
            '84627351300300300300300300300300',
            '78563412303303303303303303303303',
            '48372615202202202202202202202202',
            '24136857201201201201201201201201',
            '62518473200200200200200200200200'
        ]
        return self.position_matrix_str() in possible_solutions
        # first = ""
        # for cube in self.cube_array():
            # if first == "":
                # first = SNode.matrix_hash(cube.get_angle_matrix())
            # elif first != SNode.matrix_hash(cube.get_angle_matrix()):
                # return False
        # return True


    def is_on_animation(self):
        for cube in self.cube_array():
            if cube.is_on_animation():
                return True

        return False
            
    def do_notation(self, notation, historyOff = False, animated = True):
        if (animated):
            if self.is_on_animation():
                return
    
        if notation == "u":            
            self.do_u(animated)
        elif notation == "ui":
            self.do_ui(animated)
        elif notation == "d":
            self.do_d(animated)
        elif notation == "di":
            self.do_di(animated)
        elif notation == "l":
            self.do_l(animated)
        elif notation == "li":
            self.do_li(animated)
        elif notation == "r":
            self.do_r(animated)
        elif notation == "ri":
            self.do_ri(animated)
        elif notation == "f":
            self.do_f(animated)
        elif notation == "fi":
            self.do_fi(animated)
        elif notation == "b":
            self.do_b(animated)
        elif notation == "bi":
            self.do_bi(animated)

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
    
    def do_ui(self, animated = True):
        for i in self.u_matrix():
            c = self.cube_array()[i-1]
            c.animated_rotateY(90, False, not animated)
        
        Cube222.apply_action(self.position_matrix,"ui")

    def do_u(self, animated = True):
        for i in self.u_matrix():
            c = self.cube_array()[i-1]            
            c.animated_rotateY(-90, False, not animated)            

        Cube222.apply_action(self.position_matrix,"u")
                
    def do_di(self, animated = True):
        for i in self.d_matrix():
            c = self.cube_array()[i-1]
            c.animated_rotateY(90, False, not animated)
        
        Cube222.apply_action(self.position_matrix,"di")

    def do_d(self, animated = True):
        for i in self.d_matrix():
            c = self.cube_array()[i-1]
            c.animated_rotateY(-90, False, not animated)

        Cube222.apply_action(self.position_matrix,"d")
        
    def do_li(self, animated = True):
        for i in self.l_matrix():
            c = self.cube_array()[i-1]
            c.animated_rotateX(90, False, not animated)

        Cube222.apply_action(self.position_matrix,"li")

    def do_l(self, animated = True):
        for i in self.l_matrix():
            c = self.cube_array()[i-1]
            c.animated_rotateX(-90, False, not animated)

        Cube222.apply_action(self.position_matrix,"l")
        
    def do_ri(self, animated = True):
        for i in self.r_matrix():
            c = self.cube_array()[i-1]
            c.animated_rotateX(90, False, not animated)

        Cube222.apply_action(self.position_matrix,"ri")

    def do_r(self, animated = True):
        for i in self.r_matrix():
            c = self.cube_array()[i-1]
            c.animated_rotateX(-90, False, not animated)
        
        Cube222.apply_action(self.position_matrix,"r")

    def do_fi(self, animated = True):
        for i in self.f_matrix():
            c = self.cube_array()[i-1]
            c.animated_rotateZ(90, False, not animated)

        Cube222.apply_action(self.position_matrix,"fi")

    def do_f(self, animated = True):
        for i in self.f_matrix():
            c = self.cube_array()[i-1]
            c.animated_rotateZ(-90, False, not animated)

        Cube222.apply_action(self.position_matrix,"f")
    
    def do_bi(self, animated = True):
        for i in self.b_matrix():
            c = self.cube_array()[i-1]
            c.animated_rotateZ(90, False, not animated)

        Cube222.apply_action(self.position_matrix,"bi")

    def do_b(self, animated = True):
        for i in self.b_matrix():
            c = self.cube_array()[i-1]           
            c.animated_rotateZ(-90, False, not animated)
        
        Cube222.apply_action(self.position_matrix,"b")

    def notations(self, use_inverse=True):
        def addi(elem):
            return elem + 'i'

        notations = ['u','d','f','b','l','r']
        
        if use_inverse:
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
        
    def apply_solution(self, speed=0.2, notations=[]):
        # print(speed, notations)   

        mult = 1.5
        if len(notations) > 0:        
            notations = list(reversed(notations))
        def apply_solution_func(m):            
            if len(notations) > 0:
                n = notations.pop()
                self.do_notation(n, False)                
                Timer(speed * m, apply_solution_func, [mult]).start()
                
        apply_solution_func(mult)
        
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

    def dfs(self, speed=0.2, depth = 1, begin_time = datetime.datetime.now()):
    
        def backline():        
            print('\r', end='')
        
        self.solution_history = []
        if self.is_solved():
            return
        
        notations = self.notations(False)
        solutions = notations.copy()
        
        # if (len(self.solutions) == 0):
        print(begin_time.strftime("%H:%M:%S") + " | Calculating Possible Solutions, Depth: " + str(depth))        
        for d in range(depth):                                  
            if d in self.solutions_dictionary:
                solutions = self.solutions_dictionary[d]
            else:                           
                solutions = permutation(solutions, notations)                
                self.solutions_dictionary[d] = solutions
            
            now = datetime.datetime.now()            
            print(f"{now.strftime('%H:%M:%S')} | Depth:{d}, Count: {len(solutions)}, Last:{solutions[-1:]}")           
    
        now = datetime.datetime.now()        
        print(now.strftime("%H:%M:%S") + " | Possible Solutions Calculated")
        self.solutions = solutions
        # else:
            # solutions = self.solutions
                        
        solution_found = False
        sc = 0
        lsc = len(solutions)        
        for s in solutions:
            cube222 = self.copy()
            n_arr = s.split(' ',)
                             
            # Clear ot repeated known rotations make less
            while(True):
                remove_on = False
                repeated_rotations = False
                for i, n in enumerate(n_arr):
                    if (i > 2):
                        if n_arr[i-3] == n_arr[i-2] and n_arr[i-2] == n_arr[i-1] and n_arr[i-1] == n_arr[i]:                        
                            n_arr[i] = "_"
                            n_arr[i-1] = "_"
                            n_arr[i-2] = "_"
                            n_arr[i-3] = "_"
                            remove_on = True
                            repeated_rotations = True
                    elif (i > 1):
                        if n_arr[i-2] == n_arr[i-1] and n_arr[i-1] == n_arr[i]:                        
                            n_arr[i] = n_arr[i] + "i"
                            n_arr[i-1] = "_"
                            n_arr[i-2] = "_"
                            remove_on = True
                            repeated_rotations = True
                    elif (i > 0):
                        if n_arr[i-1] == n_arr[i] + "i":
                            n_arr[i] = "_"
                            n_arr[i-1] = "_"
                            remove_on = True
                            repeated_rotations = True
                
                if remove_on:                    
                    n_arr = list(filter(("_").__ne__, n_arr))
                    
                if not repeated_rotations:
                    break
            
            ns_arr = []
            for n in n_arr:                
                ns_arr.append(n)
                cube222.do_notation(n, True, False)                
                
            if cube222.is_solved():
                now = datetime.datetime.now()
                t_delta = now - begin_time
                print(now.strftime("%H:%M:%S"))
                print("Solved in " + str(t_delta))
                print("From: " + self.position_matrix_str())
                print("Solution: " + str(ns_arr))
                print("To: " + cube222.position_matrix_str())
                # print(cube222.is_solved())
                self.apply_solution(speed, ns_arr)
                solution_found = True
                # break
            
            if solution_found:                
                break
            else:
                if (sc % 1000 == 0):
                    now = datetime.datetime.now()        
                    print(f"{now.strftime('%H:%M:%S')} | Progress: {sc}/{lsc}, Last: {ns_arr}")
                sc += 1
                del cube222
                del n_arr
                del ns_arr                   

        if not solution_found:        
            self.dfs(speed, depth + 1, begin_time)
                
    def animated_rotateY(self, angle, use_self_center):
        pass
        
    def animated_rotateX(self, angle, use_self_center):
        pass                