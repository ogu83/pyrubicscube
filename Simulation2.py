from Colors3D import *
from Point3D import *
from Line3D import *
from Rect3D import *

class Simulation2:         
    
    lines = []    
    rects = []

    def __init__(self, win_width = 640, win_height = 480, fov = 256, viewer_distance = 4):
        self.fov = fov
        self.viewer_distance = viewer_distance

        pygame.init()

        self.screen = pygame.display.set_mode((win_width, win_height))
        pygame.display.set_caption("3D Simulation 2")

        self.clock = pygame.time.Clock()

        #self.lines = [Line3D(Point3D(0,0,0), Point3D(0,1,0), WHITE, 4),
        #              Line3D(Point3D(0,0,0), Point3D(1,0,0), WHITE, 4)
        #              ]

        self.rects = [Rect3D(Point3D(0,0,0), Point3D(1,0,0), Point3D(1,1,0),  Point3D(0,1,0), WHITE, RED, 4)
                      ]

        self.angleX, self.angleY, self.angleZ = 0, 0, 0        

    def run(self):
        """ Main Loop """
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.clock.tick(50)
            self.screen.fill(BLACK)

            for rect in self.rects:
                rect.rotateX(self.angleX).rotateY(self.angleY).rotateZ(self.angleZ)
                rect.draw(self.screen, self.fov, self.viewer_distance)

            for line in self.lines:  
                line.rotateX(self.angleX).rotateY(self.angleY).rotateZ(self.angleZ)
                line.draw(self.screen, self.fov, self.viewer_distance)

            self.angleX = 1
            self.angleY = 1
            self.angleZ = 1

            pygame.display.flip()