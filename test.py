import pygame

from settings import Settings
from doctor import Doctor
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((
        (ai_settings.screen_width, ai_settings.screen_height)
    ))
    pygame.display.set_caption("Corona Python")
    doctor = Doctor(screen)

    while True:
        gf.check_events(doctor)
        doctor.update()
        gf.update_screen(ai_settings, screen, doctor)
run_game()

