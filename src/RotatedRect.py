import pygame
import random

class RotatedRect:
    def __init__(self, screen, location, size, degree, color):
        self.screen = screen
        self.location = location
        self.size = size
        self.degree = degree
        self.color = color

        self.randomLocation = [(random.randint(location[0], location[1]))-(size[0]/2), (random.randint(location[2], location[3]))-(size[1]/2)]
        self.randomLocation = [(location[0]+(location[1]-location[0])/2)-(size[0]/2), (location[2]+(location[3]-location[2])/2)-(size[1]/2)]

        surf = pygame.Surface(size, pygame.SRCALPHA)
        pygame.draw.rect(surf, self.color, (0, 0, self.size[0], self.size[1]))

        self.rotated = pygame.transform.rotate(surf, degree)

    def draw(self):
        self.screen.blit(self.rotated, self.randomLocation)