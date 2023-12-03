class GameStatus:
    """"统计游戏信息"""

    def __init__(self, ai_game) -> None:
        self.settings = ai_game.settings
        self.game_active = True
        self.reset_status()
    
    def reset_status(self):
        self.ships_left = self.settings.ship_limit