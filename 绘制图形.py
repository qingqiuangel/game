import pygame
import sys

pygame.init()
pygame.display.set_caption("py游戏")  # 设置当前窗口标题
size = width, height = 500, 500
screen = pygame.display.set_mode(size)

# 定义颜色变量
WHITE = "0xFFFFFF"
BLACK = "0x000000"
screen.fill(WHITE)
while True:
    # 在坐标(100，50)处，画一个半径为30的黑色的圆
    pygame.draw.circle(screen, BLACK, (100, 50), 30)
    # 画一个蓝色的，以坐标为(150，130)为起点，坐标(170,170)终点的线
    pygame.draw.line(screen, BLACK, (150, 130), (130, 170))
    # 画一个红色的，左上方的坐标点为(100,200),宽100，高50的，边框宽度为2的矩形
    pygame.draw.rect(screen, BLACK, (100, 200, 100, 50), 2)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()     # 系统退出