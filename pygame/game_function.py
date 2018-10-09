import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def check_keydown_events(event,rubix,screen,theSettings,bullets):
    if event.key == pygame.K_RIGHT:
        rubix.moving_right = True
    if event.key == pygame.K_LEFT:
        rubix.moving_left = True
    if event.key == pygame.K_UP:
        rubix.moving_up = True
    if event.key == pygame.K_DOWN:
        rubix.moving_down = True
    if event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_SPACE:
        if len(bullets) < theSettings.bullets_allowed:
            new_bullet = Bullet(theSettings,screen,rubix)
            bullets.add(new_bullet)

def get_number_aliens_x(theSettings,alien_width):
    available_space_x = theSettings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(theSettings,rubix_height,alien_height):
    available_space_y = (theSettings.screen_height - (3 * alien_height) - rubix_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(theSettings,screen,aliens,alien_number,row_number):
    alien = Alien(theSettings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 1.5 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)
def create_fleet(theSettings,screen,rubix,aliens):
    alien = Alien(theSettings,screen)
    number_aliens_x = get_number_aliens_x(theSettings, alien.rect.width)
    number_rows = get_number_rows(theSettings,rubix.rect.height,alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(theSettings,screen,aliens,alien_number,row_number)

def check_keyup_events(event,rubix):
    if event.key == pygame.K_RIGHT:
        rubix.moving_right = False
    if event.key == pygame.K_LEFT:
        rubix.moving_left = False
    if event.key == pygame.K_UP:
        rubix.moving_up = False
    if event.key == pygame.K_DOWN:
        rubix.moving_down = False


def check_events(theSettings,screen,rubix,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,theSettings,screen,rubix,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,rubix)

def update_screen(theSettings,screen,rubix,aliens,bullets):
    screen.fill(theSettings.bg_color)
    rubix.blitme()
    aliens.draw(screen)

    for bullet in bullets.sprites():
        bullet.drawBullet()
        bullet.bulletUpdate()

    pygame.display.flip()

def update_bullets(theSettings,screen,rubix,aliens,bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(theSettings,screen,rubix,aliens,bullets)

def check_bullet_alien_collisions(theSettings,screen,rubix,aliens,bullets):
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(theSettings,screen,rubix,aliens)

def update_aliens(theSettings,stats,screen,rubix,aliens,bullets):
    check_fleet_edges(theSettings,aliens)
    check_aliens_bottom(theSettings,stats,screen,rubix,aliens,bullets)
    aliens.update()

    if pygame.sprite.spritecollideany(rubix,aliens):
        ship_hit(theSettings,stats,screen,rubix,aliens,bullets)
        print("Rubix Hit !!")


def check_fleet_edges(theSettings,aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(theSettings,aliens)
            break

def check_fleet_direction(theSettings,aliens):
    for alien in aliens.sprite():
        alien.rect.y += theSettings.fleet_drop_speed
    theSettings.fleet_direction *= -1

def rubix_hit():
    if stats.rubix_left > 0:
        stats.rubix_left -= 1
        aliens.empty()
        bullets.empty()
        create_fleet(theSettings,screen,rubix,aliens)
        rubix.center_rubix()
        sleep(0.5)
    else:
        stats.game_active = False

def check_aliens_bottom(theSettings,stats,screen,rubix,aliens,bullets):
    screen_rect = screen.get_rect()
    for aliens in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            rubix_hit(theSettings,stats,screen,rubix,aliens,bullets) # treat as same as the rubix got hit
            break





    #for alien_number in range(number_aliens_x):
       # alien = Alien(theSettings,screen)
        #alien.x = alien_width + 1.5 * alien_width * alien_number
        #alien.rect.x = alien.x
        #aliens.add(alien)
