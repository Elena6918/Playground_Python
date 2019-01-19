import pygame
import gamebox
import random

camera = gamebox.Camera(800, 600)
game_started = False
title_snake = []
tick_count = 0
images_sr = gamebox.load_sprite_sheet('sr.png', 4, 4)
for i in range(12):
    s_right = gamebox.from_image(-(100 * i), 500, images_sr[9])
    s_right.speedx = 5
    title_snake.append(s_right)

instructions = '''
    Some Instructions here.
    Maybe collecting the coins.
'''

def startframe(keys):
    '''
    Draw title screen
    '''
    global game_started
    global tick_count

    if keys:
        game_started = True
    keys.clear()

    to_draw = []  # contains everything drawed in this frame
    title_box = gamebox.from_text(300, 30, 'Hey', 80, 'red', True)
    to_draw.append(title_box)
    ypos = 200
    for line in instructions.split('\n'):
        to_draw.append(gamebox.from_text(300, ypos, line, 30, 'red'))
        ypos += 20
    for sr in title_snake:
        sr.image = images_sr[tick_count // 2 % len(images_sr)]
        sr.move_speed()
        to_draw.append(sr)
        if sr.x > 800 and sr.speedx > 0:
            sr.x = 0
        elif sr.x < 0 and sr.speedx < 0:
            sr.x = 800
    to_draw.append(s_right)
    tick_count += 1


    for box in to_draw:
        camera.draw(box)


coins = gamebox.load_sprite_sheet('coin.png', 1, 5)
coin_speed = random.randrange(3, 5)

def draw_coin(speed):
    global coin
    coin = gamebox.from_image(random.randrange(0, 800), random.randrange(-100, 0), coins[0])
    coin.scale_by(0.2)
    coin.speedy = speed
    return coin

new_coin = []
tick_count = 0
for i in range(6):
    new_coin.append(draw_coin(coin_speed))

ppl = gamebox.load_sprite_sheet('people')
score = 0


def draw_game(keys):
    global tick_count
    global new_coin
    global score
    camera.clear('light blue')
    to_draw = []
    for i in range(6):
        new_coin[i].image = coins[tick_count // 2 % len(coins)]
        to_draw.append(new_coin[i])
        new_coin[i].move_speed()
        if new_coin[i].y > 650:
            del new_coin[i]
            new_coin.append(draw_coin(coin_speed))
        if ppl.touches(new_coin[i]):
            score += 1
            del new_coin[i]
            new_coin.append(draw_coin(coin_speed))
    tick_count += 1
    to_draw.append(ppl)
    scoreboard = gamebox.from_text(200, 100, 'score: ' + str(score), 16, 'black')
    to_draw.append(scoreboard)
    if pygame.K_RIGHT in keys and ppl.x <= 800:
        ppl.x += 10
    if pygame.K_LEFT in keys and ppl.x >= 0:
        ppl.x -= 10





    for box in to_draw:
        camera.draw(box)


def tick(keys):
    camera.clear('white')
    if not game_started:
        startframe(keys)
    else:
        draw_game(keys)
    camera.display()

gamebox.timer_loop(30, tick)