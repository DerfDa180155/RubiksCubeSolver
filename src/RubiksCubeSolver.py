import random

from numpy.random import vonmises


class RubiksCubeSolver:
    def __init__(self):
        self.top = self.generateEmptySide(middle=1)
        self.bottom = self.generateEmptySide(middle=3)
        self.right = self.generateEmptySide(middle=6)
        self.left = self.generateEmptySide(middle=5)
        self.front = self.generateEmptySide(middle=2)
        self.back = self.generateEmptySide(middle=4)

        self.scrambleMoves = []
        self.solveMoves = []
        self.state = 0

        for i in range(1, 7):
            self.fillSide(i)

    def reset(self):
        self.top = self.generateEmptySide(middle=1)
        self.bottom = self.generateEmptySide(middle=3)
        self.right = self.generateEmptySide(middle=6)
        self.left = self.generateEmptySide(middle=5)
        self.front = self.generateEmptySide(middle=2)
        self.back = self.generateEmptySide(middle=4)

        self.scrambleMoves = []
        self.solveMoves = []
        self.state = 0

        for i in range(1, 7):
            self.fillSide(i)

    def generateEmptySide(self, middle):
        side = []
        for i in range(3):
            if i == 1:
                side.append([0,middle,0])
            else:
                side.append([0,0,0])
        return side

    def fillSide(self, side):
        match side:
            case 1:
                for i in range(len(self.top)):
                    for j in range(len(self.top[0])):
                        self.top[i][j] = self.top[1][1]
            case 2:
                for i in range(len(self.bottom)):
                    for j in range(len(self.bottom[0])):
                        self.bottom[i][j] = self.bottom[1][1]
            case 3:
                for i in range(len(self.right)):
                    for j in range(len(self.right[0])):
                        self.right[i][j] = self.right[1][1]
            case 4:
                for i in range(len(self.left)):
                    for j in range(len(self.left[0])):
                        self.left[i][j] = self.left[1][1]
            case 5:
                for i in range(len(self.front)):
                    for j in range(len(self.front[0])):
                        self.front[i][j] = self.front[1][1]
            case 6:
                for i in range(len(self.back)):
                    for j in range(len(self.back[0])):
                        self.back[i][j] = self.back[1][1]

    def generateComplete(self):
        complite =  []

        for i in range(3):
            temp = []
            for j in range(3):
                temp.append(-1)
            for j in range(3):
                temp.append(self.top[j][i])
            for j in range(3):
                temp.append(-1)
            complite.append(temp)

        for i in range(3):
            temp = []
            for j in range(3):
                temp.append(self.left[j][i])
            for j in range(3):
                temp.append(self.front[j][i])
            for j in range(3):
                temp.append(self.right[j][i])
            complite.append(temp)

        for i in range(3):
            temp = []
            for j in range(3):
                temp.append(-1)
            for j in range(3):
                temp.append(self.bottom[j][i])
            for j in range(3):
                temp.append(-1)
            complite.append(temp)

        for i in range(3):
            temp = []
            for j in range(3):
                temp.append(-1)
            for j in range(3):
                temp.append(self.back[j][i])
            for j in range(3):
                temp.append(-1)
            complite.append(temp)

        return complite

    def makeMove(self, move, isScrambleMove = False):
        if not isScrambleMove:
            if move.find("'") != -1:
                self.solveMoves.append(move[:2])
            else:
                self.solveMoves.append(move[:1])
        match move:
            case "UP" | "U":
                self.top = self.rotate(self.top, True)
                self.rotateAdjacent(self.back, [[0,2],[1,2],[2,2]], self.right, [[2,0],[1,0],[0,0]], self.front, [[2,0],[1,0],[0,0]], self.left, [[2,0],[1,0],[0,0]])
            case "U'":
                self.top = self.rotate(self.top, False)
                self.rotateAdjacent(self.back, [[0, 2], [1, 2], [2, 2]], self.left, [[2, 0], [1, 0], [0, 0]], self.front, [[2, 0], [1, 0], [0, 0]], self.right, [[2, 0], [1, 0], [0, 0]])
            case "Front" | "F":
                self.front = self.rotate(self.front, True)
                self.rotateAdjacent(self.top, [[0,2],[1,2],[2,2]], self.right, [[0,0],[0,1],[0,2]], self.bottom, [[2,0],[1,0],[0,0]], self.left, [[2,2],[2,1],[2,0]])
            case "F'":
                self.front = self.rotate(self.front, False)
                self.rotateAdjacent(self.top, [[0, 2], [1, 2], [2, 2]], self.left, [[2, 2], [2, 1], [2, 0]], self.bottom, [[2, 0], [1, 0], [0, 0]], self.right, [[0, 0], [0, 1], [0, 2]])
            case "Down" | "D":
                self.bottom = self.rotate(self.bottom, True)
                self.rotateAdjacent(self.front, [[0,2],[1,2],[2,2]], self.right, [[0,2],[1,2],[2,2]], self.back, [[2,0],[1,0],[0,0]], self.left, [[0,2],[1,2],[2,2]])
            case "D'":
                self.bottom = self.rotate(self.bottom, False)
                self.rotateAdjacent(self.front, [[0, 2], [1, 2], [2, 2]], self.left, [[0, 2], [1, 2], [2, 2]], self.back, [[2, 0], [1, 0], [0, 0]], self.right, [[0, 2], [1, 2], [2, 2]])
            case "Back" | "B":
                self.back = self.rotate(self.back, True)
                self.rotateAdjacent(self.bottom, [[0,2],[1,2],[2,2]], self.right, [[2,2],[2,1],[2,0]], self.top, [[2,0],[1,0],[0,0]], self.left, [[0,0],[0,1],[0,2]])
            case "B'":
                self.back = self.rotate(self.back, False)
                self.rotateAdjacent(self.bottom, [[0, 2], [1, 2], [2, 2]], self.left, [[0, 0], [0, 1], [0, 2]], self.top, [[2, 0], [1, 0], [0, 0]], self.right, [[2, 2], [2, 1], [2, 0]])
            case "Left" | "L":
                self.left = self.rotate(self.left, True)
                self.rotateAdjacent(self.top, [[0,0],[0,1],[0,2]], self.front, [[0,0],[0,1],[0,2]], self.bottom, [[0,0],[0,1],[0,2]], self.back, [[0,0],[0,1],[0,2]])
            case "L'":
                self.left = self.rotate(self.left, False)
                self.rotateAdjacent(self.top, [[0, 0], [0, 1], [0, 2]], self.back, [[0, 0], [0, 1], [0, 2]], self.bottom, [[0, 0], [0, 1], [0, 2]], self.front, [[0, 0], [0, 1], [0, 2]])
            case "Right" | "R":
                self.right = self.rotate(self.right, True)
                self.rotateAdjacent(self.top, [[2,2],[2,1],[2,0]], self.back, [[2,2],[2,1],[2,0]], self.bottom, [[2,2],[2,1],[2,0]], self.front, [[2,2],[2,1],[2,0]])
            case "R'":
                self.right = self.rotate(self.right, False)
                self.rotateAdjacent(self.top, [[2, 2], [2, 1], [2, 0]], self.front, [[2, 2], [2, 1], [2, 0]], self.bottom, [[2, 2], [2, 1], [2, 0]], self.back, [[2, 2], [2, 1], [2, 0]])

            case "u":
                self.top = self.rotate(self.top, True)
                self.rotateAdjacent(self.back, [[0, 2], [1, 2], [2, 2]], self.right, [[2, 0], [1, 0], [0, 0]], self.front, [[2, 0], [1, 0], [0, 0]], self.left, [[2, 0], [1, 0], [0, 0]])
                self.rotateMiddle(self.front, [[0, 1], [2, 1]], self.right, [[0, 1], [2, 1]], self.back, [[2, 1], [0, 1]], self.left, [[0, 1], [2, 1]])
            case "u'":
                self.top = self.rotate(self.top, False)
                self.rotateAdjacent(self.back, [[0, 2], [1, 2], [2, 2]], self.left, [[2, 0], [1, 0], [0, 0]], self.front, [[2, 0], [1, 0], [0, 0]], self.right, [[2, 0], [1, 0], [0, 0]])
                self.rotateMiddle(self.front, [[2, 1], [0, 1]], self.left, [[2, 1], [0, 1]], self.back, [[0, 1], [2, 1]], self.right, [[2, 1], [0, 1]])
            case "f":
                self.front = self.rotate(self.front, True)
                self.rotateAdjacent(self.top, [[0, 2], [1, 2], [2, 2]], self.right, [[0, 0], [0, 1], [0, 2]], self.bottom, [[2, 0], [1, 0], [0, 0]], self.left, [[2, 2], [2, 1], [2, 0]])
                self.rotateMiddle(self.top, [[2, 1], [0, 1]], self.left, [[1, 0], [1, 2]], self.bottom, [[0, 1], [2, 1]], self.right, [[1, 2], [1, 0]])
            case "f'":
                self.front = self.rotate(self.front, False)
                self.rotateAdjacent(self.top, [[0, 2], [1, 2], [2, 2]], self.left, [[2, 2], [2, 1], [2, 0]], self.bottom, [[2, 0], [1, 0], [0, 0]], self.right, [[0, 0], [0, 1], [0, 2]])
                self.rotateMiddle(self.top, [[0, 1], [2, 1]], self.right, [[1, 0], [1, 2]], self.bottom, [[2, 1], [0, 1]], self.left, [[1, 2], [1, 0]])
            case "d":
                self.bottom = self.rotate(self.bottom, True)
                self.rotateAdjacent(self.front, [[0, 2], [1, 2], [2, 2]], self.right, [[0, 2], [1, 2], [2, 2]], self.back, [[2, 0], [1, 0], [0, 0]], self.left, [[0, 2], [1, 2], [2, 2]])
                self.rotateMiddle(self.front, [[2, 1], [0, 1]], self.left, [[2, 1], [0, 1]], self.back, [[0, 1], [2, 1]], self.right, [[2, 1], [0, 1]])
            case "d'":
                self.bottom = self.rotate(self.bottom, False)
                self.rotateAdjacent(self.front, [[0, 2], [1, 2], [2, 2]], self.left, [[0, 2], [1, 2], [2, 2]], self.back, [[2, 0], [1, 0], [0, 0]], self.right, [[0, 2], [1, 2], [2, 2]])
                self.rotateMiddle(self.front, [[0, 1], [2, 1]], self.right, [[0, 1], [2, 1]], self.back, [[2, 1], [0, 1]], self.left, [[0, 1], [2, 1]])
            case "b":
                self.back = self.rotate(self.back, True)
                self.rotateAdjacent(self.bottom, [[0, 2], [1, 2], [2, 2]], self.right, [[2, 2], [2, 1], [2, 0]], self.top, [[2, 0], [1, 0], [0, 0]], self.left, [[0, 0], [0, 1], [0, 2]])
                self.rotateMiddle(self.top, [[0, 1], [2, 1]], self.right, [[1, 0], [1, 2]], self.bottom, [[2, 1], [0, 1]], self.left, [[1, 2], [1, 0]])
            case "b'":
                self.back = self.rotate(self.back, False)
                self.rotateAdjacent(self.bottom, [[0, 2], [1, 2], [2, 2]], self.left, [[0, 0], [0, 1], [0, 2]], self.top, [[2, 0], [1, 0], [0, 0]], self.right, [[2, 2], [2, 1], [2, 0]])
                self.rotateMiddle(self.top, [[2, 1], [0, 1]], self.left, [[1, 0], [1, 2]], self.bottom, [[0, 1], [2, 1]], self.right, [[1, 2], [1, 0]])
            case "l":
                self.left = self.rotate(self.left, True)
                self.rotateAdjacent(self.top, [[0, 0], [0, 1], [0, 2]], self.front, [[0, 0], [0, 1], [0, 2]], self.bottom, [[0, 0], [0, 1], [0, 2]], self.back, [[0, 0], [0, 1], [0, 2]])
                self.rotateMiddle(self.top, [[1, 2], [1, 0]], self.back, [[1, 2], [1, 0]], self.bottom, [[1, 2], [1, 0]], self.front, [[1, 2], [1, 0]])
            case "l'":
                self.left = self.rotate(self.left, False)
                self.rotateAdjacent(self.top, [[0, 0], [0, 1], [0, 2]], self.back, [[0, 0], [0, 1], [0, 2]], self.bottom, [[0, 0], [0, 1], [0, 2]], self.front, [[0, 0], [0, 1], [0, 2]])
                self.rotateMiddle(self.top, [[1, 0], [1, 2]], self.front, [[1, 0], [1, 2]], self.bottom, [[1, 0], [1, 2]], self.back, [[1, 0], [1, 2]])
            case "r":
                self.right = self.rotate(self.right, True)
                self.rotateAdjacent(self.top, [[2, 2], [2, 1], [2, 0]], self.back, [[2, 2], [2, 1], [2, 0]], self.bottom, [[2, 2], [2, 1], [2, 0]], self.front, [[2, 2], [2, 1], [2, 0]])
                self.rotateMiddle(self.top, [[1, 0], [1, 2]], self.front, [[1, 0], [1, 2]], self.bottom, [[1, 0], [1, 2]], self.back, [[1, 0], [1, 2]])
            case "r'":
                self.right = self.rotate(self.right, False)
                self.rotateAdjacent(self.top, [[2, 2], [2, 1], [2, 0]], self.front, [[2, 2], [2, 1], [2, 0]], self.bottom, [[2, 2], [2, 1], [2, 0]], self.back, [[2, 2], [2, 1], [2, 0]])
                self.rotateMiddle(self.top, [[1, 2], [1, 0]], self.back, [[1, 2], [1, 0]], self.bottom, [[1, 2], [1, 0]], self.front, [[1, 2], [1, 0]])

    def rotate(self, side, clockwise):
        newSide = self.generateEmptySide(side[1][1])
        if clockwise:
            corners = [[0,0], [0,2], [2,2], [2,0]]
            edges = [[0,1], [1,2], [2,1], [1,0]]
        else:
            corners = [[0, 0], [2, 0], [2, 2], [0, 2]]
            edges = [[0, 1], [1, 0], [2, 1], [1, 2]]

        temp = side[corners[0][0]][corners[0][1]]
        i = 1
        for square in corners:
            if i < 4:
                newSide[square[0]][square[1]] = side[corners[i][0]][corners[i][1]]
                i += 1
            else:
                newSide[square[0]][square[1]] = temp

        temp = side[edges[0][0]][edges[0][1]]
        i = 1
        for square in edges:
            if i < 4:
                newSide[square[0]][square[1]] = side[edges[i][0]][edges[i][1]]
                i += 1
            else:
                newSide[square[0]][square[1]] = temp

        return newSide

    def rotateAdjacent(self, top, topPositions, right, rightPostions, bottom, bottomPositions, left, leftPositions):
        temp = [top[topPositions[0][0]][topPositions[0][1]],top[topPositions[1][0]][topPositions[1][1]],top[topPositions[2][0]][topPositions[2][1]]]

        top[topPositions[0][0]][topPositions[0][1]] = left[leftPositions[0][0]][leftPositions[0][1]]
        top[topPositions[1][0]][topPositions[1][1]] = left[leftPositions[1][0]][leftPositions[1][1]]
        top[topPositions[2][0]][topPositions[2][1]] = left[leftPositions[2][0]][leftPositions[2][1]]

        left[leftPositions[0][0]][leftPositions[0][1]] = bottom[bottomPositions[0][0]][bottomPositions[0][1]]
        left[leftPositions[1][0]][leftPositions[1][1]] = bottom[bottomPositions[1][0]][bottomPositions[1][1]]
        left[leftPositions[2][0]][leftPositions[2][1]] = bottom[bottomPositions[2][0]][bottomPositions[2][1]]

        bottom[bottomPositions[0][0]][bottomPositions[0][1]] = right[rightPostions[0][0]][rightPostions[0][1]]
        bottom[bottomPositions[1][0]][bottomPositions[1][1]] = right[rightPostions[1][0]][rightPostions[1][1]]
        bottom[bottomPositions[2][0]][bottomPositions[2][1]] = right[rightPostions[2][0]][rightPostions[2][1]]

        right[rightPostions[0][0]][rightPostions[0][1]] = temp[0]
        right[rightPostions[1][0]][rightPostions[1][1]] = temp[1]
        right[rightPostions[2][0]][rightPostions[2][1]] = temp[2]

    def rotateMiddle(self, side1, side1Positions, side2, side2Positions, side3, side3Positions, side4, side4Positions):
        temp = [side1[side1Positions[0][0]][side1Positions[0][1]], side1[side1Positions[1][0]][side1Positions[1][1]]]

        side1[side1Positions[0][0]][side1Positions[0][1]] = side2[side2Positions[0][0]][side2Positions[0][1]]
        side1[side1Positions[1][0]][side1Positions[1][1]] = side2[side2Positions[1][0]][side2Positions[1][1]]

        side2[side2Positions[0][0]][side2Positions[0][1]] = side3[side3Positions[0][0]][side3Positions[0][1]]
        side2[side2Positions[1][0]][side2Positions[1][1]] = side3[side3Positions[1][0]][side3Positions[1][1]]

        side3[side3Positions[0][0]][side3Positions[0][1]] = side4[side4Positions[0][0]][side4Positions[0][1]]
        side3[side3Positions[1][0]][side3Positions[1][1]] = side4[side4Positions[1][0]][side4Positions[1][1]]

        side4[side4Positions[0][0]][side4Positions[0][1]] = temp[0]
        side4[side4Positions[1][0]][side4Positions[1][1]] = temp[1]

    def generateScramble(self):
        lastMove = ""
        moves = ["U", "D", "F", "B", "L", "R"]
        self.reset()
        for i in range(20):
            move = moves[random.randint(0, len(moves)-1)]
            while move == lastMove:
                move = moves[random.randint(0, len(moves) - 1)]
            self.scrambleMoves.append(move)
            lastMove = move

        self.scramble(self.scrambleMoves)

    def scramble(self, scramble):
        for move in scramble:
            self.makeMove(move, True)

    def doAlgorithm(self, algorithm):
        for move in algorithm:
            self.makeMove(move, False)

    def solveState(self):
        match self.state:
            case 0: # cross
                if self.top[1][0] == 1 and self.top[2][1] == 1 and self.top[1][2] == 1 and self.top[0][1] == 1 and self.back[1][2] == 4 and self.right[1][0] == 6 and self.front[1][0] == 2 and self.left[1][0] == 5:
                    self.state += 1
            case 1: # corners
                if self.top[0][0] == 1 and self.top[2][0] == 1 and self.top[2][2] == 1 and self.top[0][2] == 1 and self.back[2][2] == 4 and self.back[0][2] == 4 and self.right[2][0] == 6 and self.right[0][0] == 6 and self.front[2][0] == 2 and self.front[0][0] == 2 and self.left[2][0] == 5 and self.left[0][0] == 5:
                    self.state += 1
            case 2: # 2nd layer
                if self.front[2][1] == 2 and self.front[0][1] == 2 and self.left[2][1] == 5 and self.left[0][1] == 5 and self.back[0][1] == 4 and self.back[2][1] == 4 and self.right[2][1] == 6 and self.right[0][1] == 6:
                    self.state += 1
            case 3: # OLL
                if self.bottom[0][0] == 3 and self.bottom[1][0] == 3 and self.bottom[2][0] == 3 and self.bottom[2][1] == 3 and self.bottom[2][2] == 3 and self.bottom[1][2] == 3 and self.bottom[0][2] == 3 and self.bottom[0][1] == 3:
                    self.state += 1
            case 4: # PLL
                if self.front[0][2] == 2 and self.front[1][2] == 2 and self.front[2][2] == 2 and self.left[0][2] == 5 and self.left[1][2] == 5 and self.left[2][2] == 5 and self.back[2][0] == 4 and self.back[1][0] == 4 and self.back[0][0] == 4 and self.right[0][2] == 6 and self.right[1][2] == 6 and self.right[2][2] == 6:
                    self.state += 1

    def solve(self):
        print("solver")
        self.solveState()

        match self.state:
            case 0: # cross
                print("cross")
                self.crossSolver()
            case 1: # corners
                print("corners")
                self.cornerSolver()
            case 2: # 2nd layer
                print("2nd layer")
                self.secondLayerSolver()
            case 3: # OLL
                print("OLL")
                self.OLLSolver()
            case 4: # PLL
                print("PLL")

        print(self.solveMoves)


    def crossSolver(self):
        # correct edges
        topEdges = []
        topEdges.append([self.top[1][2] == 1, self.front[1][0], 2, ["F", "F"]])
        topEdges.append([self.top[0][1] == 1, self.left[1][0], 5, ["L", "L"]])
        topEdges.append([self.top[1][0] == 1, self.back[1][2], 4, ["B", "B"]])
        topEdges.append([self.top[2][1] == 1, self.right[1][0], 6, ["R", "R"]])

        searchEdges = []
        # bottom side edges
        searchEdges.append([self.front[1][2], ["F", "L", "D", "D", "L'", "F'"]])
        searchEdges.append([self.left[1][2], ["L", "B", "D", "D", "B'", "L'"]])
        searchEdges.append([self.back[1][0], ["B", "R", "D", "D", "R'", "B'"]])
        searchEdges.append([self.right[1][2], ["R", "F", "D", "D", "F'", "R'"]])

        # left side edges
        searchEdges.append([self.front[0][1], ["L", "D", "L'"]])
        searchEdges.append([self.left[0][1], ["B", "D", "B'"]])
        searchEdges.append([self.back[2][1], ["R", "D", "R'"]])
        searchEdges.append([self.right[0][1], ["F", "D", "F'"]])

        # right side edges
        searchEdges.append([self.front[2][1], ["R'", "D'", "R"]])
        searchEdges.append([self.left[2][1], ["F'", "D'", "F"]])
        searchEdges.append([self.back[0][1], ["L'", "D'", "L"]])
        searchEdges.append([self.right[2][1], ["B'", "D'", "B"]])

        # top side edges
        searchEdges.append([self.front[1][0], ["F", "R'", "D", "R", "F'"]])
        searchEdges.append([self.left[1][0], ["L", "F'", "D", "F", "L'"]])
        searchEdges.append([self.back[1][2], ["B", "L'", "D", "L", "B'"]])
        searchEdges.append([self.right[1][0], ["R", "B'", "D", "B", "R'"]])

        # solve bottom top edges
        self.moveBottomToTop()

        # check wrong top piece
        for edge in topEdges:
            if edge[0] and edge[1] != edge[2]:
                self.doAlgorithm(edge[3])
                self.moveBottomToTop()

        # move edges to bottom
        for edge in searchEdges:
            if edge[0] == 1:
                self.doAlgorithm(edge[1])
                self.moveBottomToTop()

    def moveBottomToTop(self):
        bottomEdges = []
        bottomEdges.append([self.bottom[1][0], self.front[1][2], self.front[1][1], ["F", "F"]])
        bottomEdges.append([self.bottom[0][1], self.left[1][2], self.left[1][1], ["L", "L"]])
        bottomEdges.append([self.bottom[1][2], self.back[1][0], self.back[1][1], ["B", "B"]])
        bottomEdges.append([self.bottom[2][1], self.right[1][2], self.right[1][1], ["R", "R"]])

        rotateBottom = False
        edgeFound = False

        for i in range(len(bottomEdges)):
            if bottomEdges[i][0] == 1:
                edgeFound = True

        while edgeFound:
            edgeFound = False
            rotateBottom = False
            for i in range(len(bottomEdges)):
                if bottomEdges[i][0] == 1:
                    if bottomEdges[i][1] == bottomEdges[i][2]:
                        self.doAlgorithm(bottomEdges[i][3])
                    else:
                        rotateBottom = True
                        edgeFound = True
            if rotateBottom:
                self.makeMove("D")
                bottomEdges = []
                bottomEdges.append([self.bottom[1][0], self.front[1][2], self.front[1][1], ["F", "F"]])
                bottomEdges.append([self.bottom[0][1], self.left[1][2], self.left[1][1], ["L", "L"]])
                bottomEdges.append([self.bottom[1][2], self.back[1][0], self.back[1][1], ["B", "B"]])
                bottomEdges.append([self.bottom[2][1], self.right[1][2], self.right[1][1], ["R", "R"]])

    def cornerSolver(self):
        searchCorners = []
        searchCorners.append([self.front[0][2], self.left[2][2] == self.left[1][1], ["F'", "D'", "F"]])
        searchCorners.append([self.front[2][2], self.right[0][2] == self.right[1][1], ["F", "D", "F'"]])
        searchCorners.append([self.left[0][2], self.back[0][0] == self.back[1][1], ["L'", "D'", "L"]])
        searchCorners.append([self.left[2][2], self.front[0][2] == self.front[1][1], ["L", "D", "L'"]])
        searchCorners.append([self.back[2][0], self.right[2][2] == self.right[1][1], ["B'", "D'", "B"]])
        searchCorners.append([self.back[0][0], self.left[0][2] == self.left[1][1], ["B", "D", "B'"]])
        searchCorners.append([self.right[0][2], self.front[2][2] == self.front[1][1], ["R'", "D'", "R"]])
        searchCorners.append([self.right[2][2], self.back[2][0] == self.back[1][1], ["R", "D", "R'"]])

        foundCorner = False
        rotateBottom = False
        for corner in searchCorners:
            if corner[0] == 1:
                foundCorner = True

        while foundCorner:
            foundCorner = False
            rotateBottom = False
            for corner in searchCorners:
                if corner[0] == 1:
                    if corner[1]:
                        self.doAlgorithm(corner[2])
                        searchCorners = []
                        searchCorners.append([self.front[0][2], self.left[2][2] == self.left[1][1], ["F'", "D'", "F"]])
                        searchCorners.append([self.front[2][2], self.right[0][2] == self.right[1][1], ["F", "D", "F'"]])
                        searchCorners.append([self.left[0][2], self.back[0][0] == self.back[1][1], ["L'", "D'", "L"]])
                        searchCorners.append([self.left[2][2], self.front[0][2] == self.front[1][1], ["L", "D", "L'"]])
                        searchCorners.append([self.back[2][0], self.right[2][2] == self.right[1][1], ["B'", "D'", "B"]])
                        searchCorners.append([self.back[0][0], self.left[0][2] == self.left[1][1], ["B", "D", "B'"]])
                        searchCorners.append([self.right[0][2], self.front[2][2] == self.front[1][1], ["R'", "D'", "R"]])
                        searchCorners.append([self.right[2][2], self.back[2][0] == self.back[1][1], ["R", "D", "R'"]])
                    else:
                        foundCorner = True
                        rotateBottom = True
            if rotateBottom:
                self.makeMove("D")
                searchCorners = []
                searchCorners.append([self.front[0][2], self.left[2][2] == self.left[1][1], ["F'", "D'", "F"]])
                searchCorners.append([self.front[2][2], self.right[0][2] == self.right[1][1], ["F", "D", "F'"]])
                searchCorners.append([self.left[0][2], self.back[0][0] == self.back[1][1], ["L'", "D'", "L"]])
                searchCorners.append([self.left[2][2], self.front[0][2] == self.front[1][1], ["L", "D", "L'"]])
                searchCorners.append([self.back[2][0], self.right[2][2] == self.right[1][1], ["B'", "D'", "B"]])
                searchCorners.append([self.back[0][0], self.left[0][2] == self.left[1][1], ["B", "D", "B'"]])
                searchCorners.append([self.right[0][2], self.front[2][2] == self.front[1][1], ["R'", "D'", "R"]])
                searchCorners.append([self.right[2][2], self.back[2][0] == self.back[1][1], ["R", "D", "R'"]])


        # bottom corners
        bottomCorner = []
        bottomCorner.append([self.bottom[0][2] == 1, self.top[0][0] != 1, ["B", "D'", "B'"]])
        bottomCorner.append([self.bottom[2][2] == 1, self.top[2][0] != 1, ["B'", "D", "B"]])
        bottomCorner.append([self.bottom[2][0] == 1, self.top[2][2] != 1, ["F", "D'", "F'"]])
        bottomCorner.append([self.bottom[0][0] == 1, self.top[0][2] != 1, ["F'", "D", "F"]])


        for corner in bottomCorner:
            #foundCorner = False
            rotateBottom = False
            if corner[0]:
                if corner[1]:
                    self.doAlgorithm(corner[2])
                    #foundCorner = False
                    bottomCorner = []
                    bottomCorner.append([self.bottom[0][2] == 1, self.top[0][0] != 1, ["B", "D'", "B'"]])
                    bottomCorner.append([self.bottom[2][2] == 1, self.top[2][0] != 1, ["B'", "D", "B"]])
                    bottomCorner.append([self.bottom[2][0] == 1, self.top[2][2] != 1, ["F", "D'", "F'"]])
                    bottomCorner.append([self.bottom[0][0] == 1, self.top[0][2] != 1, ["F'", "D", "F"]])
                else:
                    #foundCorner = True
                    rotateBottom = True
            if rotateBottom:
                self.makeMove("D")
                bottomCorner = []
                bottomCorner.append([self.bottom[0][2] == 1, self.top[0][0] != 1, ["B", "D'", "B'"]])
                bottomCorner.append([self.bottom[2][2] == 1, self.top[2][0] != 1, ["B'", "D", "B"]])
                bottomCorner.append([self.bottom[2][0] == 1, self.top[2][2] != 1, ["F", "D'", "F'"]])
                bottomCorner.append([self.bottom[0][0] == 1, self.top[0][2] != 1, ["F'", "D", "F"]])


        topCorner = []
        topCorner.append([self.top[0][0] == 1, self.left[0][0] != self.left[1][1], ["L'", "D", "L"]])
        topCorner.append([self.top[2][0] == 1, self.right[2][0] != self.right[1][1], ["R", "D'", "R'"]])
        topCorner.append([self.top[2][2] == 1, self.right[0][0] != self.right[1][1], ["R'", "D", "R"]])
        topCorner.append([self.top[0][2] == 1, self.left[2][0] != self.left[1][1], ["L", "D'", "L'"]])

        # wrong top corners
        for corner in topCorner:
            if corner[0] and corner[1]:
                self.doAlgorithm(corner[2])


        # top side corners
        topSideCorners = []
        topSideCorners.append([self.front[0][0] == 1, ["F'", "D", "F"]])
        topSideCorners.append([self.front[2][0] == 1, ["F", "D'", "F'"]])
        topSideCorners.append([self.left[0][0] == 1, ["L'", "D", "L"]])
        topSideCorners.append([self.left[2][0] == 1, ["L", "D'", "L'"]])
        topSideCorners.append([self.back[2][2] == 1, ["B'", "D", "B"]])
        topSideCorners.append([self.back[0][2] == 1, ["B", "D'", "B'"]])
        topSideCorners.append([self.right[0][0] == 1, ["R'", "D", "R"]])
        topSideCorners.append([self.right[2][0] == 1, ["R", "D'", "R'"]])

        for corner in topSideCorners:
            if corner[0]:
                self.doAlgorithm(corner[1])

    def secondLayerSolver(self):
        solvedEdges = []
        solvedEdges.append(self.front[0][1] == self.front[1][1] and self.left[2][1] == self.left[1][1])
        solvedEdges.append(self.left[0][1] == self.left[1][1] and self.back[0][1] == self.back[1][1])
        solvedEdges.append(self.back[2][1] == self.back[1][1] and self.right[2][1] == self.right[1][1])
        solvedEdges.append(self.right[0][1] == self.right[1][1] and self.front[2][1] == self.front[1][1])

        searchEdges = []
        searchEdges.append([self.front[1][2] == self.front[1][1], self.bottom[1][0] == self.right[1][1], ["D'", "R'", "D", "R", "D", "F", "D'", "F'"]])
        searchEdges.append([self.front[1][2] == self.front[1][1], self.bottom[1][0] == self.left[1][1], ["D", "L", "D'", "L'", "D'", "F'", "D", "F"]])
        searchEdges.append([self.left[1][2] == self.left[1][1], self.bottom[0][1] == self.front[1][1], ["D'", "F'", "D", "F", "D", "L", "D'", "L'"]])
        searchEdges.append([self.left[1][2] == self.left[1][1], self.bottom[0][1] == self.back[1][1], ["D", "B", "D'", "B'", "D'", "L'", "D", "L"]])
        searchEdges.append([self.back[1][0] == self.back[1][1], self.bottom[1][2] == self.left[1][1], ["D'", "L'", "D", "L", "D", "B", "D'", "B'"]])
        searchEdges.append([self.back[1][0] == self.back[1][1], self.bottom[1][2] == self.right[1][1], ["D", "R", "D'", "R'", "D'", "B'", "D", "B"]])
        searchEdges.append([self.right[1][2] == self.right[1][1], self.bottom[2][1] == self.back[1][1], ["D'", "B'", "D", "B", "D", "R", "D'", "R'"]])
        searchEdges.append([self.right[1][2] == self.right[1][1], self.bottom[2][1] == self.front[1][1], ["D", "F", "D'", "F'", "D'", "R'", "D", "R"]])

        wrongEdges = []
        wrongEdges.append([self.front[0][1] in [1,2,4,5,6] and self.left[2][1] in [1,2,4,5,6] and not solvedEdges[0], ["D", "L", "D'", "L'", "D'", "F'", "D", "F"]])
        wrongEdges.append([self.left[0][1] in [1,2,4,5,6] and self.back[0][1] in [1,2,4,5,6] and not solvedEdges[1], ["D'", "L'", "D", "L", "D", "B", "D'", "B'"]])
        wrongEdges.append([self.back[2][1] in [1,2,4,5,6] and self.right[2][1] in [1,2,4,5,6] and not solvedEdges[2], ["D", "R", "D'", "R'", "D'", "B'", "D", "B"]])
        wrongEdges.append([self.right[0][1] in [1,2,4,5,6] and self.front[2][1] in [1,2,4,5,6] and not solvedEdges[3], ["D'", "R'", "D", "R", "D", "F", "D'", "F'"]])

        done = False
        for edge in solvedEdges:
            if not edge:
                done = True

        while done:
            for edge in searchEdges:
                if edge[0] and edge[1]:
                    self.doAlgorithm(edge[2])
                    searchEdges = []
                    searchEdges.append([self.front[1][2] == self.front[1][1], self.bottom[1][0] == self.right[1][1], ["D'", "R'", "D", "R", "D", "F", "D'", "F'"]])
                    searchEdges.append([self.front[1][2] == self.front[1][1], self.bottom[1][0] == self.left[1][1], ["D", "L", "D'", "L'", "D'", "F'", "D", "F"]])
                    searchEdges.append([self.left[1][2] == self.left[1][1], self.bottom[0][1] == self.front[1][1], ["D'", "F'", "D", "F", "D", "L", "D'", "L'"]])
                    searchEdges.append([self.left[1][2] == self.left[1][1], self.bottom[0][1] == self.back[1][1], ["D", "B", "D'", "B'", "D'", "L'", "D", "L"]])
                    searchEdges.append([self.back[1][0] == self.back[1][1], self.bottom[1][2] == self.left[1][1], ["D'", "L'", "D", "L", "D", "B", "D'", "B'"]])
                    searchEdges.append([self.back[1][0] == self.back[1][1], self.bottom[1][2] == self.right[1][1], ["D", "R", "D'", "R'", "D'", "B'", "D", "B"]])
                    searchEdges.append([self.right[1][2] == self.right[1][1], self.bottom[2][1] == self.back[1][1], ["D'", "B'", "D", "B", "D", "R", "D'", "R'"]])
                    searchEdges.append([self.right[1][2] == self.right[1][1], self.bottom[2][1] == self.front[1][1], ["D", "F", "D'", "F'", "D'", "R'", "D", "R"]])

            self.makeMove("D")

            solvedEdges = []
            solvedEdges.append(self.front[0][1] == self.front[1][1] and self.left[2][1] == self.left[1][1])
            solvedEdges.append(self.left[0][1] == self.left[1][1] and self.back[0][1] == self.back[1][1])
            solvedEdges.append(self.back[2][1] == self.back[1][1] and self.right[2][1] == self.right[1][1])
            solvedEdges.append(self.right[0][1] == self.right[1][1] and self.front[2][1] == self.front[1][1])

            wrongEdges = []
            wrongEdges.append([self.front[0][1] in [1, 2, 4, 5, 6] and self.left[2][1] in [1, 2, 4, 5, 6] and not solvedEdges[0], ["D", "L", "D'", "L'", "D'", "F'", "D", "F"]])
            wrongEdges.append([self.left[0][1] in [1, 2, 4, 5, 6] and self.back[0][1] in [1, 2, 4, 5, 6] and not solvedEdges[1], ["D'", "L'", "D", "L", "D", "B", "D'", "B'"]])
            wrongEdges.append([self.back[2][1] in [1, 2, 4, 5, 6] and self.right[2][1] in [1, 2, 4, 5, 6] and not solvedEdges[2], ["D", "R", "D'", "R'", "D'", "B'", "D", "B"]])
            wrongEdges.append([self.right[0][1] in [1, 2, 4, 5, 6] and self.front[2][1] in [1, 2, 4, 5, 6] and not solvedEdges[3], ["D'", "R'", "D", "R", "D", "F", "D'", "F'"]])

            for edge in wrongEdges:
                if edge[0]:
                    self.doAlgorithm(edge[1])

            searchEdges = []
            searchEdges.append([self.front[1][2] == self.front[1][1], self.bottom[1][0] == self.right[1][1], ["D'", "R'", "D", "R", "D", "F", "D'", "F'"]])
            searchEdges.append([self.front[1][2] == self.front[1][1], self.bottom[1][0] == self.left[1][1], ["D", "L", "D'", "L'", "D'", "F'", "D", "F"]])
            searchEdges.append([self.left[1][2] == self.left[1][1], self.bottom[0][1] == self.front[1][1], ["D'", "F'", "D", "F", "D", "L", "D'", "L'"]])
            searchEdges.append([self.left[1][2] == self.left[1][1], self.bottom[0][1] == self.back[1][1], ["D", "B", "D'", "B'", "D'", "L'", "D", "L"]])
            searchEdges.append([self.back[1][0] == self.back[1][1], self.bottom[1][2] == self.left[1][1], ["D'", "L'", "D", "L", "D", "B", "D'", "B'"]])
            searchEdges.append([self.back[1][0] == self.back[1][1], self.bottom[1][2] == self.right[1][1], ["D", "R", "D'", "R'", "D'", "B'", "D", "B"]])
            searchEdges.append([self.right[1][2] == self.right[1][1], self.bottom[2][1] == self.back[1][1], ["D'", "B'", "D", "B", "D", "R", "D'", "R'"]])
            searchEdges.append([self.right[1][2] == self.right[1][1], self.bottom[2][1] == self.front[1][1], ["D", "F", "D'", "F'", "D'", "R'", "D", "R"]])

            solvedEdges = []
            solvedEdges.append(self.front[0][1] == self.front[1][1] and self.left[2][1] == self.left[1][1])
            solvedEdges.append(self.left[0][1] == self.left[1][1] and self.back[0][1] == self.back[1][1])
            solvedEdges.append(self.back[2][1] == self.back[1][1] and self.right[2][1] == self.right[1][1])
            solvedEdges.append(self.right[0][1] == self.right[1][1] and self.front[2][1] == self.front[1][1])

            done = False
            for solved in solvedEdges:
                if not solved:
                    done = True

    def OLLSolver(self):
        oll1 = []
        oll1.append([self.front[1][2] == 3 and self.right[1][2] == 3 and self.back[1][0] == 3 and self.left[1][2] == 3, ["B", "R", "D", "R'", "D'", "B'", "b", "R", "D", "R'", "D'", "b'"]]) # dot
        oll1.append([self.front[1][2] == 3 and self.bottom[2][1] == 3 and self.back[1][0] == 3 and self.bottom[0][1] == 3, ["B", "R", "D", "R'", "D'", "B'"]]) # I
        oll1.append([self.front[1][2] == 3 and self.bottom[2][1] == 3 and self.bottom[1][2] == 3 and self.left[1][2] == 3, ["b", "R", "D", "R'", "D'", "b'"]]) # L

        oll1.append([self.bottom[1][0] == 3 and self.bottom[2][1] == 3 and self.bottom[1][2] == 3 and self.bottom[0][1] == 3 and self.bottom[2][0] == 3 and self.right[2][2] == 3 and self.back[0][0] == 3 and self.left[2][2] == 3, ["R", "D", "D", "R'", "D'", "R", "D'", "R'"]]) # Antisune
        oll1.append([self.bottom[1][0] == 3 and self.bottom[2][1] == 3 and self.bottom[1][2] == 3 and self.bottom[0][1] == 3 and self.right[0][2] == 3 and self.right[2][2] == 3 and self.left[0][2] == 3 and self.left[2][2] == 3, ["R", "D", "R'", "D", "R", "D'", "R'", "D", "R", "D", "D", "R'"]]) # H
        oll1.append([self.bottom[1][0] == 3 and self.bottom[2][1] == 3 and self.bottom[1][2] == 3 and self.bottom[0][1] == 3 and self.right[0][2] == 3 and self.bottom[2][2] == 3 and self.back[0][0] == 3 and self.bottom[0][0] == 3, ["B", "R'", "B'", "r", "D", "R", "D'", "r'"]]) # L
        oll1.append([self.bottom[1][0] == 3 and self.bottom[2][1] == 3 and self.bottom[1][2] == 3 and self.bottom[0][1] == 3 and self.front[2][2] == 3 and self.back[2][0] == 3 and self.left[0][2] == 3 and self.left[2][2] == 3, ["R", "D", "D", "R", "R", "D'", "R", "R", "D'", "R", "R", "D", "D", "R"]]) # Pi
        oll1.append([self.bottom[1][0] == 3 and self.bottom[2][1] == 3 and self.bottom[1][2] == 3 and self.bottom[0][1] == 3 and self.front[0][2] == 3 and self.right[0][2] == 3 and self.back[2][0] == 3 and self.bottom[0][2] == 3, ["R", "D", "R'", "D", "R", "D", "D", "R'"]]) # Sune

        moved = False
        while not moved:
            for oll in oll1:
                if oll[0]:
                    moved = True
                    self.doAlgorithm(oll[1])
            print(oll1)
            print(moved)
            if not moved:
                self.makeMove("D")
                oll1 = []
                oll1.append([self.front[1][2] == 3 and self.right[1][2] == 3 and self.back[1][0] == 3 and self.left[1][2] == 3, ["B", "R", "D", "R'", "D'", "B'", "b", "R", "D", "R'", "D'", "b'"]])  # dot
                oll1.append([self.front[1][2] == 3 and self.bottom[2][1] == 3 and self.back[1][0] == 3 and self.bottom[0][1] == 3, ["B", "R", "D", "R'", "D'", "B'"]])  # I
                oll1.append([self.front[1][2] == 3 and self.bottom[2][1] == 3 and self.bottom[1][2] == 3 and self.left[1][2] == 3, ["b", "R", "D", "R'", "D'", "b'"]])  # L

        print(self.solveMoves)
