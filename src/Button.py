import pygame

class Button:
    def __init__(self, screen, x, y, width, height, color):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

        self.isHovered = False
        self.animationSize = 0
        self.maxAnimationSize = 20

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x-(self.animationSize/2), self.y-(self.animationSize/2), self.width+self.animationSize, self.height+self.animationSize))

    def update(self):
        if self.isHovered:
            self.animationSize += 2
        else:
            self.animationSize -= 2

        if self.animationSize > self.maxAnimationSize:
            self.animationSize = self.maxAnimationSize
        elif self.animationSize < 0:
            self.animationSize = 0

    def clicked(self,mx, my):
        return False

    def hover(self, mx, my):
        temp = pygame.Rect(self.x-(self.animationSize/2), self.y-(self.animationSize/2), self.width+self.animationSize, self.height+self.animationSize)
        self.isHovered = temp.collidepoint((mx, my))
        return self.isHovered

