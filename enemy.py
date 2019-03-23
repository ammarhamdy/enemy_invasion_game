import pygame
from pygame.sprite import Sprite
import settings as ss


class Enemy(Sprite):
    # attr: width, height, speed factor, drop speed, color, shots to die.
    enemies_attr = (
        (ss.enemy_size[0], ss.enemy_size[1], ss.enemy_speed_factor, ss.enemy_drop_speed, (230, 75, 60), 1),
        (ss.enemy_size[0]//2, ss.enemy_size[1]//2, ss.enemy_speed_factor, ss.enemy_drop_speed * 2, (255, 235, 60), 1),
        (ss.enemy_size[0], ss.enemy_size[1], ss.enemy_speed_factor, ss.enemy_drop_speed, (150, 50, 50), 2)
    )

    def __init__(self, screen, enemy_fleet, row=0, column=0, pre=None, nex=None, attr=0):
        super().__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.enemy_fleet = enemy_fleet

        self.rect = pygame.Rect(0, 0, Enemy.enemies_attr[attr][0], Enemy.enemies_attr[attr][1])

        self.previous = pre
        self.next = nex
        self.speed = Enemy.enemies_attr[attr][2]
        self.drop_speed = Enemy.enemies_attr[attr][3]
        self.color = Enemy.enemies_attr[attr][4]
        self.life = Enemy.enemies_attr[attr][5]
        self.direction = 1

        self.in_half1 = column < ss.max_enemies_x // 2
        padding_plus_width = ss.enemy_padding_left + ss.enemy_size[0]

        self.rect.y = (self.rect.width + ss.enemy_padding_top) * row + ss.enemy_padding_top
        self.y = float(self.rect.y)
        self.rect.x = padding_plus_width * column + ss.enemy_padding_left
        self.x = float(self.rect.x)

        self.threshold_right = self.screen.get_rect().right
        self.threshold_right -= (ss.max_enemies_x - column) * padding_plus_width
        self.threshold_right += padding_plus_width
        self.threshold_left = column * padding_plus_width

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def update(self):
        if self.rect.left <= self.threshold_left or self.rect.right >= self.threshold_right:
            self.direction *= -1
            self.y += self.drop_speed
            self.rect.y = self.y
        self.x += self.speed * self.direction
        self.rect.x = self.x
        if self.rect.bottom >= ss.enemy_deadline:
            self.enemy_fleet.remove(self)

    def die(self):
        self.life -= 1
        if not self.life:
            if self.previous:
                self.previous.next = self.next
                if not self.in_half1:
                    self.previous.threshold_right = self.threshold_right
                    self.previous.speed += .25
            if self.next:
                self.next.previous = self.previous
                if self.in_half1:
                    self.next.threshold_left = self.threshold_left
                    self.next.speed += .25
            self.enemy_fleet.remove(self)
