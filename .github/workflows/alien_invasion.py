import pygame

from pygame.sprite import Group

import sys

from settings import Settings

from ship import Ship

from alien import Alien

from game_stats import GameStats

from play_button import Play

from scoreboard import Scoreboard

from change_ship import Change

from change_alien import Change_alien

import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    play_button = Play(ai_settings, screen, "Play")
    change_button = Change(ai_settings, screen, "Change ship")
    change_alien_button = Change_alien(ai_settings, screen, "Change aliens")
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    ship = Ship(ai_settings, screen)
    alien = Alien(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    while True:
        gf.check_events(ai_settings, screen, stats, sb, change_button, change_alien_button, ship, alien, aliens, bullets, play_button)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, alien, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, change_button, change_alien_button, ship, aliens, alien, bullets, play_button)

run_game()
