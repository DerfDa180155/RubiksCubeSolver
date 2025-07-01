import pygame

import RubiksCubeSolver
import Button


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

        self.menuButtons = []
        self.createMenuButtons()

        self.customScrambleButtons = []
        self.createScrambleButtons()

        self.run()

    def run(self):
        oldMousePressed = pygame.mouse.get_pressed()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Quit the Game
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:  # Quit the Game
                        if self.menu == "main":
                            self.running = False
                        else:
                            self.menu = "main"
                    elif event.key == pygame.K_s and self.menu == "main":
                        self.solver.solve()
                    elif event.key == pygame.K_w:
                        self.invertedMove = not self.invertedMove
                    elif event.key == pygame.K_e:
                        self.middelMoves = not self.middelMoves
                    elif event.key == pygame.K_u:
                        if not self.middelMoves:
                            self.solver.makeMove("U" + ("'" if self.invertedMove else ""), True)
                        else:
                            self.solver.makeMove("u" + ("'" if self.invertedMove else ""), True)
                    elif event.key == pygame.K_d:
                        if not self.middelMoves:
                            self.solver.makeMove("D" + ("'" if self.invertedMove else ""), True)
                        else:
                            self.solver.makeMove("d" + ("'" if self.invertedMove else ""), True)
                    elif event.key == pygame.K_f:
                        if not self.middelMoves:
                            self.solver.makeMove("F" + ("'" if self.invertedMove else ""), True)
                        else:
                            self.solver.makeMove("f" + ("'" if self.invertedMove else ""), True)
                    elif event.key == pygame.K_b:
                        if not self.middelMoves:
                            self.solver.makeMove("B" + ("'" if self.invertedMove else ""), True)
                        else:
                            self.solver.makeMove("b" + ("'" if self.invertedMove else ""), True)
                    elif event.key == pygame.K_l:
                        if not self.middelMoves:
                            self.solver.makeMove("L" + ("'" if self.invertedMove else ""), True)
                        else:
                            self.solver.makeMove("l" + ("'" if self.invertedMove else ""), True)
                    elif event.key == pygame.K_r:
                        if not self.middelMoves:
                            self.solver.makeMove("R" + ("'" if self.invertedMove else ""), True)
                        else:
                            self.solver.makeMove("r" + ("'" if self.invertedMove else ""), True)
                    elif event.key == pygame.K_a:
                        self.solver.addRandomMove()
                    elif event.key == pygame.K_s:
                        self.solver.removeLastMove()
                    elif event.key == pygame.K_1:
                        self.solver.makeMove("M" + ("'" if self.invertedMove else ""), True)
                    elif event.key == pygame.K_SPACE:
                        self.spacePressed = True
                    elif event.key == pygame.K_n:
                        self.menu = "main"
                    elif event.key == pygame.K_m:
                        self.menu = "customScramble"
                        self.solver.reset()
                    elif event.key == pygame.K_q:
                        self.solver.reset()

            self.windowWidth = self.screen.get_width()
            self.windowHeight = self.screen.get_height()

            self.screen.fill((50, 50, 50))

            mx, my = pygame.mouse.get_pos()
            mousePressed = pygame.mouse.get_pressed()
            mousePressedUp = []
            mousePressedDown = []
            for i in range(len(mousePressed)):
                mousePressedUp.append(not mousePressed[i] and oldMousePressed[i])
                mousePressedDown.append(mousePressed[i] and not oldMousePressed[i])

            oldMousePressed = mousePressed

            unscaledSize = 30
            if self.menu == "main":
                unscaledSize = 50

            if self.windowWidth < self.windowHeight:
                textSize = int((unscaledSize * self.windowWidth) / 2000)  # scale text size
                width = (100 * self.windowWidth) / 2000
                startMenuSize = (130 * self.windowWidth) / 2000
            else:
                textSize = int((unscaledSize * self.windowHeight) / 2000)  # scale text size
                width = (100 * self.windowHeight) / 2000
                startMenuSize = (130 * self.windowHeight) / 2000

            if self.menu != "main":
                font = pygame.font.Font(pygame.font.get_default_font(), textSize)

                text = font.render(self.menu, True, (255, 255, 255))
                newRect = text.get_rect()
                newRect.centerx = self.windowWidth/2
                newRect.y = textSize * 0.5
                self.screen.blit(text, newRect)

            match self.menu:
                case "main":
                    centerX = self.windowWidth / 2
                    centerY = self.windowHeight / 1.9

                    font = pygame.font.Font(pygame.font.get_default_font(), textSize)

                    text = font.render("Rubiks Cube Solver", True, (255, 255, 255))
                    newRect = text.get_rect()
                    newRect.centerx = self.windowWidth / 2
                    newRect.y = textSize
                    self.screen.blit(text, newRect)

                    # draw cube
                    #self.drawCube(startMenuSize, centerX, centerY, True, True)

                    self.updateMenuButtons(width)

                    for button in self.menuButtons:
                        button.hover(mx, my)
                        button.clicked(mx, my, mousePressedUp)
                        button.update()
                        button.draw()

                        if button.isClicked:
                            for tempbutton in self.menuButtons:
                                tempbutton.reset()
                            self.menu = button.onClick

                case "customScramble":
                    if self.spacePressed:
                        self.solver.solve()
                        self.spacePressed = not self.spacePressed
                        self.menu = "solved"

                    centerX = self.windowWidth/2
                    centerY = self.windowHeight/2
                    #self.drawCube(width, centerX, 100, True)

                    displayedText = []
                    scrambleMoves = ""
                    first = True
                    for move in self.solver.scrambleMoves:
                        if first:
                            scrambleMoves += str(move)
                            first = False
                        else:
                            scrambleMoves += " ," + str(move)
                    displayedText.append("Scramble: " + scrambleMoves)

                    for i in range(len(displayedText)):
                        text = font.render(displayedText[i], True, (255, 255, 255))
                        newRect = text.get_rect()
                        newRect.x = 10
                        newRect.y = (((10 * self.windowHeight) / 900) + textSize * i + textSize * i / 2) + (14 * width) + 10
                        self.screen.blit(text, newRect)


                    displayedText = ["U - Up", "D - Down", "R - Right", "L - Left", "F - Front", "B - Back", "W - X'", "E - x", "A - Random", "S - Remove", "SPACE - Solve", "Q - Reset"]

                    for i in range(len(displayedText)):
                        text = font.render(displayedText[i], True, (255, 255, 255))
                        newRect = text.get_rect()
                        newRect.x = centerX*1.6
                        newRect.y = (((20 * self.windowHeight) / 900) + textSize * i + textSize * i / 2) + 10
                        self.screen.blit(text, newRect)

                    self.updateCustomScrambleButtons(width)

                    for button in self.customScrambleButtons:
                        button.hover(mx, my)
                        button.clicked(mx, my, mousePressedUp)
                        button.update()
                        button.draw()

                        if button.isClicked:
                            for tempbutton in self.customScrambleButtons:
                                tempbutton.reset()
                            self.menu = button.onClick

                case "solved":
                    if self.spacePressed:
                        self.solver.generateScramble()
                        self.spacePressed = not self.spacePressed

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

                        if count == 20:
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

                        if count == 20:
                            count = 0
                            displayedText.append(simplifiedMoves)
                            simplifiedMoves = ""
                            first = True
                    displayedText.append(simplifiedMoves)

                    centerX = self.windowWidth / 4
                    for i in range(len(displayedText)):
                        text = font.render(displayedText[i], True, (255, 255, 255))
                        newRect = text.get_rect()
                        newRect.x = centerX * 2.2
                        newRect.y = (((10 * self.windowHeight) / 900) + textSize * i + textSize * i / 2) + (1 * width) + 10
                        self.screen.blit(text, newRect)

                    self.drawCube(width, centerX, 100, True)

            pygame.display.flip()
            self.clock.tick(60)

    def drawCube(self, width, posX, posY, centerX=False, centerY=False):
        # draw cube
        cube = self.solver.generateComplete()
        for i in range(len(cube)):
            for j in range(len(cube[0])):
                if cube[i][j] != -1:
                    color = (0, 0, 0)

                    height = width
                    x = (j * (width + 1)) + posX
                    y = (i * (height + 1)) + posY

                    if centerX:
                        x += -(width*4.5)
                    if centerY:
                        y += -(height*6)

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

    def createMenuButtons(self):
        cube = self.solver.generateComplete()
        for i in range(len(cube)):
            for j in range(len(cube[0])):
                if cube[i][j] != -1:
                    color = (0, 0, 0)

                    width = (50*self.windowWidth)/1000
                    height = width
                    x = (j * (width + 10)) + (self.windowWidth/2) - width / 2
                    y = (i * (height + 10)) + (self.windowHeight/2) - height / 2

                    x += -(width * 4.5)
                    y += -(height * 6)

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

                    self.menuButtons.append(Button.Button(self.screen, x, y, width, height, color, "customScramble"))

    def createScrambleButtons(self):
        counter = 0
        onclickArray = ["top","top","top","top","top","top","top","top","top","left","left","left","front","front","front","right","right","right","left","left","left","front","front","front","right","right","right","left","left","left","front","front","front","right","right","right","bottom","bottom","bottom","bottom","bottom","bottom","bottom","bottom","bottom","back","back","back","back","back","back","back","back","back"]
        cube = self.solver.generateComplete()
        for i in range(len(cube)):
            for j in range(len(cube[0])):
                if cube[i][j] != -1:
                    color = (0, 0, 0)

                    width = (50*self.windowWidth)/1000
                    height = width
                    x = (j * (width + 10)) + (self.windowWidth/2) - width / 2
                    y = (i * (height + 10)) + (self.windowHeight/2) - height / 2

                    x += -(width * 4.5)
                    y += -(height * 6)

                    onClick = onclickArray[counter]
                    counter = counter + 1

                    match cube[i][j]:
                        case 1: # white
                            color = (255, 255, 255)
                        case 2: # blue
                            color = (0, 0, 255)
                        case 3: # yellow
                            color = (255, 255, 0)
                        case 4: # green
                            color = (0, 255, 0)
                        case 5: # red
                            color = (255, 0, 0)
                        case 6: # orange
                            color = (255, 165, 0)

                    self.customScrambleButtons.append(Button.Button(self.screen, x, y, width, height, color, onClick))

    def updateMenuButtons(self, width):
        counter = 0
        cube = self.solver.generateComplete()
        for i in range(len(cube)):
            for j in range(len(cube[0])):
                if cube[i][j] != -1:
                    height = width
                    x = (j * (width + 10)) + (self.windowWidth / 2) - width / 2
                    y = (i * (height + 10)) + (self.windowHeight / 2) - height / 2

                    x += -(width * 4.5)
                    y += -(height * 6)

                    self.menuButtons[counter].updateLocationAndSize(x, y, width, height)
                    counter += 1

    def updateCustomScrambleButtons(self, width):
        counter = 0
        cube = self.solver.generateComplete()
        for i in range(len(cube)):
            for j in range(len(cube[0])):
                if cube[i][j] != -1:
                    height = width
                    x = (j * (width + 10)) + (self.windowWidth / 2) - width / 2
                    y = (i * (height + 10)) + (self.windowHeight / 2) - height / 2

                    x += -(width * 4.5)
                    y += -(height * 6)

                    self.customScrambleButtons[counter].updateLocationAndSize(x, y, width, height)
                    counter += 1


if __name__ == "__main__":
    main()
