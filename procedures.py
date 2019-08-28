import pygame
import os
import random


class Area:

    def __init__(self, x_area, width_area, y_window):
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

    def DrawArea(self, screen):
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

    def __init__(self, x_area, width_area, y_window, x_stars):
        '''Tworze gwiazdki'''
        super().__init__(x_area, width_area, y_window)
        self.x_stars = x_stars
        self.y_stars = random.randint(self.height_top + 50, self.height_bottom + (self.distance - 50))
        self.width_stars = 20
        self.height_stars = 20
        self.shape_stars = pygame.Rect(self.x_stars, self.y_stars, self.width_stars, self.height_stars)
        self.ImageStars = pygame.image.load(os.path.join('gwiazdka.png'))

    def DrawStars(self, screen):
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

    def DrawHelicopter(self, screen):
        '''Rysuje Helikopter'''
        screen.blit(self.ImageHelicopter, (self.x_position_helicopter, self.y_position_helicopter))

    def MoveHelicopter(self, v):
        '''Poruszam helikopter'''
        self.y_position_helicopter = self.y_position_helicopter + v
        self.shape_helicopter = pygame.Rect(self.x_position_helicopter, self.y_position_helicopter,
                                            self.height_helicopter, self.width_helicopter)


class Write:

    def __init__(self, x_window, y_window, screen):
        self.text = text
        self.size = size
        self.x_window = x_window
        self.y_window = y_window
        self.screen = screen
        self.file = file

    def WriteText(self, text, size):
        '''Tworze tekst wyskakujacy podczas gry'''
        self.font_text = pygame.font.SysFont('Arial', self.size)
        self.render_text = self.font_text.render(self.text, 1, (226, 216, 196))
        self.x_position = (self.x_window - self.render_text.get_rect().width) / 2
        self.y_position = (self.y_window - self.render_text.get_rect().height) / 2
        self.screen.blit(self.render_text, (self.x_position, self.y_position))

    def WriteTextSpace(self, text, size):
        '''Tworze tekst wyskakujacy podczas gry'''
        self.font_text = pygame.font.SysFont('Arial', self.size)
        self.render_text = self.font_text.render(self.text, 1, (226, 216, 196))
        self.x_position = (self.x_window - self.render_text.get_rect().width) / 2
        self.y_position = (self.y_window - self.render_text.get_rect().height) * 2 / 3
        self.screen.blit(self.render_text, (self.x_position, self.y_position))

    def WritePoints(self, text, size):
        '''Tworze tekst z ilością punktów'''
        self.font_text = pygame.font.SysFont('Arial', self.size)
        self.render_text = self.font_text.render(self.text, 1, (220, 220, 220))
        self.screen.blit(self.render_text, (20, 20))

    def WriteResults(self, text, size):
        '''Tworze wyniki na koniec gry'''
        self.font_text = pygame.font.SysFont('Arial', self.size)
        self.render_text = self.font_text.render(self.text, 1, (220, 220, 220))
        self.x_position = (self.x_window - self.render_text.get_rect().width) / 2
        self.y_position = (self.y_window - self.render_text.get_rect().height) * 3 / 4
        self.screen.blit(self.render_text, (self.x_position, self.y_position))

    def Logo(self, file):
        self.logo = pygame.image.load(os.path.join(self.file))
        self.x_logo = (self.x_window - self.logo.get_rect().width) / 2
        self.y_logo = (self.y_window * 2 / 3 - self.logo.get_rect().height) / 2
        self.screen.blit(self.logo, (self.x_logo, self.y_logo))


class Panel():

    def __init__(self, x_window, y_window, screen):
        self.x_window = x_window
        self.y_window = y_window
        self.screen = screen

    def StartPanel(self):
        Write.WriteText('HELIKOPTER', 42, self.x_window, self.y_window, self.screen)
        Write.WriteTextSpace('Start Gry - SPACE', 38, self.x_window, self.y_window, self.screen)
        Write.Logo('logo.jpg', self.x_window, self.y_window, self.screen)
        self.font_text = pygame.font.SysFont('Arial', 32)
        self.render_text = self.font_text.render('Najlepsze wyniki - t', 1, (220, 220, 220))
        self.x_position = (self.x_window - self.render_text.get_rect().width) / 2
        self.y_position = (self.y_window - self.render_text.get_rect().height) * 3 / 4 - 50
        self.screen.blit(self.render_text, (self.x_position, self.y_position + 50))

    def EndPanel(self):
        Write.Logo('logo.jpg', self.x_window, self.y_window, self.screen)
        Write.WriteText('Niestety przegrywasz', 42, self.x_window, self.y_window, self.screen)
        Write.WriteTextSpace('Naciśnij spację, aby zacząć gre', 42, self.x_window, self.y_window, self.screen)
        self.Write.WriteResults('Uzyskałeś {} punktów'.format(str(self.points_stars)), 30, self.x_window, self.y_window, self.screen)

    def LevelPanel(self):
        Write.Logo('logo.jpg', self.x_window, self.y_window, self.screen)
        Write.WriteText('Wybierz poziom trudności', 42, self.x_window, self.y_window, self.screen)
        self.font_text = pygame.font.SysFont('Arial', 42)
        self.render_text_easy = self.font_text.render('Easy - e', 1, (226, 216, 196))
        self.render_text_medium = self.font_text.render('Medium - m', 1, (226, 216, 196))
        self.render_text_hard = self.font_text.render('Hard - h', 1, (226, 216, 196))
        self.x_position = (self.x_window - self.render_text_medium.get_rect().width) / 2
        self.y_position = (self.y_window - self.render_text_medium.get_rect().height) * 3 / 4 - 50
        self.screen.blit(self.render_text_easy, (self.x_position + 20, self.y_position - 50))
        self.screen.blit(self.render_text_medium, (self.x_position - 10, self.y_position))
        self.screen.blit(self.render_text_hard, (self.x_position + 20, self.y_position + 50))
