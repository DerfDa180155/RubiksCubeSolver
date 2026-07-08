import random

import pygame
import random

class SwitchButton:
    def __init__(self, screen, x, y, width, height, color, action1, action2):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.action1 = action1
        self.action2 = action2

        self.action = action1

        self.isHovered = False
        self.isLeftClicked = False
        self.isRightClicked = False


    def toggleSwitch(self):
        if self.action == self.action1:
            self.action = self.action2
        else:
            self.action = self.action1

    def draw(self, textColor, toggleColor):
        # draw button background
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))

        borderSize = self.height/10
        if self.action == self.action1:
            pygame.draw.rect(self.screen, toggleColor, (self.x+borderSize, self.y+borderSize, (self.width/2)-borderSize*2, self.height-borderSize*2))
        else:
            pygame.draw.rect(self.screen, toggleColor, (self.x+borderSize+self.width/2, self.y+borderSize, (self.width/2)-borderSize*2, self.height-borderSize*2))

        # line
        pygame.draw.rect(self.screen, textColor, (self.x+self.width/2-1, self.y+borderSize, 2, self.height-borderSize*2))

        # draw text
        font = pygame.font.Font(pygame.font.get_default_font(), 20)

        # left action
        text = font.render(self.action1, True, textColor)
        newRect = text.get_rect()
        newRect.centerx = self.x + self.width/4
        newRect.centery = self.y + self.height/2 + 2
        self.screen.blit(text, newRect)

        # right action
        text = font.render(self.action2, True, textColor)
        newRect = text.get_rect()
        newRect.centerx = self.x + (self.width / 4) * 3
        newRect.centery = self.y + self.height / 2 + 2
        self.screen.blit(text, newRect)

    def clicked(self, mx, my, mouseClick):
        if self.hover(mx, my) and mouseClick[0]:
            self.isLeftClicked = True
        elif self.hover(mx, my) and mouseClick[2]:
            self.isRightClicked = True
        else:
            self.isLeftClicked = False
            self.isRightClicked = False

        if self.isLeftClicked:
            self.toggleSwitch()

        return self.isLeftClicked

    def hover(self, mx, my):
        temp = pygame.Rect(self.x, self.y, self.width, self.height)
        self.isHovered = temp.collidepoint((mx, my))
        return self.isHovered

