
# window settings.
screen_size = (1200, 720)
screen_background_color = (50, 50, 70)

# ship settings.
ship_speed_factor = 2
ship_max_bullets = 2

# bullet settings.
bullet_speed_factor = 3
bullet_size = (3, 15)
bullet_color = (100, 200, 100)

# enemy
enemy_size = (60, 60)
enemy_padding_left = 60
enemy_padding_top = 30
enemy_speed_factor = 1
enemy_drop_speed = 5.0
enemy_deadline = screen_size[1] - enemy_size[1]
# maximum number of enemy can be in screen height.
max_enemies_x = screen_size[0] // (enemy_size[0] + enemy_padding_left)
# maximum number of enemy rows can be on screen height (-5 to let space between ship).
max_enemies_y = -5 + screen_size[1] // (enemy_size[1] + enemy_padding_top)
