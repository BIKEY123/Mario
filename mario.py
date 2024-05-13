from pygame import *
import pygame
import time
import os
import sys
from time import *
from player import *
from blocks import *
from monsters import *
import random
from random import randint 
from settings import WIN_WIDTH, WIN_HEIGHT, DISPLAY, FILE_PATH, BACKGROUND_COLOR, FPS, RED, WHITE, BLACK, GREEN, SLEEPING, BLACK_WHITE_STEPTIONISTICKO_STERUGOLI_GRIN, MUSIC_LOSE, target_time, JUMP, LEVEL, BLUE, image_path, target_time2
pygame.init()


# Відкриття та відображення зображення
print( pygame.font.get_fonts() )

class Camera:
    def __init__(self, camera_fn, width, height):
        self.camera_fn = camera_fn
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_fn(self.state, target.rect)

def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = - l + WIN_WIDTH / 2, - t + WIN_HEIGHT / 2
    # Не рухаємось далі лівого кордону
    l = min(0, l)
    # Не рухаємося далі за правий кордон
    l = max(-(camera.width - WIN_WIDTH), l)
    # Не рухаємося далі за нижню межу
    t = max(-(camera.height - WIN_HEIGHT), t)
    # Не рухаємося далі за верхню межу
    t = min(0, t)

    return Rect(l, t, w, h)


def load_level():
    # оголошуємо глобальні змінні, це координати героя
    global player_x, player_y
    level_file = open(FILE_PATH)
    line = " "
    # commands = []
    # поки не знайшли символ завершення файлу
    while line[0] != "/":
        # зчитуємо порядково
        line = level_file.readline()
        # якщо знайшли символ початку рівня
        if line[0] == "[":
            # те, поки не знайшли символ кінця рівня
            while line[0] != "]":
                # зчитуємо рядковий рівень
                line = level_file.readline()
                # якщо немає символу кінця рівня
                if line[0] != "]":
                    # шукаємо символ кінця рядка
                    endLine = line.find("|")
                    # додаємо в рівень рядок від початку до символу "|"
                    level.append(line[0: endLine])
        # якщо рядок не порожній
        if line[0] != "":
            # розбиваємо його на окремі команди
            commands = line.split()
            # якщо кількість команд > 1, то шукаємо ці команди
            if len(commands) > 1:
                # якщо перша команда - player
                if commands[0] == "player":
                    # записуємо координати героя
                    player_x = int(commands[1])
                    player_y = int(commands[2])
                # якщо перша команда portal, то створюємо портал
                if commands[0] == "portal":
                    tp = BlockTeleport(int(commands[1]), int(commands[2]), int(commands[3]), int(commands[1]))
                    entities.add(tp)
                    platforms.append(tp)
                    animated_entities.add(tp)
                # якщо перша команда монстра, то створюємо монстра
                if commands[0] == "monster":
                    mn = Monster(int(commands[1]), int(commands[2]), int(commands[3]), int(commands[4]),
                                 int(commands[5]), int(commands[6]))
                    entities.add(mn)
                    platforms.append(mn)
                    monsters.add(mn)

MUSIC_RANDOM_PATH = random.randint(1, 2)
if MUSIC_RANDOM_PATH == 1:
    MUSIC_PATH = 'audio/level_music.wav'
elif MUSIC_RANDOM_PATH == 2:
    MUSIC_PATH = 'audio/level_music1.mp3'
def music():
    # Ініціалізація об'єкту mixer
    mixer.init()
    # Вказуємо шлях до файлу
    mixer.music.load(MUSIC_PATH)
    # Встановлюємо рівень відтворення звуку
    mixer.music.set_volume(0.4)
    # Повторюємо відтворення циклічно
    mixer.music.play(-1)
def music2():
    # Ініціалізація об'єкту mixer
    mixer.init()
    # Вказуємо шлях до файлу
    mixer.music.load(MUSIC_LOSE)
    # Встановлюємо рівень відтворення звуку
    mixer.music.set_volume(0.5)
    # Повторюємо відтворення циклічно
    mixer.music.play(1)
