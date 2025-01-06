import pygame

import RubiksCubeSolver

class main:
    def __init__(self):
        pygame.init()
        pygame.display.init()

        pygame.display.gl_set_attribute(pygame.GL_ACCELERATED_VISUAL, 0)
        pygame.display.gl_set_attribute(pygame.GL_DOUBLEBUFFER, 1)

        self.windowWidth = 1500
        self.windowHeight = 1500

        self.screen = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.RESIZABLE | pygame.GL_DOUBLEBUFFER)
        pygame.display.set_caption("Rubik`s Cube Solver by David Derflinger")

        self.clock = pygame.time.Clock()
        self.running = True

        self.solver = RubiksCubeSolver.RubiksCubeSolver()

        self.run()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Quit the Game
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:  # Quit the Game
                        self.running = False

            self.screen.fill((50, 50, 50))

            # draw cube
            cube = self.solver.generateComplete()
            for i in range(len(cube)):
                for j in range(len(cube[0])):
                    if cube[i][j] != -1:
                        color = (0, 0, 0)
                        width = 100
                        height = 100
                        x = 10 + (j * (width + 1))
                        y = 10 + (i * (height + 1))

                        match cube[i][j]:
                            case 1: # white
                                color = (255,255,255)
                            case 2: # blue
                                color = (0, 255, 0)
                            case 3: # yellow
                                color = (255,255,0)
                            case 4: # green
                                color = (0, 0, 255)
                            case 5: # orange
                                color = (255, 165, 0)
                            case 6: # red
                                color = (255, 0 ,0)

                        pygame.draw.rect(self.screen, color, (x, y, width, height))









            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    main()
