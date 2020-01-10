from Point3D import *

class Simulation:
    def __init__(self, win_width = 640, win_height = 480):
        pygame.init()
 
        self.screen = pygame.display.set_mode((win_width, win_height))
        pygame.display.set_caption("3D Wireframe Cube Simulation (http://codeNtronix.com)")
 
        self.clock = pygame.time.Clock()
 
        self.vertices = [
            Point3D(-1,1,-1),
            Point3D(1,1,-1),
            Point3D(1,-1,-1),
            Point3D(-1,-1,-1),
            Point3D(-1,1,1),
            Point3D(1,1,1),
            Point3D(1,-1,1),
            Point3D(-1,-1,1)
        ]
 
        # Define the vertices that compose each of the 6 faces. These numbers are
        # indices to the vertices list defined above.
        self.faces = [(0,1,2,3),(1,5,6,2),(5,4,7,6),(4,0,3,7),(0,4,5,1),(3,2,6,7)]
 
        self.angleX, self.angleY, self.angleZ = 0, 0, 0
 
    def run(self):
        """ Main Loop """
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
 
            self.clock.tick(50)
            self.screen.fill((0,0,0))
 
            # Will hold transformed vertices.
            t = []
 
            for v in self.vertices:
                # Rotate the point around X axis, then around Y axis, and finally around Z axis.
                r = v.rotateX(self.angleX).rotateY(self.angleY).rotateZ(self.angleZ)
                # Transform the point from 3D to 2D
                p = r.project(self.screen.get_width(), self.screen.get_height(), 256, 4)
                # Put the point in the list of transformed vertices
                t.append(p)
 
            for f in self.faces:
                pygame.draw.line(self.screen, (255,255,255), (t[f[0]].x, t[f[0]].y), (t[f[1]].x, t[f[1]].y))
                pygame.draw.line(self.screen, (255,255,255), (t[f[1]].x, t[f[1]].y), (t[f[2]].x, t[f[2]].y))
                pygame.draw.line(self.screen, (255,255,255), (t[f[2]].x, t[f[2]].y), (t[f[3]].x, t[f[3]].y))
                pygame.draw.line(self.screen, (255,255,255), (t[f[3]].x, t[f[3]].y), (t[f[0]].x, t[f[0]].y))
 
            self.angleX += 1
            #self.angleY += 1
            #self.angleZ += 1
 
            pygame.display.flip()