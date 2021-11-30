import sys
from time import sleep
import pygame

from bullet import Bullet
from virus import Virus


def check_events(ai_settings, screen, stats, play_button, doctor, viruses, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, doctor, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, doctor)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button,
                              doctor, viruses, bullets, mouse_x, mouse_y)


def check_play_button(ai_settings, screen, stats, play_button, doctor, viruses, bullets, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True
        viruses.empty()
        bullets.empty()
        create_fleet(ai_settings, screen, doctor, viruses)
        doctor.center_doctor()


def create_fleet(ai_settings, screen, doctor, viruses):
    virus = Virus(ai_settings, screen)
    number_viruses_x = get_number_viruses_x(ai_settings, virus.rect.width)
    number_rows = int(get_number_rows(
        ai_settings, doctor.rect.height, virus.rect.height))

    for row_number in range(number_rows):
        for virus_number in range(number_viruses_x):
            create_virus(ai_settings, screen, viruses,
                         virus_number, row_number)


def get_number_viruses_x(ai_settings, virus_width):
    available_space_x = ai_settings.screen_width - 2 * virus_width
    number_viruses_x = int(available_space_x / (2 * virus_width))
    return number_viruses_x


def create_virus(ai_settings, screen, viruses, virus_number, row_number):
    virus = Virus(ai_settings, screen)
    virus_width = virus.rect.width
    virus.x = virus_width + 2 * virus_width * virus_number
    virus.rect.x = virus.x
    virus.rect.y = virus.rect.height + 2 * virus.rect.height * row_number
    viruses.add(virus)


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
        if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, doctor)
            bullets.add(new_bullet)


def update_screen(ai_setting, screen, stats, doctor, viruses, bullets, play_button):
    screen.fill(ai_setting.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    doctor.blitme()
    viruses.draw(screen)

    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip()


def check_bullet_virus_collision(ai_settings, screen, doctor, viruses, bullets):
    collisions = pygame.sprite.groupcollide(bullets, viruses, True, True)
    if len(viruses) == 0:
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, doctor, viruses)


def update_bullets(ai_settings, screen, doctor, viruses, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_virus_collision(ai_settings, screen, doctor, viruses, bullets)


def get_number_rows(ai_settings, doctor_height, virus_height):
    available_space_y = (ai_settings.screen_height -
                         (3 * virus_height) - doctor_height)
    number_rows = int(available_space_y) / (2 * virus_height)
    return number_rows


def update_viruses(ai_settings, stats, screen, doctor, viruses, bullets):
    check_fleet_edges(ai_settings, viruses)
    viruses.update()
    if pygame.sprite.spritecollideany(doctor, viruses):
        doctor_hit(ai_settings, stats, screen, doctor, viruses, bullets)

    if pygame.sprite.spritecollideany(doctor, viruses):
        print("Corona te pegou!")
    check_viruses_bottom(ai_settings, stats, screen, doctor, viruses, bullets)


def check_fleet_edges(ai_settings, viruses):
    for virus in viruses.sprites():
        if virus.check_edges():
            change_fleet_direction(ai_settings, viruses)
            break


def change_fleet_direction(ai_settings, viruses):
    for virus in viruses.sprites():
        virus.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def doctor_hit(ai_settings, stats, screen, doctor, viruses, bullets):
    if stats.viruses_left > 0:
        stats.viruses_left -= 1
        viruses.empty()
        bullets.empty()
        create_fleet(ai_settings, screen, doctor, viruses)
        doctor.center_doctor()
        sleep(0.5)
    else:
        stats.game_active = False


def check_viruses_bottom(ai_settings, stats, screen, doctor, viruses, bullets):
    screen_rect = screen.get_rect()
    for virus in viruses.sprites():
        if virus.rect.bottom >= screen_rect.bottom:
            doctor_hit(ai_settings, stats, screen, doctor, viruses, bullets)
            break
