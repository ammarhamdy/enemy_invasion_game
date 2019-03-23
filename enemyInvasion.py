import pygame
import sys
import settings as ss
from ship import Ship
from bullet import Bullet
from enemyFleet import EnemyFleet
from eventHandler import EventHandler


class EnemyInvasion:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('enemy invasion')
        self.main_clock = pygame.time.Clock()

        self.background_color = ss.screen_background_color

        self.screen = pygame.display.set_mode(ss.screen_size)

        self.ship: Ship = Ship(self.screen)

        self.enemyFleet = EnemyFleet(self.screen, self.ship)

        self.eventHandler = EventHandler()
        self.add_events()

    def add_events(self):
        self.eventHandler.add_event(pygame.QUIT, lambda event: sys.exit(0))
        move = {pygame.K_q: sys.exit,
                pygame.K_LEFT: self.ship.move_left,
                pygame.K_RIGHT: self.ship.move_right,
                pygame.K_SPACE: self.ship.shot}
        self.eventHandler.add_event(pygame.KEYDOWN, lambda event: move.get(event.key, lambda: None)())
        stop_move = {pygame.K_LEFT: self.ship.stop_move_left, pygame.K_RIGHT: self.ship.stop_move_right}
        self.eventHandler.add_event(pygame.KEYUP, lambda event: stop_move.get(event.key, lambda: None)())

    def check_collision(self):
        # #pygame.sprite.groupcollide(self.ship.bullets_group, self.enemyFleet, lambda i: i.set_ready(), True)
        for bullet, enemy in pygame.sprite.groupcollide(self.ship.bullets_group, self.enemyFleet, False, False).items():
            # only first enemy has been shot will die.
            enemy[0].die()
            bullet.set_ready()

    def update_screen(self):
        # redraw the screen.
        self.screen.fill(self.background_color)
        # draw bullets.
        self.ship.draw_bullets()
        self.ship.bullets_group.update()
        # draw ship in screen.
        self.ship.draw()
        # #self.enemyFleet.draw(self.screen)
        self.enemyFleet.draw_enemies()
        self.enemyFleet.update()
        self.check_collision()
        self.enemyFleet.schedule()
        # make the most recently drawn screen visible.
        pygame.display.flip()

    def start(self):
        while True:
            self.eventHandler.check_events(pygame.event.get())
            self.update_screen()
            # control the game speed by 40 iteration per second.
            self.main_clock.tick(170)
