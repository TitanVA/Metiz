import pygame
from body import Body
import functions as fs
from settings import Settings


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    body = Body(screen)
    pygame.display.set_caption('Homework')
    while True:
        screen.fill(ai_settings.bg_color)
        fs.check_events()
        fs.update_screen(ai_settings, screen, body)

run_game()
