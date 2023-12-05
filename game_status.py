import json
class GameStatus:
    """"统计游戏信息"""

    def __init__(self, ai_game) -> None:
        self.settings = ai_game.settings
        self.game_active = False
        self.reset_status()
        self.high_score = self.get_high_score()
        #self.level = 1
    
    def reset_status(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def save_high_score(self):
        """保存最高分"""
        with open('high_score.json', 'w') as f:
            json.dump({'high_score':self.high_score}, f)

    def get_high_score(self):
        try:
            with open('high_score.json', 'r') as f:
                return json.load(f).get('high_score', 0)
        except:
            return 0
