import os
import pygame
import time
import random
import pygame
import sys
import string
from random import randint 
# музика для всього
MUSIC_RANDOM_WIN = random.randint(1, 3)
if MUSIC_RANDOM_WIN == 1:
    MUSIC_WIN = 'audio/level_music_win.mp3'
elif MUSIC_RANDOM_WIN == 2:
    MUSIC_WIN = 'audio/level_music_win1.mp3'
elif MUSIC_RANDOM_WIN == 3:
    MUSIC_WIN = 'audio/level_music_win2.mp3'
MUSIC_RANDOM_LOSE = random.randint(1, 2)
if MUSIC_RANDOM_LOSE == 1:
    MUSIC_LOSE = 'audio/level_music_lose.mp3'
elif MUSIC_RANDOM_LOSE == 2:
    MUSIC_LOSE = 'audio/level_music_lose1.mp3'
JUMP = 'audio/jump.mp3'

LEVEL = int(input('Який lvl бажаєте вибрати (1, 2, 3)? = '))
def SLEEPING():
    time.sleep(1488)
# mario.py
WIN_WIDTH, WIN_HEIGHT = 1600, 900
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
BACKGROUND_COLOR = '#000000'
FPS = 60
SCREEN_START = (0, 0)
FILE_DIR = os.path.dirname(__file__)
if LEVEL == 1:
    FILE_PATH = '%s/levels/1.txt' % FILE_DIR
    target_time = 300
    target_time1 = 300
    target_time2 = 300
elif LEVEL == 2:
    FILE_PATH = '%s/levels/2.txt' % FILE_DIR
    target_time = 300
    target_time1 = 300
    target_time2 = 300
elif LEVEL == 3:
    FILE_PATH = '%s/levels/3.txt' % FILE_DIR
    target_time = 400
    target_time1 = 400
    target_time2 = 400
elif LEVEL == 1488:
    FILE_PATH = '%s/levels/4.txt' % FILE_DIR
    target_time = 1488
    target_time1 = 1488
    target_time2 = 1488
screen = pygame.display.set_mode(DISPLAY)

# monsters.py
MONSTER_WIDTH, MONSTER_HEIGHT, MONSTER_COLOR = 32, 32, '#2111FF'
ICON_DIR = os.path.dirname(__file__)
ANIMATION_MONSTER_HORIZONTAL = [('%s/monsters/fire1.png' % ICON_DIR), ('%s/monsters/fire2.png' % ICON_DIR)]

# blocks.py
PLATFORM_WIDTH, PLATFORM_HEIGHT, PLATFORM_COLOR = 32, 32, '#000000'
# ICON_DIR = os.path.dirname(__file__)
ANIMATION_BLOCK_TELEPORT = [('%s/blocks/portal1.png' % ICON_DIR), ('%s/blocks/portal2.png' % ICON_DIR)]
ANIMATION_PRINCESS = [('%s/blocks/princess_l.png' % ICON_DIR), ('%s/blocks/princess_r.png' % ICON_DIR)]
if LEVEL == 3:
    PATH_BLOCK_PLATFORM = '%s/blocks/ung_block.png' % ICON_DIR
else:
    PATH_BLOCK_PLATFORM = '%s/blocks/platform.png' % ICON_DIR
PATH_BLOCK_DIE = '%s/blocks/dieBlock.png' % ICON_DIR

# player.py
image_path = '%s/blocks/end_and_start.png' % ICON_DIR 





MOVE_SPEED = 7
MOVE_EXTRA_SPEED = 2.5
WIDTH, HEIGHT, COLOR = 22, 32, '#888888'
JUMP_POWER, JUMP_EXTRA_POWER, GRAVITY = 10, 1, 0.25
ANIMATION_DELAY, ANIMATION_SUPER_SPEED_DELAY = 0.1, 0.05

PLATFORM_IMAGE = "%s/blocks/platform.png" % ICON_DIR

ANIMATION_LEFT = [('%s/mario/l1.png' % ICON_DIR),
                  ('%s/mario/l2.png' % ICON_DIR),
                  ('%s/mario/l3.png' % ICON_DIR),
                  ('%s/mario/l4.png' % ICON_DIR),
                  ('%s/mario/l5.png' % ICON_DIR)
                  ]

ANIMATION_RIGHT = [('%s/mario/r1.png' % ICON_DIR),
                   ('%s/mario/r2.png' % ICON_DIR),
                   ('%s/mario/r3.png' % ICON_DIR),
                   ('%s/mario/r4.png' % ICON_DIR),
                   ('%s/mario/r5.png' % ICON_DIR)
                   ]

ANIMATION_JUMP = [('%s/mario/j.png' % ICON_DIR, ANIMATION_DELAY)]
ANIMATION_JUMP_LEFT = [('%s/mario/jl.png' % ICON_DIR, ANIMATION_DELAY)]
ANIMATION_JUMP_RIGHT = [('%s/mario/jr.png' % ICON_DIR, ANIMATION_DELAY)]
ANIMATION_STAY = [('%s/mario/0.png' % ICON_DIR, ANIMATION_DELAY)]

# pyganim.py
PLAYING, PAUSED, STOPPED = 'playing', 'paused', 'stopped'
# Ці значення використовуються в методі anchor().
NORTH, SOUTH, WEST, EAST, CENTER = 'north', 'south', 'west', 'east', 'center'
NORTH_WEST, SOUTH_WEST, NORTH_EAST, SOUTH_EAST = 'northwest', 'southwest', 'northeast', 'southeast'
# Кольора
BLUE = (47,79,79)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLACK_WHITE_STEPTIONISTICKO_STERUGOLI_GRIN = (0, 127, 14)
