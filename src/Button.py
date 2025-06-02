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
        pass

    def clicked(self):
        return False

    def hover(self):
        return False

