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
        self.invertedMove = False
        self.middelMoves = False

        self.menu = "main"
        self.spacePressed = False

        self.run()

    def run(self):
        #self.solver.top[0][0] = 2
        #self.solver.top[0][1] = 2
        #self.solver.top[2][0] = 6
        #self.solver.top[1][0] = 6
        #self.solver.top[2][2] = 3
        #self.solver.top[2][1] = 3
        #self.solver.top[0][2] = 4
        #self.solver.top[1][2] = 4

        #self.solver.bottom[0][0] = 2
        #self.solver.bottom[0][1] = 2
        #self.solver.bottom[2][0] = 6
        #self.solver.bottom[1][0] = 6
        #self.solver.bottom[2][2] = 3
        #self.solver.bottom[2][1] = 3
        #self.solver.bottom[0][2] = 4
        #self.solver.bottom[1][2] = 4
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Quit the Game
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:  # Quit the Game
                        self.running = False
                    elif event.key == pygame.K_s:
                        self.solver.solve()
                    elif event.key == pygame.K_w:
                        self.invertedMove = not self.invertedMove
                    elif event.key == pygame.K_e:
                        self.middelMoves = not self.middelMoves
                    elif event.key == pygame.K_1:
                        if not self.middelMoves:
                            self.solver.makeMove("U" + ("'" if self.invertedMove else ""))
                        else:
                            self.solver.makeMove("u" + ("'" if self.invertedMove else ""))
                    elif event.key == pygame.K_2:
                        if not self.middelMoves:
                            self.solver.makeMove("D" + ("'" if self.invertedMove else ""))
                        else:
                            self.solver.makeMove("d" + ("'" if self.invertedMove else ""))
                    elif event.key == pygame.K_3:
                        if not self.middelMoves:
                            self.solver.makeMove("F" + ("'" if self.invertedMove else ""))
                        else:
                            self.solver.makeMove("f" + ("'" if self.invertedMove else ""))
                    elif event.key == pygame.K_4:
                        if not self.middelMoves:
                            self.solver.makeMove("B" + ("'" if self.invertedMove else ""))
                        else:
                            self.solver.makeMove("b" + ("'" if self.invertedMove else ""))
                    elif event.key == pygame.K_5:
                        if not self.middelMoves:
                            self.solver.makeMove("L" + ("'" if self.invertedMove else ""))
                        else:
                            self.solver.makeMove("l" + ("'" if self.invertedMove else ""))
                    elif event.key == pygame.K_6:
                        if not self.middelMoves:
                            self.solver.makeMove("R" + ("'" if self.invertedMove else ""))
                        else:
                            self.solver.makeMove("r" + ("'" if self.invertedMove else ""))
                    elif event.key == pygame.K_7:
                        self.solver.makeMove("M" + ("'" if self.invertedMove else ""))
                    elif event.key == pygame.K_SPACE:
                        self.spacePressed = True
                    elif event.key == pygame.K_n:
                        self.menu = "main"
                    elif event.key == pygame.K_m:
                        self.menu = "customScramble"
                    elif event.key == pygame.K_q:
                        self.solver.reset()

            self.windowWidth = self.screen.get_width()
            self.windowHeight = self.screen.get_height()

            self.screen.fill((50, 50, 50))

            unscaledSize = 30
            if self.windowWidth < self.windowHeight:
                textSize = int((unscaledSize * self.windowWidth) / 2000)  # scale text size
                width = (100 * self.windowWidth) / 2000
            else:
                textSize = int((unscaledSize * self.windowHeight) / 2000)  # scale text size
                width = (100 * self.windowHeight) / 2000

            match self.menu:
                case "main":
                    if self.spacePressed:
                        self.solver.generateScramble()
                        self.spacePressed = not self.spacePressed


                    font = pygame.font.Font(pygame.font.get_default_font(), textSize)

                    scrambleMoves = ""
                    first = True
                    for move in self.solver.scrambleMoves:
                        if first:
                            scrambleMoves += str(move)
                            first = False
                        else:
                            scrambleMoves += " ," + str(move)

                    displayedText = []
                    displayedText.append("Scramble: " + scrambleMoves)

                    displayedText.append("Solve (" + str(len(self.solver.solveMoves)) + "):")

                    solveMoves = ""
                    first = True
                    count = 0
                    for move in self.solver.solveMoves:
                        count += 1

                        if first:
                            solveMoves += str(move)
                            first = False
                        else:
                            solveMoves += " ," + str(move)

                        if count == 30:
                            count = 0
                            displayedText.append(solveMoves)
                            solveMoves = ""
                            first = True
                    displayedText.append(solveMoves)

                    displayedText.append("simplifiedMoves (" + str(len(self.solver.simplifySolve())) + "):")

                    simplifiedMoves = ""
                    first = True
                    count = 0
                    for move in self.solver.simplifySolve():
                        count += 1
                        if first:
                            simplifiedMoves += str(move)
                            first = False
                        else:
                            simplifiedMoves += " ," + str(move)

                        if count == 30:
                            count = 0
                            displayedText.append(simplifiedMoves)
                            simplifiedMoves = ""
                            first = True
                    displayedText.append(simplifiedMoves)

                    for i in range(len(displayedText)):
                        text = font.render(displayedText[i], True, (255,255,255))
                        newRect = text.get_rect()
                        newRect.x = 10
                        newRect.y = (((10 * self.windowHeight) / 900) + textSize * i + textSize * i / 2) + (12*width) + 10
                        self.screen.blit(text, newRect)

                    self.drawCube(width)

                case "customScramble":
                    if self.spacePressed:
                        self.solver.solve()
                        self.spacePressed = not self.spacePressed

                    self.drawCube(width)





            pygame.display.flip()
            self.clock.tick(60)

    def drawCube(self, width):
        # draw cube
        cube = self.solver.generateComplete()
        for i in range(len(cube)):
            for j in range(len(cube[0])):
                if cube[i][j] != -1:
                    color = (0, 0, 0)

                    height = width
                    x = 10 + (j * (width + 1))
                    y = 10 + (i * (height + 1))

                    match cube[i][j]:
                        case 1:  # white
                            color = (255, 255, 255)
                        case 2:  # blue
                            color = (0, 0, 255)
                        case 3:  # yellow
                            color = (255, 255, 0)
                        case 4:  # green
                            color = (0, 255, 0)
                        case 5:  # red
                            color = (255, 0, 0)
                        case 6:  # orange
                            color = (255, 165, 0)

                    pygame.draw.rect(self.screen, color, (x, y, width, height))

if __name__ == "__main__":
    main()
