import pygame
from pygame.sprite import Sprite

# classe Bullet herda de Sprite
class Bullet(Sprite):
    def __init__(self, ai_settings, screen, doctor):
        super(Bullet, self).__init__()
        self.screen = screen

        # cria um retangulo para o projetil na origem
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = doctor.rect.centerx
        self.rect.top = doctor.rect.top

        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    # posicao do projetil
    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y

    # desenha o projetil
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)