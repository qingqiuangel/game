import pygame
import sys

pygame.init()
pygame.display.set_caption("py游戏")  # 设置当前窗口标题
size = width, height = 400, 600
screen = pygame.display.set_mode(size)

# 加载图像
background = pygame.image.load("./resource/AnimatedStreet.png")
player = pygame.image.load("./resource/Player.png")
x, y = 178, 504
# 设置FPS
FPS = 30
clock = pygame.time.Clock()
while True:
    screen.blit(background, (0, 0))
    screen.blit(player, (x,y))  # 对图像的局部区域进行绘制或者刷新
    y -=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()     # 系统退出
    pygame.display.update()
    clock.tick(FPS)
