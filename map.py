import os
import pygame
from display import *
from file import *

class Map(pygame.sprite.Sprite):
    def __init__(self, speed=1, is_alt=1):
        # 定义对象的属性
        image_src = os.getcwd() + "\\images\\background.png"
        self.image = pygame.image.load(image_src)
        self.rect = self.image.get_rect()
        self.speed = speed

        # 2.判断是否交替图像，如果是需要设置初始位置
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        # 在屏幕的垂直方向上移动
        self.rect.y += self.speed

        if self.rect.y >= Reader().getContent("size")[1]:
            self.rect.y = -self.rect.height
