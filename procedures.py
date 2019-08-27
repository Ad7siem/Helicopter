import pygame
import os
import random
import math
import sys


pygame.init()

'''Rozmiar okna gry'''
x_window = 800
y_window = 800

'''Tworzę okno gry'''
screen = pygame.display.set_mode((x_window, y_window))

class Area:

    def __init__(self, x_area, width_area):
        '''Towrze górną i dolną granice przeszkód'''
        self.x_area = x_area
        self.width_area = width_area
        self.y_top = 0
        self.height_top = random.randint(200, 350)
        self.distance = random.randint(250, 350)
        self.y_bottom = self.height_top + self.distance
        self.height_bottom = y_window - self.y_bottom
        self.color_area = (70, 50, 0)
        self.shape_area_top = pygame.Rect(self.x_area, self.y_top, self.width_area, self.height_top)
        self.shape_area_botton = pygame.Rect(self.x_area, self.y_bottom, self.width_area, self.height_bottom)

    def DrawArea(self):
        '''Rysuje górną i dolną przeszkodę'''
        pygame.draw.rect(screen, self.color_area, self.shape_area_top, 0)
        pygame.draw.rect(screen, self.color_area, self.shape_area_botton, 0)

    def MoveArea(self, v):
        '''Wprowadzam przeszkody w ruch'''
        self.x_area = self.x_area - v
        self.shape_area_top = pygame.Rect(self.x_area, self.y_top, self.width_area, self.height_top)
        self.shape_area_botton = pygame.Rect(self.x_area, self.y_bottom, self.width_area, self.height_bottom)

    def CollisionArea(self, player):
        if self.shape_area_top.colliderect(player) or self.shape_area_botton.colliderect(player):
            return True
        else:
            return False


class Stars(Area):

    def __init__(self, x_area, width_area, x_stars):
        '''Tworze gwiazdki'''
        super().__init__(x_area, width_area)
        self.x_stars = x_stars
        self.y_stars = random.randint(self.height_top + 50, self.height_bottom + (self.distance - 50))
        self.width_stars = 20
        self.height_stars = 20
        self.shape_stars = pygame.Rect(self.x_stars, self.y_stars, self.width_stars, self.height_stars)
        self.ImageStars = pygame.image.load(os.path.join('gwiazdka.png'))

    def DrawStars(self):
        '''Rysuje gwiazdki'''
        screen.blit(self.ImageStars, (self.x_stars, self.y_stars))

    def MoveStars(self, v):
        '''Napędzam gwiazdki'''
        self.x_stars = self.x_stars - v
        self.shape_stars = pygame.Rect(self.x_stars, self.y_stars, self.width_stars, self.height_stars)

    def CollisionStars(self, player):
        if self.shape_stars.colliderect(player):
            return True
        else:
            return False


class Helicopter:

    def __init__(self, x_position_helicopter, y_position_helicopter):
        '''Tworze helikopter'''
        self.x_position_helicopter = x_position_helicopter
        self.y_position_helicopter = y_position_helicopter
        self.height_helicopter = 40
        self.width_helicopter = 40
        self.shape_helicopter = pygame.Rect(self.x_position_helicopter, self.y_position_helicopter,
                                            self.width_helicopter, self.height_helicopter)
        self.ImageHelicopter = pygame.image.load(os.path.join('helikopter.png'))

    def DrawHelicopter(self):
        '''Rysuje Helikopter'''
        screen.blit(self.ImageHelicopter, (self.x_position_helicopter, self.y_position_helicopter))

    def MoveHelicopter(self, v):
        '''Poruszam helikopter'''
        self.y_position_helicopter = self.y_position_helicopter + v
        self.shape_helicopter = pygame.Rect(self.x_position_helicopter, self.y_position_helicopter,
                                            self.height_helicopter, self.width_helicopter)

'''Tworzę listę przeszkód'''
objects_stars = []
objects_area = []
for i in range(21):
    objects_area.append(Area(i * x_window / 20, x_window / 20))
    objects_stars.append(Stars(i * x_window / 20, x_window / 20, i * x_window / 20))

'''Tworzenie gracza'''
players = Helicopter(y_window / 2, x_window / 2)
# namePlayers = input('Name:')
dy = 0
shows = 'menu'
