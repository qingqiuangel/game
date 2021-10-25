import pygame
import sys

pygame.init()
pygame.display.set_caption("py游戏")  # 设置当前窗口标题
size = width, height = 400, 600
screen = pygame.display.set_mode(size)

# 加载图像
background = pygame.image.load("./resource/AnimatedStreet.png")
# 设置FPS
FPS = 60
clock = pygame.time.Clock()


# 定义玩家类
class Player:
    def __init__(self):
        self.image = pygame.image.load("./resource/Player.png")  # 返回底图层
        self.rect = self.image.get_rect(center=(width / 2, height - 48))

    def move(self):
        self.rect.y -= 1


# 初始化对象
player = Player()

while True:
    screen.blit(background, (0, 0))
    screen.blit(player.image, player.rect)  # 对图像的局部区域进行绘制或者刷新
    player.move()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()  # 系统退出
    pygame.display.update()
    clock.tick(FPS)
