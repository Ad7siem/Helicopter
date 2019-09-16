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



class File:

    def __init__(self, path):
        self.path = path
        #self.parameter = {}
        self.parameters = {}
        self.ReadFromDisk()

    def ReadFromDisk(self):
        if os.path.isfile(self.path):
            self.tablica = []
            with open(self.path) as file:
                for line in file:
                    parts = line.replace('\n', '').split('=')
                    self.parameters[parts[0]] = parts[1]
                    self.tablica.append(self.parameters)
                #print(self.tablica)

    def ReadParameter(self, key):
        if key in self.parameters.keys():
            return self.parameters[key]
        else:
            return None

    def WriteParameter(self, key, value):
            self.parameters[key] = value

    def SaveOnDisk(self):
        with open(self.path, 'a+') as file:
            for key, value in self.parameters.items():
                line = '{}={}\n'.format(key, value)
                file.writelines(line)

class Write(File):

    def __init__(self, path, x_window, y_window, screen):
        super().__init__(path)
        self.x_window = x_window
        self.y_window = y_window
        self.screen = screen
        self.file = File(self.path)

    def WriteText(self, text, size):
        '''Tworze tekst wyskakujacy podczas gry'''
        self.text = text
        self.size = size
        self.font_text = pygame.font.SysFont('Arial', self.size)
        self.render_text = self.font_text.render(self.text, 1, (156, 146, 126))
        self.x_position = (self.x_window - self.render_text.get_rect().width) / 2
        self.y_position = (self.y_window - self.render_text.get_rect().height) / 2
        self.screen.blit(self.render_text, (self.x_position, self.y_position))

    def WriteTextSpace(self, text, size):
        '''Tworze tekst wyskakujacy podczas gry'''
        self.text = text
        self.size = size
        self.font_text = pygame.font.SysFont('Arial', self.size)
        self.render_text = self.font_text.render(self.text, 1, (226, 216, 196))
        self.x_position = (self.x_window - self.render_text.get_rect().width) / 2
        self.y_position = (self.y_window - self.render_text.get_rect().height) * 2 / 3
        self.screen.blit(self.render_text, (self.x_position, self.y_position))

    def WritePoints(self, text, size):
        '''Tworze tekst z ilością punktów'''
        self.text = text
        self.size = size
        self.font_text = pygame.font.SysFont('Arial', self.size)
        self.render_text = self.font_text.render(self.text, 1, (220, 220, 220))
        self.screen.blit(self.render_text, (20, 20))

    def WriteResults(self, text, size):
        '''Tworze wyniki na koniec gry'''
        self.text = text
        self.size = size
        self.font_text = pygame.font.SysFont('Arial', self.size)
        self.render_text = self.font_text.render(self.text, 1, (220, 220, 220))
        self.x_position = (self.x_window - self.render_text.get_rect().width) / 2
        self.y_position = (self.y_window - self.render_text.get_rect().height) * 3 / 4
        self.screen.blit(self.render_text, (self.x_position, self.y_position))

    def Logo(self, file):
        self.file = file
        self.logo = pygame.image.load(os.path.join(self.file))
        self.x_logo = (self.x_window - self.logo.get_rect().width) / 2
        self.y_logo = (self.y_window * 2 / 3 - self.logo.get_rect().height) / 2
        self.screen.blit(self.logo, (self.x_logo, self.y_logo))

    def WriteStatistic(self, size):
        self.size = size
        self.font_text = pygame.font.SysFont('Arial', self.size)
        self.render_text_value = self.font_text.render(self.file.ReadParameter('value'), 1, (220, 220, 220))
        self.render_text_level = self.font_text.render(self.file.ReadParameter('level'), 1, (220, 220, 220))
        self.x_position_level = (self.x_window - self.render_text_level.get_rect().width) * 1 / 3
        self.y_position_level = (self.y_window - self.render_text_level.get_rect().height) * 1 / 4
        self.x_position_value = (self.x_window - self.render_text_value.get_rect().width) * 2 / 3
        self.y_position_value = (self.y_window - self.render_text_value.get_rect().height) * 1 / 4
        self.screen.blit(self.render_text_value, (self.x_position_value, self.y_position_value))
        self.screen.blit(self.render_text_level, (self.x_position_level, self.y_position_level))

        self.render_text = self.font_text.render('Poziom:', 1, (220, 220, 220))
        self.x_position = (self.x_window - self.render_text.get_rect().width) * 1 / 3
        self.y_position = (self.y_window - self.render_text.get_rect().height) * 1 / 5
        self.screen.blit(self.render_text, (self.x_position, self.y_position))

        self.render_text = self.font_text.render('Punkty:', 1, (220, 220, 220))
        self.x_position = (self.x_window - self.render_text.get_rect().width) * 2 / 3
        self.y_position = (self.y_window - self.render_text.get_rect().height) * 1 / 5
        self.screen.blit(self.render_text, (self.x_position, self.y_position))

    def WriteOther(self, text, size, x_window, y_window, color):
        self.text = text
        self.size = size
        self.x_position = x_window
        self.y_position = y_window
        self. font_text = pygame.font.SysFont('Arial', self.size)
        self.render_text = self.font_text.render(self.text, 1, (color))
        self.screen.blit(self.render_text, (self.x_position, self.y_position))


