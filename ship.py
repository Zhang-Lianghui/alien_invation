import pygame

class Ship:
    """管理飞船的类"""

    def __init__(self, ai_game) -> None:
        "初始化飞船，设置初始位置为底部中间"
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # 飞船初始位置设置到底部中间
        self.rect.midbottom = self.screen_rect.midbottom

        # 在飞船的属性中储存小数值
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        #飞船移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """根据键盘标志调整飞船位置"""
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        # 判断是否出界
        if self.x > self.screen_rect.right - self.rect.width:
            self.x = self.screen_rect.right - self.rect.width
        if self.x < 0:
            self.x = 0
        if self.y > self.screen_rect.bottom - self.rect.height:
            self.y = self.screen_rect.bottom - self.rect.height
        if self.y < 0:
            self.y = 0
        self.rect.x = self.x
        self.rect.y = self.y
        
    def blitme(self):
        """绘制飞船"""
        self.screen.blit(self.image, self.rect)