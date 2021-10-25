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

# 添加用户自定义事件
OTF_RANGE = pygame.USEREVENT + 1


# 定义玩家类
class Player:
    def __init__(self):
        self.image = pygame.image.load("./resource/Player.png")  # 返回底图层
        self.rect = self.image.get_rect(center=(width / 2, height - 48))

    def move(self):
        mouseX, mouseY = pygame.mouse.get_pos()
        # 触发用户自定义事件，将自定义的事件放入event检测池
        if self.rect.left < 40 or self.rect.right > 360:
            pygame.event.post(pygame.event.Event(OTF_RANGE))

        # 将鼠标位置默认定位在rect的中心
        # 控制鼠标，不让小车出边界. X范围为  矩阵宽度的一半<x<backgorund宽度-矩阵宽度的一半。 高以此类推
        if self.rect.width / 2 <= mouseX <= width - self.rect.width / 2 and self.rect.height / 2 <= mouseY <= height - self.rect.height / 2:
            self.rect.center = (mouseX, mouseY)


# 初始化对象
player = Player()

while True:
    screen.blit(background, (0, 0))
    screen.blit(player.image, player.rect)  # 对图像的局部区域进行绘制或者刷新
    player.move()

    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()  # 系统退出
        if event.type == OTF_RANGE:
            print("汽车越界！")

    pygame.display.update()
    clock.tick(FPS)
