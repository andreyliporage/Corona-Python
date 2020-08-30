import sys
import pygame
from bullet import Bullet

def check_events(ai_settings, screen, doctor, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, doctor, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, doctor)

def check_keyup_events(event, doctor):
    if event.key == pygame.K_RIGHT:
        doctor.moving_right = False
    elif event.key == pygame.K_LEFT:
        doctor.moving_left = False

def check_keydown_events(event, ai_settings, screen, doctor, bullets):
    if event.key == pygame.K_RIGHT:
        doctor.moving_right = True
    elif event.key == pygame.K_LEFT:
        doctor.moving_left = True
    elif event.key == pygame.K_SPACE:
        new_bullet = Bullet(ai_settings, screen, doctor)
        bullets.add(new_bullet)

def update_screen(ai_setting, screen, doctor, bullets):
    screen.fill(ai_setting.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    doctor.blitme()

    pygame.display.flip()