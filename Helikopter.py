'''
1. wywala blad sRGB
'''
from function import *
from procedures import *
import pygame


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
    objects_area.append(Area(i * x_window / 20, x_window / 20, y_window))
    objects_stars.append(Stars(i * x_window / 20, x_window / 20, y_window, i * x_window / 20))

'''Tworzenie gracza'''
players = Helicopter(y_window / 2, x_window / 2)

dy = 0
shows = 'menu'

file = File(FilePath())

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
                if shows == 'statistic' or shows == 'level':
                    shows = 'menu'
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or pygame.K_DOWN:
                dy = 0

    '''Panel gry'''
    screen.fill((0, 0, 0))
    panel = Panel(FilePath(), x_window, y_window, screen)
    write = Write(FilePath(), x_window, y_window, screen)
    if shows == 'menu':
        panel.StartPanel()

    elif shows == 'game':

        for obj_area in objects_area:
            obj_area.MoveArea(speed)
            obj_area.DrawArea(screen)

            if obj_area.CollisionArea(players.shape_helicopter):
                shows = 'end'
                if points_level == 1:
                    file.WriteParameter('level', 'easy')
                elif points_level == 2:
                    file.WriteParameter('level', 'medium')
                elif points_level == 3:
                    file.WriteParameter('level', 'hard')
                file.WriteParameter('value', points_stars)
                file.SaveOnDisk()

        for obj_area in objects_area:

            if obj_area.x_area <= -obj_area.width_area:
                objects_area.remove(obj_area)
                objects_area.append(Area(x_window, x_window / 20, y_window))

        for obj_star in objects_stars:
            obj_star.MoveStars(speed)
            obj_star.DrawStars(screen)

            if obj_star.CollisionStars(players.shape_helicopter):
                points_stars = points_stars + (1 * points_level)
                objects_stars.remove(obj_star)
                objects_stars.append(Stars(0, 0, y_window, x_window))

        for obj_star in objects_stars:

            if obj_star.x_stars <= -obj_star.width_stars:
                objects_stars.remove(obj_star)
                objects_stars.append(Stars(0, 0,y_window, x_window))

        players.DrawHelicopter(screen)
        players.MoveHelicopter(dy)
        write.WritePoints('Punkty: {}'.format(str(points_stars)), 20)

    elif shows == 'level':
        panel.LevelPanel()

    elif shows == 'statistic':
        panel.StatisticsTablePanel()

    elif shows == 'end':
        panel.EndPanel(points_stars)

    pygame.display.update()
