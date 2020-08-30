import pygame
import game_functions as gf
from pygame.sprite import Group
from settings import Settings
from doctor import Doctor

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((
        (ai_settings.screen_width, ai_settings.screen_height)
    ))
    pygame.display.set_caption("Corona Python")
    doctor = Doctor(ai_settings, screen)
    bullets = Group()

    while True:
        gf.check_events(ai_settings, screen, doctor, bullets)
        doctor.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, doctor, bullets)
run_game()

