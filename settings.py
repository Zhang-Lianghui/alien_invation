class Settings:
    """储存游戏的设置的类"""

    def __init__(self) -> None:
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船属性
        self.ship_speed = 1
        self.ship_limit = 3

        # 子弹属性
        self.bullet_speed = 0.5
        self.bullet_width = 5
        self.bullet_height = 20
        self.bullet_color = (198, 145, 69)
        self.bullets_allowed = 20

        # 外星人属性
        self.alien_speed = 0.1
        self.aliens_creat_gap = 3
        self.aliens_per_row = 4