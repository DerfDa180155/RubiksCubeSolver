import random

import pygame
import random

class Button:
    def __init__(self, screen, x, y, width, height, color, onClick, doAnimation = True, maxAnimationSize = 20):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.onClick = onClick
        self.doAnimation = doAnimation

        availableColors = [(255, 255, 255), (0, 0, 255), (255, 255, 0), (0, 255, 0), (180, 0, 0), (255, 165, 0)]
        self.onClickTextColor = availableColors[random.randint(0, len(availableColors)-1)]

        self.isHovered = False
        self.isleftClicked = False
        self.isrightClicked = False
        self.animationSize = 0
        self.maxAnimationSize = maxAnimationSize

        self.groupUpdate = False

    def reset(self):
        self.isHovered = False
        self.isleftClicked = False
        self.isrightClicked = False
        self.animationSize = 0

    def updateLocationAndSize(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, drawOnClickText=False, onClickTextSize=20):
        pygame.draw.rect(self.screen, self.color, (self.x-(self.animationSize/2), self.y-(self.animationSize/2), self.width+self.animationSize, self.height+self.animationSize))

        if drawOnClickText:
            font = pygame.font.Font(pygame.font.get_default_font(), int(onClickTextSize+self.animationSize/1.5))

            text = font.render(self.onClick, True, self.onClickTextColor)
            newRect = text.get_rect()
            newRect.centerx = self.x + self.width/2
            newRect.centery = self.y + self.height/2
            self.screen.blit(text, newRect)


    def update(self):
        if not self.groupUpdate:
            if self.doAnimation:
                if self.isHovered:
                    self.animationSize += 2
                else:
                    self.animationSize -= 2

                if self.animationSize > self.maxAnimationSize:
                    self.animationSize = self.maxAnimationSize
                elif self.animationSize < 0:
                    self.animationSize = 0
            else:
                if not self.isHovered:
                    self.animationSize -= 2
                if self.animationSize < 0:
                    self.animationSize = 0

    def doAnimationDef(self):
        temp = self.doAnimation
        self.doAnimation = True
        self.isHovered = True
        self.groupUpdate = False
        self.update()
        self.groupUpdate = True
        self.doAnimation = temp

    def animateGroup(self, buttons):
        for btn in buttons:
            btn.doAnimationDef()

    def clicked(self, mx, my, mouseClick):
        if self.hover(mx, my) and mouseClick[0]:
            self.isleftClicked = True
        elif self.hover(mx, my) and mouseClick[2]:
            self.isrightClicked = True
        else:
            self.isleftClicked = False
            self.isrightClicked = False
        return self.isleftClicked

    def hover(self, mx, my):
        temp = pygame.Rect(self.x-(self.animationSize/2), self.y-(self.animationSize/2), self.width+self.animationSize, self.height+self.animationSize)
        self.isHovered = temp.collidepoint((mx, my))
        return self.isHovered

