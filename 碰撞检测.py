import pygame
import sys
from pygame.locals import *

pygame.init()
pygame.display.set_caption("py游戏")  # 设置当前窗口标题
size = width, height = 400, 600
screen = pygame.display.set_mode(size)

# 加载图像
background = pygame.image.load("./resource/AnimatedStreet.png")
# 设置FPS
FPS = 60
clock = pygame.time.Clock()


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
        self.rect = self.image.get_rect(left=width / 2 - 22, top=0)

    def move(self):
        self.rect.y += 5


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
    # 3.撞车后敌人和玩家消失
    if pygame.sprite.spritecollide(player, spriteList, False):
        player.kill()
        print("撞车了！")

    pygame.display.update()
    clock.tick(FPS)
