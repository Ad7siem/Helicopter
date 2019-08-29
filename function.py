import pygame
import os
import sys


def SaveFileStatistic(points_level, points_stars):
    path = os.path.dirname(sys.argv[0])
    with open(path + '\statistic.ini', 'a+') as file:
        if points_level == 1:
            file.writelines((str(points_stars) + ' easy') + '\n')
        elif points_level == 2:
            file.writelines((str(points_stars) + ' medium') + '\n')
        elif points_level == 3:
            file.writelines((str(points_stars) + ' hard') + '\n')


def OpenFileStatistic(x_window, y_window, screen):
    path = os.path.dirname(sys.argv[0])
    with open(path + '\statistic.ini', 'r+') as file:
        size = 24
        x_position = (x_window - size) * 1 / 5
        y_position = (y_window - size) * 1 / 5
        for line in file:
            parts = line.replace('\n', '')
            font_text = pygame.font.SysFont('Arial', size)
            render_text = font_text.render(str(parts), 1, (220, 220, 220))
            screen.blit(render_text, (x_position, y_position))
            y_position = y_position + 35


def ResertStatistic():
    path = os.path.dirname(sys.argv[0])
    with open(path + '\statistic.ini', 'w+') as file:
        file.writelines('')
