import sys
import pygame


def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(ai_settings, screen, body):
    screen.fill(ai_settings.bg_color)
    body.blitme()
    pygame.display.flip()
