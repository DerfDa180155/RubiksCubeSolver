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
        self.maxAnimationSize = 10

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x-self.animationSize, self.y-self.animationSize, self.width+self.animationSize, self.height+self.animationSize))

    def update(self):
        if self.isHovered:
            self.animationSize += 1
        else:
            self.animationSize -= 1

        if self.animationSize > self.maxAnimationSize:
            self.animationSize = self.maxAnimationSize
        elif self.animationSize < 0:
            self.animationSize = 0

    def clicked(self):
        return False

    def hover(self, mx, my):
        temp = pygame.rect
        temp.Rect.x = self.x
        temp.Rect.y = self.y
        temp.Rect.width = self.width
        temp.Rect.height = self.height
        self.isHovered = temp.Rect.collidepoint(mx, my)
        return self.isHovered