class Panel(File):

    def __init__(self, path, x_window, y_window, screen):
        super().__init__(path)
        self.x_window = x_window
        self.y_window = y_window
        self.screen = screen
        self.write = Write(self.path, self.x_window, self.y_window, self.screen)


    def StartPanel(self):
        self.write.WriteText('HELIKOPTER', 72)
        self.write.WriteTextSpace('Start Gry - SPACE'.upper(), 38)
        self.write.Logo('logo.jpg')
        self.write.WriteOther('Najlepszy wynik - t'.upper(), 28, x_window=(self.x_window)*3.5/10, y_window=(self.y_window)*7/10, color=(226, 216, 196))
        self.write.WriteOther('exit game - esc'.upper(), 20, x_window=(self.x_window) * 4.05 / 10, y_window=(self.y_window) * 8 / 10, color=(70, 70, 70))

    def EndPanel(self, points_stars):
        self.points_stars = points_stars
        self.write.Logo('logo.jpg')
        self.write.WriteText('Niestety przegrywasz', 42)
        self.write.WriteTextSpace('Naciśnij spację, aby zacząć gre', 42)
        self.write.WriteResults('Uzyskałeś {} punktów'.format(str(self.points_stars)), 30)
        self.write.WriteOther('exit game - esc'.upper(), 20, x_window=(self.x_window) * 4.05 / 10,
                              y_window=(self.y_window) * 8 / 10, color=(70, 70, 70))

    def LevelPanel(self):
        self.write.WriteOther('Wróć - Backspace', 19, 40, 40, color=(100, 100, 100))
        self.write.Logo('logo.jpg')
        self.write.WriteText('Wybierz poziom trudności', 42)
        self.font_text = pygame.font.SysFont('Arial', 42)
        self.render_text_easy = self.font_text.render('Easy - e', 1, (226, 216, 196))
        self.render_text_medium = self.font_text.render('Medium - m', 1, (226, 216, 196))
        self.render_text_hard = self.font_text.render('Hard - h', 1, (226, 216, 196))
        self.x_position = (self.x_window - self.render_text_medium.get_rect().width) / 2
        self.y_position = (self.y_window - self.render_text_medium.get_rect().height) * 3 / 4 - 50
        self.screen.blit(self.render_text_easy, (self.x_position + 20, self.y_position - 50))
        self.screen.blit(self.render_text_medium, (self.x_position - 10, self.y_position))
        self.screen.blit(self.render_text_hard, (self.x_position + 20, self.y_position + 50))
        self.write.WriteOther('exit game - esc'.upper(), 20, x_window=(self.x_window) * 4.05 / 10,
                              y_window=(self.y_window) * 8 / 10, color=(70, 70, 70))

    def StatisticsTablePanel(self): #OpenFileStatistic):
        self.write.WriteStatistic(32)
        self.write.WriteOther('Wróć - Backspace', 18, 40, 40, color=(100, 100, 100))
        self.write.WriteOther('Oto Tablica ostatniego wyniku:'.upper(), 36, x_window = (self.x_window) * 1.7 / 10, y_window = (self.y_window) * 1 / 9, color = (226, 216, 196))
        self.write.WriteOther('Naciśnij w aby wyczyścić tablice', 28, x_window=(self.x_window) * 1.5 / 5, y_window=(self.y_window) * 4 / 5, color = (60, 60, 60))
        self.write.WriteOther('exit game - esc'.upper(), 20, x_window=(self.x_window) * 4.05 / 10,
                              y_window=(self.y_window) * 8.5 / 10, color=(70, 70, 70))

