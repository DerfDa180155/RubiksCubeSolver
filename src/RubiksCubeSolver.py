

class RubiksCubeSolver:
    def __init__(self):
        self.top = self.generateEmptySide(middle=1)
        self.bottom = self.generateEmptySide(middle=3)
        self.right = self.generateEmptySide(middle=6)
        self.left = self.generateEmptySide(middle=5)
        self.front = self.generateEmptySide(middle=2)
        self.back = self.generateEmptySide(middle=4)

        for i in range(1, 7):
            self.fillSide(i)

    def reset(self):
        self.top = self.generateEmptySide(middle=1)
        self.bottom = self.generateEmptySide(middle=3)
        self.right = self.generateEmptySide(middle=6)
        self.left = self.generateEmptySide(middle=5)
        self.front = self.generateEmptySide(middle=2)
        self.back = self.generateEmptySide(middle=4)

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

    def makeMove(self, move):
        match move:
            case "UP":
                self.top = self.rotate(self.top)
            case "Front":
                pass
            case "Down":
                pass
            case "Back":
                pass
            case "Left":
                pass
            case "Right":
                pass

    def rotate(self, side):
        newSide = self.generateEmptySide(side[1][1])
        corners = [[0,0], [0,2], [2,2], [2,0]]
        edges = [[0,1], [1,2], [2,1], [1,0]]

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

    def solve(self):
        pass

