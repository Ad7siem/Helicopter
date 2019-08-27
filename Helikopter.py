'''
Nie chce mi sie juz dalej dzisiaj nad tym siedziec

1. wywala blad sRGB

'''

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


def WriteText(text, size):
    '''Tworze tekst wyskakujacy podczas gry'''
    font_text = pygame.font.SysFont('Arial', size)
    render_text = font_text.render(text, 1, (226, 216, 196))
    x_position = (x_window - render_text.get_rect().width) / 2
    y_position = (y_window - render_text.get_rect().height) / 2
    screen.blit(render_text, (x_position, y_position))


def WriteTextSpace(text, size):
    '''Tworze tekst wyskakujacy podczas gry'''
    font_text = pygame.font.SysFont('Arial', size)
    render_text = font_text.render(text, 1, (226, 216, 196))
    x_position = (x_window - render_text.get_rect().width) / 2
    y_position = (y_window - render_text.get_rect().height) * 2 / 3
    screen.blit(render_text, (x_position, y_position))


def WritePoints(text, size):
    '''Tworze tekst z ilością punktów'''
    font_text = pygame.font.SysFont('Arial', size)
    render_text = font_text.render(text, 1, (220, 220, 220))
    screen.blit(render_text, (20, 20))


def WriteResults(text, size):
    '''Tworze wyniki na koniec gry'''
    font_text = pygame.font.SysFont('Arial', size)
    render_text = font_text.render(text, 1, (220, 220, 220))
    x_position = (x_window - render_text.get_rect().width) / 2
    y_position = (y_window - render_text.get_rect().height) * 3 / 4
    screen.blit(render_text, (x_position, y_position))

'Do dokończenia'
def SaveFileStatistic():
    path = os.path.dirname(sys.argv[0])
    with open(path+'\statistic.ini', 'a+') as file:
        if points_level == 1:
            file.writelines((str(points_stars)+' easy')+'\n')
        elif points_level == 2:
            file.writelines((str(points_stars)+' medium')+'\n')
        elif points_level == 3:
            file.writelines((str(points_stars)+' hard')+'\n')


def OpenFileStatistic():
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

def Logo(file):
    logo = pygame.image.load(os.path.join(file))
    x_logo = (x_window - logo.get_rect().width) / 2
    y_logo = (y_window * 2 / 3 - logo.get_rect().height) / 2
    screen.blit(logo, (x_logo, y_logo))


def StartPanel():
    WriteText('HELIKOPTER', 42)
    WriteTextSpace('Start Gry - SPACE', 38)
    Logo('logo.jpg')
    font_text = pygame.font.SysFont('Arial', 32)
    render_text = font_text.render('Najlepsze wyniki - t', 1, (220, 220, 220))
    x_position = (x_window - render_text.get_rect().width) / 2
    y_position = (y_window - render_text.get_rect().height) * 3 / 4 - 50
    screen.blit(render_text, (x_position, y_position + 50))



def EndPanel():
    Logo('logo.jpg')
    WriteText('Niestety przegrywasz', 42)
    WriteTextSpace('Naciśnij spację, aby zacząć gre', 42)
    WriteResults('Uzyskałeś {} punktów'.format(str(points_stars)), 30)


def LevelPanel():
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
                SaveFileStatistic()

        for obj_area in objects_area:

            if obj_area.x_area <= -obj_area.width_area:
                objects_area.remove(obj_area)
                objects_area.append(Area(x_window, x_window / 20))
                #points = points + math.fabs(dy)

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
        #StatisticsTablePanel()
        OpenFileStatistic()

    elif shows == 'end':
        EndPanel()

    pygame.display.update()
