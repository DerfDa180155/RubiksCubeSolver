import random


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
            self.solveMoves.append(move[:1])
        match move:
            case "UP" | "U":
                self.top = self.rotate(self.top, True)
                self.rotateAdjacent(self.back, [[0,2],[1,2],[2,2]], self.right, [[2,0],[1,0],[0,0]], self.front, [[2,0],[1,0],[0,0]], self.left, [[2,0],[1,0],[0,0]])
            case "U'":
                self.top = self.rotate(self.top, False)
            case "Front" | "F":
                self.front = self.rotate(self.front, True)
                self.rotateAdjacent(self.top, [[0,2],[1,2],[2,2]], self.right, [[0,0],[0,1],[0,2]], self.bottom, [[2,0],[1,0],[0,0]], self.left, [[2,2],[2,1],[2,0]])
            case "F'":
                self.front = self.rotate(self.front, False)
            case "Down" | "D":
                self.bottom = self.rotate(self.bottom, True)
                self.rotateAdjacent(self.front, [[0,2],[1,2],[2,2]], self.right, [[0,2],[1,2],[2,2]], self.back, [[2,0],[1,0],[0,0]], self.left, [[0,2],[1,2],[2,2]])
            case "D'":
                self.bottom = self.rotate(self.bottom, False)
            case "Back" | "B":
                self.back = self.rotate(self.back, True)
                self.rotateAdjacent(self.bottom, [[0,2],[1,2],[2,2]], self.right, [[2,2],[2,1],[2,0]], self.top, [[2,0],[1,0],[0,0]], self.left, [[0,0],[0,1],[0,2]])
            case "B'":
                self.back = self.rotate(self.back, False)
            case "Left" | "L":
                self.left = self.rotate(self.left, True)
                self.rotateAdjacent(self.top, [[0,0],[0,1],[0,2]], self.front, [[0,0],[0,1],[0,2]], self.bottom, [[0,0],[0,1],[0,2]], self.back, [[0,0],[0,1],[0,2]])
            case "L'":
                self.left = self.rotate(self.left, False)
            case "Right" | "R":
                self.right = self.rotate(self.right, True)
                self.rotateAdjacent(self.top, [[2,2],[2,1],[2,0]], self.back, [[2,2],[2,1],[2,0]], self.bottom, [[2,2],[2,1],[2,0]], self.front, [[2,2],[2,1],[2,0]])
            case "R'":
                self.right = self.rotate(self.right, False)

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

    def solveState(self):
        match self.state:
            case 0: # cross
                if self.top[1][0] == 1 and self.top[2][1] == 1 and self.top[1][2] == 1 and self.top[0][1] == 1 and self.back[1][2] == 4 and self.right[1][0] == 6 and self.front[1][0] == 2 and self.left[1][0] == 5:
                    self.state += 1
            case 1: # corners
                if self.top[0][0] == 1 and self.top[2][0] == 1 and self.top[2][2] == 1 and self.top[0][2] == 1 and self.back[2][2] == 4 and self.back[0][2] == 4 and self.right[2][0] == 6 and self.right[0][0] == 6 and self.front[2][0] == 2 and self.front[0][0] == 2 and self.left[2][0] == 5 and self.left[0][0] == 5:
                    self.state += 1
            case 2: # 2nd layer
                if self.front[2][1] == 2 and self.front[0][1] == 2 and self.left[2][1] == 5 and self.left[0][1] == 5 and self.back[0][1] == 4 and self.back[2][1] == 4 and self.right[2][1] == 6 and self.right[0][2] == 6:
                    self.state += 1
            case 3: # OLL
                if self.bottom[0][0] == 3 and self.bottom[1][0] == 3 and self.bottom[2][0] == 3 and self.bottom[2][1] == 3 and self.bottom[2][2] == 3 and self.bottom[1][2] == 3 and self.bottom[0][2] == 3 and self.bottom[0][1] == 3:
                    self.state += 1
            case 4: # PLL
                if self.front[0][2] == 2 and self.front[1][2] == 2 and self.front[2][2] == 2 and self.left[0][2] == 5 and self.left[1][2] == 5 and self.left[2][2] == 5 and self.back[2][0] == 4 and self.back[1][0] == 4 and self.back[0][0] == 4 and self.right[0][2] == 6 and self.right[1][2] == 6 and self.right[2][2] == 6:
                    self.state += 1

    def solve(self):
        self.solveState()

