import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((500, 500))

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()     #系统结束