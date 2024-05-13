from pygame import *
import pyganim
from settings import PLATFORM_WIDTH, PLATFORM_HEIGHT, PLATFORM_COLOR, ANIMATION_BLOCK_TELEPORT, \
    ANIMATION_PRINCESS, PATH_BLOCK_PLATFORM, PATH_BLOCK_DIE, SCREEN_START


class Platform(sprite.Sprite):
    def __init__(self, x, y):
        # sprite.Sprite.__init__(self)
        super().__init__()
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(Color(PLATFORM_COLOR))
        self.image = image.load(PATH_BLOCK_PLATFORM)
        self.image.set_colorkey(Color(PLATFORM_COLOR))
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)


class BlockDie(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = image.load(PATH_BLOCK_DIE)


class BlockTeleport(Platform):
    def __init__(self, x, y, go_x, go_y):
        Platform.__init__(self, x, y)
        # координати призначені для переміщення
        self.go_x = go_x
        self.go_y = go_y
        """bolt_anim = []
        for anim in ANIMATION_BLOCK_TELEPORT:
            bolt_anim.append((anim, 0.3))
        self.bolt_anim = pyganim.PygAnimation(bolt_anim)"""
        self.bolt_anim = pyganim.PygAnimation([(anim, 0.3) for anim in ANIMATION_BLOCK_TELEPORT])
        self.bolt_anim.play()

    def update(self):
        self.image.fill(Color(PLATFORM_COLOR))
        self.bolt_anim.blit(self.image, SCREEN_START)


class Princess(Platform):
    def __init__(self, x, y):
        # Platform.__init__(self, x, y)
        super().__init__(x, y)
        """bolt_anim = []
        for anim in ANIMATION_PRINCESS:
            bolt_anim.append((anim, 0.8))
        self.bolt_anim = pyganim.PygAnimation(bolt_anim)"""
        self.bolt_anim = pyganim.PygAnimation([(anim, 0.8) for anim in ANIMATION_PRINCESS])
        self.bolt_anim.play()

    def update(self):
        self.image.fill(Color(PLATFORM_COLOR))
        self.bolt_anim.blit(self.image, SCREEN_START)
