import sys
import pygame

def check_events(doctor):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                doctor.moving_right = True
            elif event.key == pygame.K_LEFT:
                doctor.moving_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                doctor.moving_right = False
            elif event.key == pygame.K_LEFT:
                doctor.moving_left = False

def update_screen(ai_setting, screen, doctor):
    screen.fill(ai_setting.bg_color)
    doctor.blitme()

    pygame.display.flip()