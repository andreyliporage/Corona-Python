import pygame
import game_functions as gf
from pygame.sprite import Group

import virus
from settings import Settings
from game_stats import GameStats
from doctor import Doctor
from button import Button
from scoreboard import ScoreBoard


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((
        (ai_settings.screen_width, ai_settings.screen_height)
    ))
    pygame.display.set_caption("Corona Python")
    play_button = Button(ai_settings, screen, "Play")
    doctor = Doctor(ai_settings, screen)
    bullets = Group()
    viruses = Group()

    stats = GameStats(ai_settings)
    sb = ScoreBoard(ai_settings, screen, stats)

    gf.create_fleet(ai_settings, screen, doctor, viruses)

    while True:
        gf.check_events(ai_settings, screen, stats,
                        sb, play_button, doctor, viruses, bullets)

        if stats.game_active:
            doctor.update()
            gf.update_bullets(ai_settings, screen, stats,
                              sb, doctor, viruses, bullets)
            gf.update_bullets(ai_settings, screen, stats,
                              sb, doctor, viruses, bullets)
            gf.update_viruses(ai_settings, stats, screen,
                              doctor, viruses, bullets)
            for bullet in bullets.copy():
                if bullet.rect.bottom <= 0:
                    bullets.remove(bullet)
            gf.update_screen(ai_settings, screen, stats, sb, doctor,
                             viruses, bullets, play_button)


run_game()
