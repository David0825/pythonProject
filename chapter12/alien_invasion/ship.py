# 创建Ship类，管理飞船的大部分行为
import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """管理飞船的类"""

    def __init__(self, ai_game):
        super().__init__()
        """初始化飞船并设置其初始位置"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('../adding_ship_image/images/ship.bmp')
        self.rect = self.image.get_rect()
        # 对于每艘新飞船，都将其放在屏幕底部的中央
        self.rect.midbottom = self.screen_rect.midbottom
        #定义一个moving_right标志位，为True时，向右+1像素
        self.moving_right = False
        # 定义一个moving_left标志位，为True时，向左+1像素
        self.moving_left = False
        #引入settings
        self.settings = ai_game.settings
        #在飞船的属性x中存储小数
        self.x = float(self.rect.x)

    #允许持续移动
    def update(self):
        """根据移动标志调整飞船的位置"""
        """限制飞船的活动范围"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            #更新飞船而不是rect对象的x值
            # self.rect.x += 1
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            # self.rect.x -= 1
            self.x -= self.settings.ship_speed
        #根据self.x更新rect对象
        self.rect.x = self.x
    def blitme(self):
        """在指定的位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """让飞船在屏幕底端居中"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
