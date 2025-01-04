

class RubiksCubeSolver:
    def __init__(self):
        self.top = self.generateEmptySide(middle=1)
        self.bottom = self.generateEmptySide(middle=3)
        self.right = self.generateEmptySide(middle=6)
        self.left = self.generateEmptySide(middle=5)
        self.front = self.generateEmptySide(middle=2)
        self.back = self.generateEmptySide(middle=4)

    def reset(self):
        self.top = self.generateEmptySide(middle=1)
        self.bottom = self.generateEmptySide(middle=3)
        self.right = self.generateEmptySide(middle=6)
        self.left = self.generateEmptySide(middle=5)
        self.front = self.generateEmptySide(middle=2)
        self.back = self.generateEmptySide(middle=4)

    def generateEmptySide(self, middle):
        side = []
        for i in range(3):
            if i == 1:
                side.append([0,middle,0])
            else:
                side.append([0,0,0])
        return side

    def generateComplete(self):
        complite =  []

        for i in range(3):
            temp = []
            for j in range(3):
                temp.append(0)
            for j in range(3):
                temp.append(self.top[j][i])
            for j in range(3):
                temp.append(0)
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
                temp.append(0)
            for j in range(3):
                temp.append(self.bottom[j][i])
            for j in range(3):
                temp.append(0)
            complite.append(temp)

        for i in range(3):
            temp = []
            for j in range(3):
                temp.append(0)
            for j in range(3):
                temp.append(self.back[j][i])
            for j in range(3):
                temp.append(0)
            complite.append(temp)

        return complite

    def solve(self):
        pass

