class Settings:
    """储存游戏的设置的类"""

    def __init__(self) -> None:
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船属性
        self.ship_speed = 0.4