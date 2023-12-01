import pygame

class Ship:
    """管理飞船的类"""

    def __init__(self, ai_game) -> None:
        "初始化飞船，设置初始位置为底部中间"
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # 飞船初始位置设置到底部中间
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """绘制飞船"""
        self.screen.blit(self.image, self.rect)