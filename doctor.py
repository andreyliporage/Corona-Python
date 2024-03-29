import pygame

class Doctor():
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_setting = ai_settings

        self.image = pygame.image.load('images/doctor.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # doctor na parte inferior central da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        # flag de movimento
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_setting.doctor_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_setting.doctor_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_doctor(self):
        self.center = self.screen_rect.centerx