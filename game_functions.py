import sys
import pygame

def check_events(doctor):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                doctor.rect.centerx += 1

def update_screen(ai_setting, screen, doctor):
    screen.fill(ai_setting.bg_color)
    doctor.blitme()

    pygame.display.flip()