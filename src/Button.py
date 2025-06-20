import pygame

class Button:
    def __init__(self, screen, x, y, width, height, color, onClick):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.onClick = onClick

        self.isHovered = False
        self.isClicked = False
        self.animationSize = 0
        self.maxAnimationSize = 20

    def reset(self):
        self.isHovered = False
        self.isClicked = False
        self.animationSize = 0
        self.maxAnimationSize = 20

    def updateLocationAndSize(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

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

    def clicked(self, mx, my, mouseClick):
        if self.hover(mx, my) and mouseClick[0]:
            self.isClicked = True
        else:
            self.isClicked = False
        return self.isClicked

    def hover(self, mx, my):
        temp = pygame.Rect(self.x-(self.animationSize/2), self.y-(self.animationSize/2), self.width+self.animationSize, self.height+self.animationSize)
        self.isHovered = temp.collidepoint((mx, my))
        return self.isHovered

