import pygame
import os
import random
import math
import sys


def WriteText(text, size, x_window, y_window, screen):
    '''Tworze tekst wyskakujacy podczas gry'''
    font_text = pygame.font.SysFont('Arial', size)
    render_text = font_text.render(text, 1, (226, 216, 196))
    x_position = (x_window - render_text.get_rect().width) / 2
    y_position = (y_window - render_text.get_rect().height) / 2
    screen.blit(render_text, (x_position, y_position))


def WriteTextSpace(text, size, x_window, y_window, screen):
    '''Tworze tekst wyskakujacy podczas gry'''
    font_text = pygame.font.SysFont('Arial', size)
    render_text = font_text.render(text, 1, (226, 216, 196))
    x_position = (x_window - render_text.get_rect().width) / 2
    y_position = (y_window - render_text.get_rect().height) * 2 / 3
    screen.blit(render_text, (x_position, y_position))


def WritePoints(text, size, screen):
    '''Tworze tekst z ilością punktów'''
    font_text = pygame.font.SysFont('Arial', size)
    render_text = font_text.render(text, 1, (220, 220, 220))
    screen.blit(render_text, (20, 20))


def WriteResults(text, size, x_window, y_window, screen):
    '''Tworze wyniki na koniec gry'''
    font_text = pygame.font.SysFont('Arial', size)
    render_text = font_text.render(text, 1, (220, 220, 220))
    x_position = (x_window - render_text.get_rect().width) / 2
    y_position = (y_window - render_text.get_rect().height) * 3 / 4
    screen.blit(render_text, (x_position, y_position))


def SaveFileStatistic(points_level, points_stars):
    path = os.path.dirname(sys.argv[0])
    with open(path+'\statistic.ini', 'a+') as file:
        if points_level == 1:
            file.writelines((str(points_stars)+' easy')+'\n')
        elif points_level == 2:
            file.writelines((str(points_stars)+' medium')+'\n')
        elif points_level == 3:
            file.writelines((str(points_stars)+' hard')+'\n')


def OpenFileStatistic(x_window, y_window, screen):
    path = os.path.dirname(sys.argv[0])
    with open(path+'\statistic.ini', 'r+') as file:
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
    with open(path+'\statistic.ini', 'w+') as file:
        file.writelines('')

def Logo(file, x_window, y_window, screen):
    logo = pygame.image.load(os.path.join(file))
    x_logo = (x_window - logo.get_rect().width) / 2
    y_logo = (y_window * 2 / 3 - logo.get_rect().height) / 2
    screen.blit(logo, (x_logo, y_logo))


def StartPanel(x_window, y_window, screen):
    WriteText('HELIKOPTER', 42)
    WriteTextSpace('Start Gry - SPACE', 38)
    Logo('logo.jpg')
    font_text = pygame.font.SysFont('Arial', 32)
    render_text = font_text.render('Najlepsze wyniki - t', 1, (220, 220, 220))
    x_position = (x_window - render_text.get_rect().width) / 2
    y_position = (y_window - render_text.get_rect().height) * 3 / 4 - 50
    screen.blit(render_text, (x_position, y_position + 50))



def EndPanel(points_stars):
    Logo('logo.jpg')
    WriteText('Niestety przegrywasz', 42)
    WriteTextSpace('Naciśnij spację, aby zacząć gre', 42)
    WriteResults('Uzyskałeś {} punktów'.format(str(points_stars)), 30)


def LevelPanel(x_window, y_window, screen):
    Logo('logo.jpg')
    WriteText('Wybierz poziom trudności', 42)
    font_text = pygame.font.SysFont('Arial', 42)
    render_text_easy = font_text.render('Easy - e', 1, (226, 216, 196))
    render_text_medium = font_text.render('Medium - m', 1, (226, 216, 196))
    render_text_hard = font_text.render('Hard - h', 1, (226, 216, 196))
    x_position = (x_window - render_text_medium.get_rect().width) / 2
    y_position = (y_window - render_text_medium.get_rect().height) * 3 / 4 - 50
    screen.blit(render_text_easy, (x_position + 20, y_position - 50))
    screen.blit(render_text_medium, (x_position - 10, y_position))
    screen.blit(render_text_hard, (x_position + 20, y_position + 50))

'Do dokończenia = puste i nie wiem czy cos zrobie'
def StatisticsTablePanel():
    pass
    '''
    path = os.path.dirname(sys.argv[0])
    with open(path + '\statistic.ini', 'w+') as file:
        for line in file:
            font_text = pygame.font.SysFont('Arial', 32)
            render_text = font_text.render(str(line), 1, (255, 255, 255))
            screen.blit(render_text, (20, 20))
        #font_text = pygame.font.SysFont('Arial', 32)
        #render_text = font_text.render(str(file.write), 1, (220, 220, 220))
        #screen.blit(render_text, (20, 20))'''




