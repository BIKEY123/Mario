from pygame import *
import pyganim
from settings import MONSTER_WIDTH, MONSTER_HEIGHT, MONSTER_COLOR, ANIMATION_MONSTER_HORIZONTAL, SCREEN_START


class Monster(sprite.Sprite):
    def __init__(self, x, y, left, up, max_length_left, max_length_up):
        # sprite.Sprite.__init__(self)
        super().__init__()
        self.image = Surface((MONSTER_WIDTH, MONSTER_HEIGHT))
        self.image.fill(Color(MONSTER_COLOR))
        self.rect = Rect(x, y, MONSTER_WIDTH, MONSTER_HEIGHT)
        self.image.set_colorkey(Color(MONSTER_COLOR))
        self.start_x = x  # Початкові координати
        self.start_y = y
        # максимальна відстань, яка може пройти в один бік
        self.max_length_left = max_length_left
        # максимальна відстань, яка може пройти в один бік, вертикаль
        self.max_length_up = max_length_up
        # швидкість пересування по горизонталі, 0 - стоїть на місці
        self.x_val = left
        # швидкість руху по вертикалі, 0 - не рухається
        self.y_val = up
        """ bolt_anim = [(anim, 0.3) for anim in ANIMATION_MONSTER_HORIZONTAL]
        for anim in ANIMATION_MONSTER_HORIZONTAL:
            bolt_anim.append((anim, 0.3))
        self.boltAnim = pyganim.PygAnimation(bolt_anim)"""
        self.bolt_anim = pyganim.PygAnimation([(anim, 0.3) for anim in ANIMATION_MONSTER_HORIZONTAL])
        self.bolt_anim.play()

    def update(self, platforms):
        self.image.fill(Color(MONSTER_COLOR))
        self.bolt_anim.blit(self.image, SCREEN_START)

        self.rect.y += self.y_val
        self.rect.x += self.x_val

        self.collide(platforms)

        if abs(self.start_x - self.rect.x) > self.max_length_left:
            # якщо пройшли максимальну відстань, то ідеї у зворотний бік
            self.x_val = - self.x_val
        if abs(self.start_y - self.rect.y) > self.max_length_up:
            # якщо пройшли максимальну відстань, то ідеї у зворотний бік, вертикаль
            self.y_val = - self.y_val

    def collide(self, platforms):
        for platform in platforms:
            # якщо з чимось чи кимось зіткнулися
            if sprite.collide_rect(self, platform) and self != platform:
                # то повертаємо у зворотний бік
                self.x_val = - self.x_val
                self.y_val = - self.y_val
