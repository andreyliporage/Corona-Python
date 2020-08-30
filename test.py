import pygame
import game_functions as gf
from pygame.sprite import Group
from settings import Settings
from doctor import Doctor
from virus import Virus

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((
        (ai_settings.screen_width, ai_settings.screen_height)
    ))
    pygame.display.set_caption("Corona Python")
    doctor = Doctor(ai_settings, screen)
    bullets = Group()
    virus = Virus(ai_settings, screen)

    while True:
        gf.check_events(ai_settings, screen, doctor, bullets)
        doctor.update()
        bullets.update()
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        print(len(bullets))
        gf.update_screen(ai_settings, screen, doctor, virus, bullets)

run_game()

