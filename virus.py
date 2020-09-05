import pygame
from pygame.sprite import Sprite

# classe Virus herda da classe Sprite
class Virus(Sprite):
    def __init__(self, ai_settings, screen):
        super(Virus, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # carrega a imagem do virus
        self.image = pygame.image.load('images/sacola2.bmp')
        self.rect = self.image.get_rect()

        # inicia cada virus proximo a parte superior esqueda
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    # desenha o virus na sua posicao atual
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.x += (self.ai_settings.virus_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True