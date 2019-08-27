'''
Nie chce mi sie juz dalej dzisiaj nad tym siedziec

1. wywala blad sRGB
2. zrobic klase zapisu do pliku i tworzenia tablicy

'''
from function import *
from procedures import *
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

while True:
    '''Funkcja wyłączenia gry'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                dy = -1
            elif event.key == pygame.K_DOWN:
                dy = 1
            elif event.key == pygame.K_SPACE:
                if shows == 'menu':
                    players = Helicopter(y_window / 2, x_window / 2)
                    shows = 'level'
                    points = 0
                    points_stars = 0
                    points_level = 0
                elif shows == 'end':
                    shows = 'menu'
                else:
                    pass
            elif event.key == pygame.K_e:
                if shows == 'level':
                    speed = 1 / 2
                    shows = 'game'
                    points_level = 1
            elif event.key == pygame.K_m:
                if shows == 'level':
                    speed = 1
                    shows = 'game'
                    points_level = 2
            elif event.key == pygame.K_h:
                if shows == 'level':
                    speed = 3 / 2
                    shows = 'game'
                    points_level = 3
            elif event.key == pygame.K_t:
                if shows == 'menu':
                    shows = 'statistic'
            elif event.key == pygame.K_w:
                if shows == 'statistic':
                    ResertStatistic()
            elif event.key == pygame.K_BACKSPACE:
                if shows == 'statistic':
                    shows = 'menu'
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or pygame.K_DOWN:
                dy = 0

    '''Panel gry'''
    screen.fill((100, 100, 100))
    if shows == 'menu':
        StartPanel()

    elif shows == 'game':

        for obj_area in objects_area:
            obj_area.MoveArea(speed)
            obj_area.DrawArea()

            if obj_area.CollisionArea(players.shape_helicopter):
                shows = 'end'
                SaveFileStatistic(points_level, points_stars)

        for obj_area in objects_area:

            if obj_area.x_area <= -obj_area.width_area:
                objects_area.remove(obj_area)
                objects_area.append(Area(x_window, x_window / 20))

        for obj_star in objects_stars:
            obj_star.MoveStars(speed)
            obj_star.DrawStars()

            if obj_star.CollisionStars(players.shape_helicopter):
                points_stars = points_stars + (1 * points_level)
                objects_stars.remove(obj_star)
                objects_stars.append(Stars(0, 0, x_window))

        for obj_star in objects_stars:

            if obj_star.x_stars <= -obj_star.width_stars:
                objects_stars.remove(obj_star)
                objects_stars.append(Stars(0, 0, x_window))

        players.DrawHelicopter()
        players.MoveHelicopter(dy)
        WritePoints('Punkty: {}'.format(str(points_stars)), 20)

    elif shows == 'level':
        LevelPanel()

    elif shows == 'statistic':
        OpenFileStatistic()

    elif shows == 'end':
        EndPanel(points_stars)

    pygame.display.update()