def music3():
    # Ініціалізація об'єкту mixer
    mixer.init()
    # Вказуємо шлях до файлу
    mixer.music.load(JUMP)
    # Встановлюємо рівень відтворення звуку
    mixer.music.set_volume(0.5)
    # Повторюємо відтворення циклічно
    mixer.music.play(1)
current_time2 = pygame.time.get_ticks() // 1000

def draw13():
        font = pygame.font.SysFont('grand9kpixelregular', 150)  # Choose a font and size
        win_text = "YOU LOSE"
        text_surface = font.render(win_text, True, (255, 255, 255))  # White color
        screen.blit(text_surface, (380, 280))  # Adjust position as needed
        remaining_time = max(0, target_time2 - (pygame.time.get_ticks() // 1000 - current_time2))
        font = pygame.font.SysFont('grand9kpixelregular', 60)  # Choose a font and size
        win_text = f"Time left: {remaining_time} seconds"
        text_surface = font.render(win_text, True, (WHITE))  # White color
        screen.blit(text_surface, (420, 550))
ICON_DIR = os.path.dirname(__file__)
Menu_fon = '%s/blocks/bg_menu.jpg' % ICON_DIR
quit1 =  '%s/blocks/quit.png' % ICON_DIR
settings1 =  '%s/blocks/settings.png' % ICON_DIR
play1 = '%s/blocks/play.png' % ICON_DIR
back1 = '%s/blocks/back.png' % ICON_DIR
pixel_1 = '%s/blocks/pixel-number-1.png' % ICON_DIR
pixel_2 = '%s/blocks/pixel-number-2.png' % ICON_DIR
music_1 = '%s/blocks/music.png' % ICON_DIR
pashalka = '%s/blocks/pashalka.png' % ICON_DIR
# Ініціалізація Pygame

# Завантаження зображення
image1 = pygame.image.load(Menu_fon)
image2 = pygame.image.load(quit1)
image3 = pygame.image.load(settings1)
image4 = pygame.image.load(play1)
image5 = pygame.image.load(back1)
image6 = pygame.image.load(pixel_1)
image7 = pygame.image.load(pixel_2)
image8 = pygame.image.load(music_1)
image9 = pygame.image.load(pashalka)
image4_rect = image4.get_rect()
image1_rect = image1.get_rect()
image2_rect = image2.get_rect()
image3_rect = image3.get_rect()
image5_rect = image5.get_rect()
image6_rect = image6.get_rect()
image7_rect = image7.get_rect()
image8_rect = image8.get_rect()
image9_rect = image9.get_rect()
# Визначення центральних координат екрану
center_x = WIN_WIDTH // 2
center_y = WIN_HEIGHT // 2
# Визначення позицій зображень поруч із центром екрана, але не точно в центрі і не справа
image4_rect.center = (center_x , center_y + 200) 
image1_rect.center = (center_x, center_y)
image2_rect.center = (center_x - 350, center_y)
image3_rect.center = (center_x + 350, center_y)
image5_rect.center = (center_x - 600, center_y - 300)
image8_rect.center = (center_x - 500, center_y + 150)
image6_rect.center = (center_x - 300, center_y + 150)
image7_rect.center = (center_x - 200, center_y + 150)
image9_rect.center = (center_x, center_y)
# Основний цикл програми

def main():
    screen1 = "menu"
    setoreto = 1
    LOSE1 = 0
    load_level()
    # Ініціація PyGame, обов'язковий рядок
    pygame.init()
    current_time = pygame.time.get_ticks() // 1000
    
    # Створюємо віконце
    screen = pygame.display.set_mode(DISPLAY)
    # Пишемо шапку
    pygame.display.set_caption("Super Mario Bros.")
    # Створення видимої поверхні
    bg = Surface((WIN_WIDTH, WIN_HEIGHT))
    if LEVEL == 3:
        bg.fill(Color(BLUE))
        screen.blit(bg, SCREEN_START)
    # Заливаємо поверхню суцільним кольором
    # За замовчуванням - стоїмо
    left = right = up = running = False
    # Створюємо героя за (x, y) координатами
    hero = Player(player_x, player_y)
    entities.add(hero)

    timer = pygame.time.Clock()
    # Координати
    x = y = 0
    # Весь рядок
    for row in level:
        # Кожний символ
        for col in row:
            if col == "-":
                pf = Platform(x, y)
                entities.add(pf)
                platforms.append(pf)
            if col == "*":
                bd = BlockDie(x, y)
                entities.add(bd)
                platforms.append(bd)
            if col == "P":
                pr = Princess(x, y)
                entities.add(pr)
                platforms.append(pr)
                animated_entities.add(pr)

            x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
        y += PLATFORM_HEIGHT  # то же самое и с высотой
        x = 0  # на каждой новой строчке начинаем с нуля

    total_level_width = len(level[0]) * PLATFORM_WIDTH  # Высчитываем фактическую ширину уровня
    total_level_height = len(level) * PLATFORM_HEIGHT  # высоту

    camera = Camera(camera_configure, total_level_width, total_level_height)
    if setoreto == 1:
        music()
    # Основний цикл програми   
    while not hero.winner:
        if LEVEL == 1488: 
            screen.blit(image9, image9_rect)
            pygame.display.flip()
            time.wait(100000)
        remaining_time = max(0, target_time - (pygame.time.get_ticks() // 1000 - current_time))
        font = pygame.font.SysFont('grand9kpixelregular', 25)  # Choose a font and size
        win_text = f"Time left: {remaining_time} seconds"
        text_surface = font.render(win_text, True, (BLACK_WHITE_STEPTIONISTICKO_STERUGOLI_GRIN))  # White color
        if screen1 == 'menu':
            # Відображення зображення на екрані у вказаних координатах (наприклад, 0, 0)
            screen.fill((255, 255, 255))
            screen.blit(image1, image1_rect)
            screen.blit(image2, image2_rect)
            screen.blit(image3, image3_rect)
            screen.blit(image4, image4_rect)
            screen.blit(text_surface, (35, 50)) 
            pygame.display.flip()
            # Перевірка подій
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Перевірка, чи мишка натиснула на перше зображення
                    if image2_rect.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()
                    if image3_rect.collidepoint(event.pos):
                        screen1 = "settings"
                    if image4_rect.collidepoint(event.pos):
                        screen1 = "play"
        elif screen1  == "settings":
            # Відображення сторінки налаштувань
            # Очищення екрану
            screen.fill((255, 255, 255))
            screen.blit(image1, image1_rect)
            screen.blit(image5, image5_rect)
            font = pygame.font.SysFont('arialblack', 20)  # Choose a font and size
            settings_text1 = "По-перше гра може запускати тільки в розрішенні 1600х900, по іншому не запустить, якшо запустить все буде каряво робити."
            settings_text2 = "Тут не буде неяких налаштувань шкидкості гравця, чи інших змінних, тут можна тільки вибрати яка музика буде грати)"
            settings_text2_1 = "із-за того що я дуже сильно занятий останній час (управляти гравцем на стілки ←↑→)"
            settings_text3 = "і ще бо це за правилами бали не брибавляє бо в правилах написано що треба тільки дати відомості про проект в настройках"
            settings_text4 = "Якщо коротко говорити про гру то це копія 2d гри про маріо, над якою я старався багато бессоних ночей бо днем я був занятий"
            settings_text5 = "НЕКОЛИ НЕ ПИШІТЬ КОЛИ ВИБЕРАЄТЕ ЛЕВЕЛ 1488"
            text_surface1 = font.render(settings_text1, True, (BLACK))  # White color
            screen.blit(text_surface1, (35, 200)) 
            text_surface2 = font.render(settings_text2, True, (BLACK))  # White color
            screen.blit(text_surface2, (35, 230)) 
            text_surface2_1 = font.render(settings_text2_1, True, (BLACK))  # White color
            screen.blit(text_surface2_1, (35, 260)) 
            text_surface3 = font.render(settings_text3, True, (BLACK))  # White color
            screen.blit(text_surface3, (35, 290)) 
            text_surface4 = font.render(settings_text4, True, (BLACK))  # White color
            screen.blit(text_surface4, (35, 320)) 
            text_surface5 = font.render(settings_text5, True, (BLACK))  # White color
            screen.blit(text_surface5, (35, 350)) 
            # Оновлення відображення
            screen.blit(image6, image6_rect)
            screen.blit(image7, image7_rect)
            screen.blit(image8, image8_rect)
            screen.blit(text_surface, (35, 50)) 
            pygame.display.flip()

            # Перевірка подій
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if image5_rect.collidepoint(event.pos):
                        screen1 = "menu"
                    if image6_rect.collidepoint(event.pos):
                        setoreto = 2
                        MUSIC_PATH = 'audio/level_music.wav'
                        # Ініціалізація об'єкту mixer
                        mixer.init()
                        # Вказуємо шлях до файлу
                        mixer.music.load(MUSIC_PATH)
                        # Встановлюємо рівень відтворення звуку
                        mixer.music.set_volume(0.4)
                        # Повторюємо відтворення циклічно
                        mixer.music.play(-1)
                    if image7_rect.collidepoint(event.pos):
                        setoreto = 2
                        MUSIC_PATH = 'audio/level_music1.mp3'
                        # Ініціалізація об'єкту mixer
                        mixer.init()
                        # Вказуємо шлях до файлу
                        mixer.music.load(MUSIC_PATH)
                        # Встановлюємо рівень відтворення звуку
                        mixer.music.set_volume(0.4)
                        # Повторюємо відтворення циклічно
                        mixer.music.play(-1)
        elif screen1 == "play":
            for event in pygame.event.get():
                if event.type == QUIT:
                    raise SystemExit("QUIT")
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        up = True
                    if event.key == K_LEFT:
                        left = True
                    if event.key == K_RIGHT:
                        right = True
                    if event.key == K_LSHIFT:
                        running = True

                if event.type == KEYUP:
                    if event.key == K_UP:
                        up = False
                    if event.key == K_RIGHT:
                        right = False
                    if event.key == K_LEFT:
                        left = False
                    if event.key == K_LSHIFT:
                        running = False
            
            
            # Кожну ітерацію необхідно все перемальовувати
            screen.blit(bg, SCREEN_START)
            # Обчислення залишкового часу
            
                
            # показуємо анімацію
            animated_entities.update()
            # пересуваємо всіх монстрів
            monsters.update(platforms)
            # центризуємо камеру щодо персонажа
            camera.update(hero)
            # пересування
            hero.update(left, right, up, running, platforms)
            

            for entity in entities:
                screen.blit(entity.image, camera.apply(entity))
            screen.blit(text_surface, (35, 50)) 
            if remaining_time == 0:
                LOSE1 = 1
                pygame.init()
                image = pygame.image.load(image_path)
                scaled_image = pygame.transform.scale(image, (1600, 900))
                screen.blit(scaled_image, (0, 0))
                draw13()
                music2()
                pygame.display.update()
                sleep(5)
                break 
                

            timer.tick(FPS)
            # оновлення та виведення всіх змін на екран
            if LOSE1 == 0:
                pygame.display.update()
            
           


level = []
# те, у що ми врізатимемося або спиратимемося
platforms = []
# Всі об'єкти
entities = pygame.sprite.Group()
# Всі анімовані об'єкти, за винятком героя
animated_entities = pygame.sprite.Group()
# Всі об'єкти, що пересуваються
monsters = pygame.sprite.Group()


if __name__ == "__main__":
    main()
