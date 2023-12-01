import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
import time
from random import sample

class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self) -> None:
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("外星人入侵")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._creat_alien_line()
        self.last_alien_time = time.time()

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._creat_alien_fleet()
            self.aliens.update()
            self._update_screen()

    def _check_events(self):
        """监视键盘和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # 移动飞船
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self,event):
        """处理键盘按下事件"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()
    
    def _check_keyup_events(self,event):
        """处理键盘松开事件"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _update_screen(self):
        """更新屏幕元素并显示"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        # 让最近绘制的屏幕可见
        pygame.display.flip()
    
    def _fire_bullet(self):
        """创建一颗子弹"""
        if len(self.bullets) < self.settings.bullets_allowed:
            self.bullets.add(Bullet(self))

    def _update_bullets(self):
        """更新子弹位置并删除消失的子弹"""

        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
    
    def _creat_alien_fleet(self):
        """创建外星人舰队，连续不断的外星人"""
        cur_time = time.time()
        if cur_time - self.last_alien_time >= self.settings.aliens_creat_gap:
            self._creat_alien_line()
            self.last_alien_time = cur_time
    def _creat_alien_line(self):
        """创建一行随机生成的外星人"""

        # 随机生成一行外星人的x坐标
        alien_width = Alien(self).rect.width
        random_x = sorted(sample(range(0,self.settings.screen_width - alien_width),self.settings.aliens_per_row))
        # 确保任意两个外星人之间的距离大于外星人的宽度
        while any(abs(random_x[i] - random_x[i + 1]) < alien_width for i in range(self.settings.aliens_per_row - 1)):
            random_x = sorted(sample(range(0,self.settings.screen_width - alien_width),self.settings.aliens_per_row))
        for x in random_x:
            self._creat_alien(x)

    def _creat_alien(self, x, y=0):
        """在(x, y)点创建一个外星人"""
        alien = Alien(self)
        alien.rect.x = x
        alien.rect.y = y
        self.aliens.add(alien)

if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
