import sys
import pygame

def check_events(rubix,theSettings,screen,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,rubix,screen,theSettings,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,rubix)

def check_keydown_events(event,rubix,theSettings,bullets,screen):
    if event.key == pygame.K_RIGHT:
        rubix.moving_right = True
    if event.key == pygame.K_LEFT:
        rubix.moving_left = True
    if event.key == pygame.K_UP:
        rubix.moving_up = True
    if event.key == pygame.K_DOWN:
        rubix.moving_down = True
    if event.key == pygame.K_SPACE:
        new_bullet = bullets(theSettings,screen,rubix)
        bullets.add(new_bullet)

def check_keyup_events(event,rubix):
    if event.key == pygame.K_RIGHT:
        rubix.moving_right = False
        rubix.rect.centerx += 1
    if event.key == pygame.K_LEFT:
        rubix.moving_left = False
        rubix.rect.centerx -= 1
    if event.key == pygame.K_UP:
        rubix.moving_up = False
        rubix.rect.centery -= 1
    if event.key == pygame.K_DOWN:
        rubix.moving_down = False
        rubix.rect.centery += 1


def update_screen(theSettings,screen,rubix,bullets):
    screen.fill(theSettings.bg_color)
    rubix.blitme()

    for bullet in bullets.sprites():
        bullet.draw_bullet()