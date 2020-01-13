import pygame

BLACK, RED = (0, 0, 0), (255, 128, 128)

class Paint:
    def __init__(self, shape, keys_handler):
        self.__shape = shape
        self.__keys_handler = keys_handler
        self.__size = 450, 450
        self.__clock = pygame.time.Clock()
        self.__screen = pygame.display.set_mode(self.__size)
        self.__mainloop()

    def __fit(self, vec):
        """
        ignore the z-element (creating a very cheap projection), and scale x, y to the coordinates of the screen
        """
        # notice that len(self.__size) is 2, hence zip(vec, self.__size) ignores the vector's last coordinate
        return [round(70 * coordinate + frame / 2) for coordinate, frame in zip(vec, self.__size)]

    def __handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        self.__keys_handler(pygame.key.get_pressed())

    def __draw_shape(self, thickness=4):
        for start, end in self.__shape.lines:
            pygame.draw.line(self.__screen, RED, self.__fit(start), self.__fit(end), thickness)

        #left =  self.__fit(self.__shape.lines[0].start)
        #top =  self.__fit(self.__shape.lines[0].start)
        #width = self.__fit(self.__shape.lines[0].end - self.__shape.lines[0].start)
        #height = self.__fit(self.__shape.lines[1].end - self.__shape.lines[1].start)
        #pygame.draw.rect(self.__screen, RED, pygame.rect(left,top,width,hegiht), thickness)

    def __mainloop(self):
        while True:
            self.__handle_events()
            self.__screen.fill(BLACK)
            self.__draw_shape()
            pygame.display.flip()
            self.__clock.tick(40)