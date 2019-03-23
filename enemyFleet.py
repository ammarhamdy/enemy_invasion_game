from enemy import Enemy
from pygame.sprite import Group
import settings as ss
from ship import Ship
import time


class EnemyFleet(Group):

    def __init__(self, screen, ship: Ship):
        super().__init__()
        self.screen = screen
        self.ship = ship
        self.fleets = (self.fleet1, self.fleet2, self.fleet3, self.fleet4, self.fleet5, self.fleet6)
        self.fleet_index = 0
        self.num_fleets = len(self.fleets)
        self.start_time = int(time.time())
        self.current_time = int(time.time())
        self.wt = 3

    def draw_enemies(self):
        for enemy in self.sprites():
            enemy.draw()

    def schedule(self):
        if self.current_time - self.start_time == self.wt:
            self.fleets[self.fleet_index]()
            self.fleet_index = (self.fleet_index + 1) % self.num_fleets
            self.start_time = self.current_time
            self.wt = 15
        self.current_time = int(time.time())

    def fleet1(self, num_row=1):
        for i in range(num_row):
            enemy = Enemy(self.screen, self, row=i)
            for j in range(1, ss.max_enemies_x):
                enemy.next = Enemy(self.screen, self, row=i, column=j, pre=enemy)
                self.add(enemy)
                enemy = enemy.next
            self.add(enemy)

    def fleet2(self, num_row=1):
        # #ss.enemy_padding_left *= 2
        # #ss.max_enemies_x = ss.screen_size[0] // (ss.enemy_size[0] + ss.enemy_padding_left)
        # #self.empty()
        for i in range(num_row):
            enemy = Enemy(self.screen, self, row=i, attr=1)
            for j in range(1, ss.max_enemies_x):
                enemy.next = Enemy(self.screen, self, row=i, column=j, pre=enemy, attr=1)
                self.add(enemy)
                enemy = enemy.next
            self.add(enemy)

    def fleet3(self, num_row=1):
        # #self.empty()
        for i in range(num_row):
            enemy = Enemy(self.screen, self, row=i, attr=2)
            for j in range(1, ss.max_enemies_x):
                enemy.next = Enemy(self.screen, self, row=i, column=j, pre=enemy, attr=2)
                self.add(enemy)
                enemy = enemy.next
            self.add(enemy)

    def fleet4(self, num_row=1):
        # #self.empty()
        self.ship.swap_directions()
        for i in range(num_row):
            enemy = Enemy(self.screen, self, row=i, attr=2)
            for j in range(1, ss.max_enemies_x):
                enemy.next = Enemy(self.screen, self, row=i, column=j, pre=enemy, attr=2)
                self.add(enemy)
                enemy = enemy.next
            self.add(enemy)

    def fleet5(self, num_row=1):
        # #self.empty()
        # self.ship.disappear()
        for i in range(num_row):
            enemy = Enemy(self.screen, self, row=i, attr=2)
            for j in range(1, ss.max_enemies_x):
                enemy.next = Enemy(self.screen, self, row=i, column=j, pre=enemy, attr=2)
                self.add(enemy)
                enemy = enemy.next
            self.add(enemy)

    def fleet6(self, num_row=1):
        # #self.empty()
        # self.ship.appear()
        self.ship.swap_directions()
        for i in range(num_row):
            enemy = Enemy(self.screen, self, row=i, attr=1)
            for j in range(1, ss.max_enemies_x):
                enemy.next = Enemy(self.screen, self, row=i, column=j, pre=enemy, attr=(j % 2)+1)
                self.add(enemy)
                enemy = enemy.next
            self.add(enemy)
