import pygame
import os
import sys
import itertools


def SaveFileStatistic(points_level, points_stars):
    path = os.path.dirname(sys.argv[0])
    with open(path + '\statistic.ini', 'a+') as file:
        if points_level == 1:
            #s = {}
            #s['easy'] = points_stars
            s = 'easy: {}\n'.format(points_stars)
            file.writelines('{}'.format(s).upper())
        elif points_level == 2:
            #s = {'medium':''}
            #s['medium'] = points_stars
            s = 'medium: {}\n'.format(points_stars)
            file.writelines('{}'.format(s).upper())
        elif points_level == 3:
            #s = {'hard':''}
            #s['hard'] = points_stars
            s = 'hard: {}\n'.format(points_stars)
            file.writelines('{}'.format(s).upper())


def OpenFileStatistic(x_window, y_window, screen):
    path = os.path.dirname(sys.argv[0])
    """table = {}
    with open(path + '\statistic.ini', 'r+') as file:

        for line in file:
            elements = line.replace('\n','').split(':')
            d = {'level' : elements[0], 'value' : elements[1]}
            table.append(d)

    size = 24
    x_position = (x_window - size) * 1 / 5
    y_position = (y_window - size) * 1 / 5
        #for line in file:
         #   parts = line.replace('\n', '').replace(' ', '           ')
            #parts = line

    #table = sorted(table, key = lambda x: x > 0)

    for key, elements in itertools.groupby(table, key=lambda x: x['value']):

        font_text = pygame.font.SysFont('Arial', 18)
        render_text = font_text.render('{}'.format(table[key]), 1, (220, 220, 220))
        screen.blit(render_text, (x_position, y_position))
        print(key, list(elements))
        y_position = y_position + 35

    """

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
            """
    with open(path + '\statistic.ini', 'r+') as file:
        size = 24
        x_position = (x_window - size) * 1 / 5
        y_position = (y_window - size) * 1 / 5
        for line in file:
            d = []
            d.append(line)
            parts = line.replace('\n', '')
            font_text = pygame.font.SysFont('Arial', size)
            render_text = font_text.render(char+' '+n, 1, (220, 220, 220))
            screen.blit(render_text, (x_position, y_position))
            y_position = y_position + 35
"""

def ResertStatistic():
    path = os.path.dirname(sys.argv[0])
    with open(path + '\statistic.ini', 'w+') as file:
        file.writelines('')
