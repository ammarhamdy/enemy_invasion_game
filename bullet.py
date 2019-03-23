import pygame
from pygame.sprite import Sprite
import settings as ss


class Bullet(Sprite):
    speed_factor = ss.bullet_speed_factor

    def __init__(self, ship):
        super().__init__()
        self.ship = ship
        self.color = ss.bullet_color
        self.size = ss.bullet_size
        self.screen = self.ship.screen
        self.rect = pygame.Rect(0, 0, self.size[0], self.size[1])
        # set the bullet coordinate x.
        self.rect.centerx = self.ship.image_rect.centerx
        self.rect.top = self.ship.image_rect.top
        # store the bullet's position as a float value.
        self.y = float(self.rect.y)
        # set the bullet coordinate y.
        self.rect.y = self.y
        self.useful = True

    def update(self):
        self.useful = self.rect.bottom > 0
        if self.useful:
            self.y -= Bullet.speed_factor
            self.rect.y = self.y

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def re_shot(self):
        # reset position of bullet to be shot from ship to top.
        self.rect.centerx = self.ship.image_rect.centerx
        self.rect.top = self.ship.image_rect.top
        self.y = float(self.rect.y)
        self.rect.y = self.y

    def is_ready(self):
        # the bullet will be ready when it cross the top of screen.
        return not self.useful

    def set_ready(self):
        self.rect.bottom = -1
