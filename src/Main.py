import random

import pygame
import webbrowser

import RubiksCubeSolver
import Button
import RotatedRect
import SwitchButton

class main:
    def __init__(self):
        pygame.init()
        pygame.display.init()

        pygame.display.gl_set_attribute(pygame.GL_ACCELERATED_VISUAL, 0)
        pygame.display.gl_set_attribute(pygame.GL_DOUBLEBUFFER, 1)

        self.windowWidth = 1500
        self.windowHeight = 1500

        self.author = "David Derflinger"

        # todo maybe resizeable entfernen und durch setting mit so 4 größen ersetzen oder einfach nur eine größe festlegen
        self.screen = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.RESIZABLE | pygame.GL_DOUBLEBUFFER)
        pygame.display.set_caption("Rubik`s Cube Solver by " + self.author)

        self.clock = pygame.time.Clock()
        self.running = True

        self.solver = RubiksCubeSolver.RubiksCubeSolver()
        self.invertedMove = False
        self.middelMoves = False

        self.menu = "main"
        self.spacePressed = False

        # background cubes
        self.availableColors = [(255, 255, 255), (0, 0, 255), (255, 255, 0), (0, 255, 0), (180, 0, 0), (255, 165, 0)]
        self.backgroundCubes = []
        self.generateBackgroundCubes()

        # buttons
        self.mainButtons = [Button.Button(self.screen, 250, 250, 1000, 200, (100, 100, 100), "Enter your Cube"),
                            Button.Button(self.screen, 250, 600, 1000, 200, (100, 100, 100), "Custom Scramble"),
                            Button.Button(self.screen, 250, 950, 400, 200, (100, 100, 100), "About"),
                            Button.Button(self.screen, 850, 950, 400, 200, (100, 100, 100), "GitHub Page")]
        self.aboutButtons = [Button.Button(self.screen, 250, 1100, 1000, 200, (100, 100, 100), "Back")]

        self.enterYourCubeButtons = [Button.Button(self.screen, 50, 50, 100, 50, (100, 100, 100), "Back"),
                                     Button.Button(self.screen, 1300, 150, 100, 100, (255, 255, 255), "SelectWhite"),
                                     Button.Button(self.screen, 1300, 300, 100, 100, (0, 0, 255), "SelectBlue"),
                                     Button.Button(self.screen, 1300, 450, 100, 100, (255, 255, 0), "SelectYellow"),
                                     Button.Button(self.screen, 1300, 600, 100, 100, (0, 255, 0), "SelectGreen"),
                                     Button.Button(self.screen, 1300, 750, 100, 100, (255, 0, 0), "SelectRed"),
                                     Button.Button(self.screen, 1300, 900, 100, 100, (255, 165, 0), "SelectOrange"),
                                     Button.Button(self.screen, 1250, 1050, 200, 80, (100, 100, 100), "Clear Cube"),
                                     Button.Button(self.screen, 1250, 1180, 200, 80, (100, 100, 100), "Solve")]
        self.enterYourCubeSwitchButtons = [SwitchButton.SwitchButton(self.screen, 50, 150, 100, 50, (100, 100, 100), "2D", "3D")]

        self.enterYourCubeSelectedButton = self.enterYourCubeButtons[1]
        self.enterYourCubeSelectedButton.selected = True

        self.customScrambleButtons = [Button.Button(self.screen, 50, 50, 100, 50, (100, 100, 100), "Back"),
                                      Button.Button(self.screen, 1200, 950, 200, 80, (100, 100, 100), "Reset"),
                                      Button.Button(self.screen, 1200, 1070, 200, 80, (100, 100, 100), "Solve")]
        self.customScrambleCubeButtons = []
        self.customScrambleSwitchButtons = [SwitchButton.SwitchButton(self.screen, 50, 150, 100, 50, (100, 100, 100), "2D", "3D")]

        self.createScrambleButtons()

        self.run()

    def run(self):
        oldMousePressed = pygame.mouse.get_pressed()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # Quit the Game
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE: # Quit the Game
                        if self.menu == "main":
                            self.running = False
                        else:
                            self.menu = "main"
                    elif event.key == pygame.K_w and self.menu == "custom_scramble":
                        self.invertedMove = not self.invertedMove
                    elif event.key == pygame.K_e and self.menu == "custom_scramble":
                        self.middelMoves = not self.middelMoves
                    elif event.key == pygame.K_u and self.menu == "custom_scramble":
                        if not self.middelMoves:
                            self.solver.makeMove("U" + ("'" if self.invertedMove else ""), True)
                        else:
                            self.solver.makeMove("u" + ("'" if self.invertedMove else ""), True)
                    elif event.key == pygame.K_d and self.menu == "custom_scramble":
                        if not self.middelMoves:
                            self.solver.makeMove("D" + ("'" if self.invertedMove else ""), True)
                        else:
                            self.solver.makeMove("d" + ("'" if self.invertedMove else ""), True)
                    elif event.key == pygame.K_f and self.menu == "custom_scramble":
                        if not self.middelMoves:
                            self.solver.makeMove("F" + ("'" if self.invertedMove else ""), True)
                        else:
                            self.solver.makeMove("f" + ("'" if self.invertedMove else ""), True)
                    elif event.key == pygame.K_b and self.menu == "custom_scramble":
                        if not self.middelMoves:
                            self.solver.makeMove("B" + ("'" if self.invertedMove else ""), True)
                        else:
                            self.solver.makeMove("b" + ("'" if self.invertedMove else ""), True)
                    elif event.key == pygame.K_l and self.menu == "custom_scramble":
                        if not self.middelMoves:
                            self.solver.makeMove("L" + ("'" if self.invertedMove else ""), True)
                        else:
                            self.solver.makeMove("l" + ("'" if self.invertedMove else ""), True)
                    elif event.key == pygame.K_r and self.menu == "custom_scramble":
                        if not self.middelMoves:
                            self.solver.makeMove("R" + ("'" if self.invertedMove else ""), True)
                        else:
                            self.solver.makeMove("r" + ("'" if self.invertedMove else ""), True)
                    elif event.key == pygame.K_a and self.menu == "custom_scramble":
                        self.solver.addRandomMove()
                    elif event.key == pygame.K_s and self.menu == "custom_scramble":
                        self.solver.removeLastMove()
                    elif event.key == pygame.K_1 and self.menu == "custom_scramble":
                        self.solver.makeMove("M" + ("'" if self.invertedMove else ""), True)
                    elif event.key == pygame.K_SPACE and self.menu == "custom_scramble":
                        self.spacePressed = True
                    elif event.key == pygame.K_n and self.menu == "custom_scramble":
                        self.menu = "main"
                    elif event.key == pygame.K_q and self.menu == "custom_scramble":
                        self.solver.reset()

            self.windowWidth = self.screen.get_width()
            self.windowHeight = self.screen.get_height()
            centerX = self.windowWidth / 2
            centerY = self.windowHeight / 2

            self.screen.fill((50, 50, 50))

            # detect mouse press and release
            mx, my = pygame.mouse.get_pos()
            mousePressed = pygame.mouse.get_pressed()
            mousePressedUp = []
            mousePressedDown = []
            for i in range(len(mousePressed)):
                mousePressedUp.append(not mousePressed[i] and oldMousePressed[i])
                mousePressedDown.append(mousePressed[i] and not oldMousePressed[i])

            oldMousePressed = mousePressed

            # remove last move with mouse wheel click
            if self.menu == "customScramble" and mousePressedDown[1]:
                self.solver.removeLastMove()

            unscaledSize = 70

            if self.windowWidth < self.windowHeight:
                headingTextSize = int((unscaledSize * self.windowWidth) / 2000) # scale text size
                textSize = int(((unscaledSize-30) * self.windowWidth) / 2000)
                width = (100 * self.windowWidth) / 2000
                startMenuSize = (130 * self.windowWidth) / 2000
            else:
                headingTextSize = int((unscaledSize * self.windowHeight) / 2000) # scale text size
                textSize = int(((unscaledSize-30) * self.windowHeight) / 2000)
                width = (100 * self.windowHeight) / 2000
                startMenuSize = (130 * self.windowHeight) / 2000

            headingFont = pygame.font.Font(pygame.font.get_default_font(), headingTextSize)
            smallerFont = pygame.font.Font(pygame.font.get_default_font(), textSize)


            # draw background cubes
            if self.menu in ["main", "about"]:
                # draw background cubes
                for cube in self.backgroundCubes:
                    cube.draw()

            # draw copyright and version
            if self.menu in ["main", "about", "enter_your_scramble", "custom_scramble"]:
                # draw copyright
                text = smallerFont.render("\u00A9 2026 " + self.author, True, (150, 150, 150))
                newRect = text.get_rect()
                newRect.left = 20
                newRect.bottom = self.windowHeight - 5
                self.screen.blit(text, newRect)

                # draw version
                text = smallerFont.render("V1.0.0", True, (150, 150, 150))
                newRect = text.get_rect()
                newRect.right = self.windowWidth - 20
                newRect.bottom = self.windowHeight - 5
                self.screen.blit(text, newRect)

            match self.menu:
                case "main":
                    # draw headline
                    text = headingFont.render("Rubiks Cube Solver", True, (255, 255, 255))
                    newRect = text.get_rect()
                    newRect.centerx = self.windowWidth / 2
                    newRect.y = headingTextSize
                    self.screen.blit(text, newRect)

                    # buttons
                    for button in self.mainButtons:
                        button.update()
                        button.draw(drawOnClickText=True, onClickTextSize=50)
                        if button.clicked(mx, my, mousePressedUp):
                            match button.onClick:
                                case "Enter your Cube":
                                    self.solver.cleanCube()
                                    self.menu = "enter_your_scramble"
                                case "Custom Scramble":
                                    self.solver.fillCube()
                                    self.menu = "custom_scramble"
                                case "About":
                                    self.menu = "about"
                                case "GitHub Page":
                                    webbrowser.open_new_tab("https://github.com/DerfDa180155/RubiksCubeSolver")

                case "about":
                    # draw headline
                    text = headingFont.render("About this project", True, (255, 255, 255))
                    newRect = text.get_rect()
                    newRect.centerx = self.windowWidth / 2
                    newRect.y = headingTextSize
                    self.screen.blit(text, newRect)

                    # draw text
                    lines = [
                        "A 3x3 Rubik's Cube Solver.",
                        "You can either enter the colors of all",
                        "the sides or enter your scramble.",
                        "The solver then generates the solution",
                        "moves using the CFOP method."
                    ]

                    start_y = (self.windowHeight / 2) - headingTextSize * 1.5 * 3

                    for i in range(len(lines)):
                        text = headingFont.render(lines[i], True, (255, 255, 255))
                        rect = text.get_rect()
                        rect.centerx = self.windowWidth / 2
                        rect.centery = start_y + i * headingTextSize * 1.5
                        self.screen.blit(text, rect)

                    # buttons
                    for button in self.aboutButtons:
                        button.update()
                        button.draw(drawOnClickText=True, onClickTextSize=70)
                        if button.clicked(mx, my, mousePressedUp):
                            match button.onClick:
                                case "Back":
                                    self.menu = "main"

                case "enter_your_scramble":
                    # draw headline
                    text = headingFont.render("Enter your scramble", True, (255, 255, 255))
                    newRect = text.get_rect()
                    newRect.centerx = self.windowWidth / 2
                    newRect.y = headingTextSize
                    self.screen.blit(text, newRect)

                    cubeStyle = self.enterYourCubeSwitchButtons[0].action

                    if cubeStyle == "2D":
                        # 2D
                        cubeRects = self.drawCube(80, self.windowWidth/2, 150, True)

                        placeColor = 0
                        match self.enterYourCubeSelectedButton.onClick:
                            case "SelectWhite":
                                placeColor = 1
                            case "SelectBlue":
                                placeColor = 2
                            case "SelectYellow":
                                placeColor = 3
                            case "SelectGreen":
                                placeColor = 4
                            case "SelectRed":
                                placeColor = 5
                            case "SelectOrange":
                                placeColor = 6

                        counter = 0
                        for rect in cubeRects:
                            if rect.collidepoint(mx, my) and counter not in [4, 19, 22, 25, 40, 49]:
                                if mousePressedUp[0]:
                                    match counter:
                                        case 0:
                                            self.solver.top[0][0] = placeColor
                                        case 1:
                                            self.solver.top[1][0] = placeColor
                                        case 2:
                                            self.solver.top[2][0] = placeColor
                                        case 3:
                                            self.solver.top[0][1] = placeColor
                                        case 4:
                                            self.solver.top[1][1] = placeColor
                                        case 5:
                                            self.solver.top[2][1] = placeColor
                                        case 6:
                                            self.solver.top[0][2] = placeColor
                                        case 7:
                                            self.solver.top[1][2] = placeColor
                                        case 8:
                                            self.solver.top[2][2] = placeColor

                                        case 9:
                                            self.solver.left[0][0] = placeColor
                                        case 10:
                                            self.solver.left[1][0] = placeColor
                                        case 11:
                                            self.solver.left[2][0] = placeColor

                                        case 12:
                                            self.solver.front[0][0] = placeColor
                                        case 13:
                                            self.solver.front[1][0] = placeColor
                                        case 14:
                                            self.solver.front[2][0] = placeColor

                                        case 15:
                                            self.solver.right[0][0] = placeColor
                                        case 16:
                                            self.solver.right[1][0] = placeColor
                                        case 17:
                                            self.solver.right[2][0] = placeColor

                                        case 18:
                                            self.solver.left[0][1] = placeColor
                                        case 19:
                                            self.solver.left[1][1] = placeColor
                                        case 20:
                                            self.solver.left[2][1] = placeColor

                                        case 21:
                                            self.solver.front[0][1] = placeColor
                                        case 22:
                                            self.solver.front[1][1] = placeColor
                                        case 23:
                                            self.solver.front[2][1] = placeColor

                                        case 24:
                                            self.solver.right[0][1] = placeColor
                                        case 25:
                                            self.solver.right[1][1] = placeColor
                                        case 26:
                                            self.solver.right[2][1] = placeColor

                                        case 27:
                                            self.solver.left[0][2] = placeColor
                                        case 28:
                                            self.solver.left[1][2] = placeColor
                                        case 29:
                                            self.solver.left[2][2] = placeColor

                                        case 30:
                                            self.solver.front[0][2] = placeColor
                                        case 31:
                                            self.solver.front[1][2] = placeColor
                                        case 32:
                                            self.solver.front[2][2] = placeColor

                                        case 33:
                                            self.solver.right[0][2] = placeColor
                                        case 34:
                                            self.solver.right[1][2] = placeColor
                                        case 35:
                                            self.solver.right[2][2] = placeColor

                                        case 36:
                                            self.solver.bottom[0][0] = placeColor
                                        case 37:
                                            self.solver.bottom[1][0] = placeColor
                                        case 38:
                                            self.solver.bottom[2][0] = placeColor
                                        case 39:
                                            self.solver.bottom[0][1] = placeColor
                                        case 40:
                                            self.solver.bottom[1][1] = placeColor
                                        case 41:
                                            self.solver.bottom[2][1] = placeColor
                                        case 42:
                                            self.solver.bottom[0][2] = placeColor
                                        case 43:
                                            self.solver.bottom[1][2] = placeColor
                                        case 44:
                                            self.solver.bottom[2][2] = placeColor

                                        case 45:
                                            self.solver.back[0][0] = placeColor
                                        case 46:
                                            self.solver.back[1][0] = placeColor
                                        case 47:
                                            self.solver.back[2][0] = placeColor
                                        case 48:
                                            self.solver.back[0][1] = placeColor
                                        case 49:
                                            self.solver.back[1][1] = placeColor
                                        case 50:
                                            self.solver.back[2][1] = placeColor
                                        case 51:
                                            self.solver.back[0][2] = placeColor
                                        case 52:
                                            self.solver.back[1][2] = placeColor
                                        case 53:
                                            self.solver.back[2][2] = placeColor

                            counter += 1

                    else:
                        # 3D
                        text = headingFont.render("Comming soon ...", True, (255, 255, 255))
                        newRect = text.get_rect()
                        newRect.centerx = self.windowWidth/2
                        newRect.centery = self.windowHeight/2
                        self.screen.blit(text, newRect)

                    # display solve moves
                    displayedText = []
                    displayedText.append("Solve moves (" + str(len(self.solver.simplifySolve())) + "):")

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

                        if count == 25:
                            count = 0
                            displayedText.append(simplifiedMoves)
                            simplifiedMoves = ""
                            first = True
                    displayedText.append(simplifiedMoves)

                    for i in range(len(displayedText)):
                        text = smallerFont.render(displayedText[i], True, (255, 255, 255))
                        newRect = text.get_rect()
                        newRect.x = 20
                        newRect.y = 1200 + textSize * i
                        self.screen.blit(text, newRect)


                    for button in self.enterYourCubeButtons:
                        button.update()
                        button.draw(drawOnClickText=not "Select" in button.onClick, onClickTextSize=25)
                        if button.clicked(mx, my, mousePressedUp):
                            if "Select" in button.onClick:
                                self.enterYourCubeSelectedButton.selected = False
                                self.enterYourCubeSelectedButton = button
                                self.enterYourCubeSelectedButton.selected = True

                            match button.onClick:
                                case "Back":
                                    self.menu = "main"
                                case "Clear Cube":
                                    self.solver.cleanCube()
                                case "Solve":
                                    if self.solver.isFullCube():
                                        self.solver.solve()
                                        self.solver.simplifySolve()

                    for switchButton in self.enterYourCubeSwitchButtons:
                        switchButton.draw((20, 20, 20), (128, 255, 128))
                        switchButton.clicked(mx, my, mousePressedUp)

                case "custom_scramble":
                    # draw headline
                    text = headingFont.render("Custom scramble", True, (255, 255, 255))
                    newRect = text.get_rect()
                    newRect.centerx = self.windowWidth / 2
                    newRect.y = headingTextSize
                    self.screen.blit(text, newRect)

                    # space for solve
                    if self.spacePressed:
                        self.solver.solve()
                        self.spacePressed = not self.spacePressed
                        #self.menu = "solve" # no longer needed

                    # display hotkeys
                    displayedText = ["U - Up", "D - Down", "R - Right", "L - Left", "F - Front", "B - Back", "W - X'",
                                     "E - x", "A - Random", "S - Remove", "SPACE - Solve", "Q - Reset"]

                    for i in range(len(displayedText)):
                        text = smallerFont.render(displayedText[i], True, (255, 255, 255))
                        newRect = text.get_rect()
                        newRect.x = centerX * 1.6
                        newRect.y = (150 + textSize * i + textSize * i / 2)
                        self.screen.blit(text, newRect)


                    cubeStyle = self.customScrambleSwitchButtons[0].action

                    if cubeStyle == "2D":
                        self.updateCustomScrambleButtons(75)

                        buttongroups = []
                        buttongroups.append(
                            [self.customScrambleCubeButtons[0], self.customScrambleCubeButtons[1],
                             self.customScrambleCubeButtons[2],
                             self.customScrambleCubeButtons[3], self.customScrambleCubeButtons[4],
                             self.customScrambleCubeButtons[5],
                             self.customScrambleCubeButtons[6], self.customScrambleCubeButtons[7],
                             self.customScrambleCubeButtons[8]])
                        buttongroups.append(
                            [self.customScrambleCubeButtons[9], self.customScrambleCubeButtons[10],
                             self.customScrambleCubeButtons[11],
                             self.customScrambleCubeButtons[18], self.customScrambleCubeButtons[19],
                             self.customScrambleCubeButtons[20],
                             self.customScrambleCubeButtons[27], self.customScrambleCubeButtons[28],
                             self.customScrambleCubeButtons[29]])
                        buttongroups.append(
                            [self.customScrambleCubeButtons[12], self.customScrambleCubeButtons[13],
                             self.customScrambleCubeButtons[14],
                             self.customScrambleCubeButtons[21], self.customScrambleCubeButtons[22],
                             self.customScrambleCubeButtons[23],
                             self.customScrambleCubeButtons[30], self.customScrambleCubeButtons[31],
                             self.customScrambleCubeButtons[32]])
                        buttongroups.append(
                            [self.customScrambleCubeButtons[15], self.customScrambleCubeButtons[16],
                             self.customScrambleCubeButtons[17],
                             self.customScrambleCubeButtons[24], self.customScrambleCubeButtons[25],
                             self.customScrambleCubeButtons[26],
                             self.customScrambleCubeButtons[33], self.customScrambleCubeButtons[34],
                             self.customScrambleCubeButtons[35]])
                        buttongroups.append(
                            [self.customScrambleCubeButtons[36], self.customScrambleCubeButtons[37],
                             self.customScrambleCubeButtons[38],
                             self.customScrambleCubeButtons[39], self.customScrambleCubeButtons[40],
                             self.customScrambleCubeButtons[41],
                             self.customScrambleCubeButtons[42], self.customScrambleCubeButtons[43],
                             self.customScrambleCubeButtons[44]])
                        buttongroups.append(
                            [self.customScrambleCubeButtons[45], self.customScrambleCubeButtons[46],
                             self.customScrambleCubeButtons[47],
                             self.customScrambleCubeButtons[48], self.customScrambleCubeButtons[49],
                             self.customScrambleCubeButtons[50],
                             self.customScrambleCubeButtons[51], self.customScrambleCubeButtons[52],
                             self.customScrambleCubeButtons[53]])

                        for buttongroup in buttongroups:
                            for button in buttongroup:
                                button.groupUpdate = False

                            for button in buttongroup:
                                button.hover(mx, my)
                                if button.isHovered == True and not button.groupUpdate:
                                    button.animateGroup(buttongroup)

                            for button in buttongroup:
                                button.clicked(mx, my, mousePressedUp)
                                button.update()
                                button.draw()

                                if button.isleftClicked:
                                    match button.onClick:
                                        case "top":
                                            self.solver.makeMove("U'", True)
                                        case "front":
                                            self.solver.makeMove("F'", True)
                                        case "bottom":
                                            self.solver.makeMove("D'", True)
                                        case "back":
                                            self.solver.makeMove("B'", True)
                                        case "left":
                                            self.solver.makeMove("L'", True)
                                        case "right":
                                            self.solver.makeMove("R'", True)
                                elif button.isrightClicked:
                                    match button.onClick:
                                        case "top":
                                            self.solver.makeMove("U", True)
                                        case "front":
                                            self.solver.makeMove("F", True)
                                        case "bottom":
                                            self.solver.makeMove("D", True)
                                        case "back":
                                            self.solver.makeMove("B", True)
                                        case "left":
                                            self.solver.makeMove("L", True)
                                        case "right":
                                            self.solver.makeMove("R", True)

                    else:
                        # 3D
                        text = headingFont.render("Comming soon ...", True, (255, 255, 255))
                        newRect = text.get_rect()
                        newRect.centerx = self.windowWidth / 2
                        newRect.centery = self.windowHeight / 2
                        self.screen.blit(text, newRect)


                    # display scramble and solve moves
                    displayedText = []
                    scrambleMoves = ""
                    first = True
                    for move in self.solver.scrambleMoves:
                        if first:
                            scrambleMoves += str(move)
                            first = False
                        else:
                            scrambleMoves += " ," + str(move)
                    displayedText.append("Scramble: (" + str(len(self.solver.scrambleMoves)) + ")")
                    displayedText.append(scrambleMoves)

                    if self.solver.solveMoves != []:
                        displayedText.append("Solve: (" + str(len(self.solver.simplifiedSolveMoves)) + ")")

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

                            if count == 32:
                                count = 0
                                displayedText.append(simplifiedMoves)
                                simplifiedMoves = ""
                                first = True
                        displayedText.append(simplifiedMoves)

                    for i in range(len(displayedText)):
                        text = smallerFont.render(displayedText[i], True, (255, 255, 255))
                        newRect = text.get_rect()
                        newRect.x = 20
                        newRect.y = (1200 + textSize * i + textSize * i / 2) - textSize * 1.5
                        self.screen.blit(text, newRect)


                    for button in self.customScrambleButtons:
                        button.update()
                        button.draw(drawOnClickText=True, onClickTextSize=25)
                        if button.clicked(mx, my, mousePressedUp):
                            match button.onClick:
                                case "Back":
                                    self.menu = "main"
                                case "Reset":
                                    self.solver.reset()
                                case "Solve":
                                    self.solver.solve()

                    for switchButton in self.customScrambleSwitchButtons:
                        switchButton.draw((20, 20, 20), (128, 255, 128))
                        switchButton.clicked(mx, my, mousePressedUp)

            pygame.display.flip()
            self.clock.tick(60)

    def generateBackgroundCubes(self):
        self.backgroundCubes = []

        minSize = 50
        maxSize = 300
        minRotation = 0
        maxRotation = 90

        locations = [[0, self.windowWidth/3, 0, self.windowHeight/3], [(self.windowWidth/3)*2, self.windowWidth, 0, self.windowHeight/3],
                     [0, self.windowWidth/3, self.windowHeight/3, (self.windowHeight/3)*2], [(self.windowWidth/3)*2, self.windowWidth, self.windowHeight/3, (self.windowHeight/3)*2],
                     [0, self.windowWidth/3, (self.windowHeight/3)*2, self.windowHeight], [self.windowWidth/3, (self.windowWidth/3)*2, (self.windowHeight/3)*2, self.windowHeight], [(self.windowWidth/3)*2, self.windowWidth, (self.windowHeight/3)*2, self.windowHeight]]

        for location in locations:
            randomSize = random.randint(minSize, maxSize)
            size = [randomSize, randomSize]
            degree = random.randint(minRotation, maxRotation)
            color = self.availableColors[random.randint(0, len(self.availableColors)-1)]
            self.backgroundCubes.append(RotatedRect.RotatedRect(self.screen, location, size, degree, color))

    def drawCube(self, width, posX, posY, centerX=False, centerY=False):
        # draw cube
        cubeRects = []
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
                        case 0: # empty
                            color = (100, 100, 100)
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

                    rect = pygame.Rect(x, y, width, width)
                    cubeRects.append(rect)
                    pygame.draw.rect(self.screen, color, rect)

        return cubeRects

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
                    y = (i * (height + 10)) + (self.windowHeight/2) - (155 * self.windowHeight / 1000)

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

                    self.customScrambleCubeButtons.append(Button.Button(self.screen, x, y, width, height, color, onClick, False, 10))

    def updateCustomScrambleButtons(self, width):
        counter = 0
        cube = self.solver.generateComplete()
        for i in range(len(cube)):
            for j in range(len(cube[0])):
                if cube[i][j] != -1:
                    height = width
                    x = (j * (width + 10)) + (self.windowWidth / 2) - width / 2 - (width * 4.5)
                    y = (i * (height + 10)) + 150

                    color = (0, 0, 0)

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

                    self.customScrambleCubeButtons[counter].updateLocationAndSize(x, y, width, height)
                    self.customScrambleCubeButtons[counter].color = color
                    counter += 1


if __name__ == "__main__":
    main()
