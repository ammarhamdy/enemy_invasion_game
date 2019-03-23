import pygame
from pygame.sprite import Group
import settings as ss
from bullet import Bullet


class Ship:
    # image size (60, 42)
    speed_factor = ss.ship_speed_factor
    max_bullets = ss.ship_max_bullets
    direction = 1

    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load('image\\triangle.bmp')
        # #pygame.mixer.music.load(r'sound\shot.mp3')
        self.image_rect = self.image.get_rect()
        # rect centerx store only int value.
        self.image_rect.centerx = self.screen_rect.centerx
        # centerx can be float value unlike rect centerx.
        self.centerx = float(self.image_rect.centerx)
        self.image_rect.bottom = self.screen_rect.bottom

        # movement.
        self.left_key_down = True
        self.right_key_down = True
        self.move_left_event = pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_LEFT})
        self.move_right_event = pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_RIGHT})

        # shooting.
        self.bullets_group = Group()
        self.bullets = []
        self.bullet_index = 0
        self.num_shot = 0

        self.shot0 = self.shot1
        self.draw = self.blit

        self.direction = 1
        self.threshold_left = lambda: self.image_rect.left > 0
        self.threshold_right = lambda: self.image_rect.right < self.screen_rect.right

    def blit(self):
        # draw the image at it's location.
        self.screen.blit(self.image, self.image_rect)

    def move_left(self):
        if self.left_key_down:
            self.centerx -= self.threshold_left() * Ship.speed_factor * self.direction
            self.image_rect.centerx = self.centerx
            # make movement continuous by add the same event to queue.
            pygame.event.post(self.move_left_event)
        self.left_key_down = True

    def move_right(self):
        if self.right_key_down:
            self.centerx += self.threshold_right() * Ship.speed_factor * self.direction
            self.image_rect.centerx = self.centerx
            # make movement continuous by add the same event to queue.
            pygame.event.post(self.move_right_event)
        self.right_key_down = True

    def stop_move_left(self):
        self.left_key_down = False

    def stop_move_right(self):
        self.right_key_down = False

    def shot(self):
        self.shot0()

    def shot1(self):
        # make new Bullet.
        self.bullets.append(Bullet(self))
        self.bullets_group.add(self.bullets[self.num_shot])
        self.num_shot += 1
        # #pygame.mixer.music.play(1)
        if self.num_shot == Ship.max_bullets:
            self.shot0 = self.shot2

    def shot2(self):
        # get the useless bullet to re shot it again, instead of make new bullet.
        if self.bullets[self.bullet_index].is_ready():
            self.bullets[self.bullet_index].re_shot()
            self.bullet_index = (self.bullet_index + 1) % Ship.max_bullets
            # #pygame.mixer.music.play(1)

    def draw_bullets(self):
        for bullet in self.bullets_group.sprites():
            bullet.draw()

    # instead of remove and make new bullet we use the same bullet each time.
    # def remove_unused_bullets(self):
    #     for bullet in self.ship.bullets.copy():
    #         if bullet.rect.bottom <= 0:
    #             self.ship.bullets.remove(bullet)

    def swap_directions(self):
        self.direction *= -1
        self.threshold_left, self.threshold_right = self.threshold_right, self.threshold_left

    def disappear(self):
        self.draw = lambda: None

    def appear(self):
        self.draw = self.blit
