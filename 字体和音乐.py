import pygame
import sys
import time
from pygame.locals import *

pygame.init()
pygame.display.set_caption("py游戏")  # 设置当前窗口标题
size = width, height = 400, 600
screen = pygame.display.set_mode(size)

# 定义颜色
BLACK = "#000000"
RED = "#FF0000"
# 加载图像
background = pygame.image.load("./resource/AnimatedStreet.png")
# 设置FPS
FPS = 60
clock = pygame.time.Clock()
# 设置文字
font_big = pygame.font.SysFont("华文琥珀", 60)
font_small = pygame.font.SysFont("Verdana", 40)
game_over = font_big.render("游戏结束", True, BLACK)
# 定义分数
SCORE = 0
# 播放音乐
pygame.mixer.Sound("./resource/background.wav").play(-1)  # 默认参数为0 ，表示音乐播放一次， -1 表示无限循环

# 定义玩家类, 继承sprite
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()  # 调用父类的init初始化方法
        self.image = pygame.image.load("./resource/Player.png")  # 返回底图层
        self.rect = self.image.get_rect(center=(width / 2, height - 48))

    def move(self):
        # 监听键盘事件放在for循环外面，否则只会处理一次事件。   for循环外面可以随着图像刷新持续监听
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -10)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 10)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-10, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(10, 0)


# 定义敌人类, 继承sprite
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()  # 调用父类的init初始化方法
        self.image = pygame.image.load("./resource/Enemy.png")  # 返回底图层
        self.rect = self.image.get_rect(left=100, top=0)

    def move(self):
        global SCORE
        self.rect.y += 5
        if self.rect.top > height:
            SCORE += 1
            self.rect.top = 0  # 敌人到达底部后，又重新回到顶部


# 初始化对象
player = Player()
enemy = Enemy()

# 定义sprite组
spriteList = pygame.sprite.Group()
spriteList.add(enemy)

# 定义全部的sprite组，优化代码，下面for循环遍历，避免重复的绘制图像和调用move()方法。
All_SpriteList = pygame.sprite.Group()
All_SpriteList.add(player)
All_SpriteList.add(enemy)

while True:
    # 绘制图像
    screen.blit(background, (0, 0))
    score = font_small.render(str(SCORE),True,BLACK)
    screen.blit(score,(10,10))
    # screen.blit(player.image, player.rect)  # 对图像的局部区域进行绘制或者刷新
    # screen.blit(enemy.image, enemy.rect)
    # player.move()
    # enemy.move()

    for sprite in All_SpriteList:
        screen.blit(sprite.image, sprite.rect)
        sprite.move()

    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()  # 系统退出

    # 检测碰撞，利用spritecollide(), True,表示碰撞后，将会移除

    # 1.撞车后敌人和玩家 都存在
    # if pygame.sprite.spritecollide(player, spriteList, False):
    #     print("撞车了！")
    # 2.撞车后敌人和玩家 敌人消失
    # if pygame.sprite.spritecollide(player, spriteList, True):
    #     print("撞车了！")
    # 3.撞车后敌人和玩家，敌人全部消失
    # if pygame.sprite.spritecollide(player, spriteList, True):
    #     player.kill()
    #     print("撞车了！")
    # 4.撞车后敌人和玩家消失  游戏结束
    if pygame.sprite.spritecollide(player, spriteList, False):
        pygame.mixer.Sound("./resource/crash.wav").play() # 撞车音乐
        time.sleep(1)

        screen.fill(RED)
        screen.blit(game_over, (80, 150))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()  # 系统退出

    pygame.display.update()
    clock.tick(FPS)
