class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.m_score1 += 1
        elif player_name == self.player2_name:
            self.m_score2 += 1
        
    def game_is_deuce(self):
        return self.m_score1 >= 3 and self.m_score2 == self.m_score1
    
    def game_is_advantage(self):
        score_diff = self.m_score1 - self.m_score2
        return (self.m_score1 >= 4 or self.m_score2 >= 4) and abs(score_diff) == 1
    
    def game_is_win(self):
        score_diff = self.m_score1 - self.m_score2
        return (self.m_score1 >= 4 or self.m_score2 >= 4) and abs(score_diff) >= 2
    
    def game_is_equal(self):
        return self.m_score1 == self.m_score2
    
    def get_score(self):
        SCORES = ["Love", "Fifteen", "Thirty", "Forty"]

        if self.game_is_deuce():
            return "Deuce"
        
        if self.game_is_advantage():
            if self.m_score1 > self.m_score2:
                return f"Advantage {self.player1_name}"
            else:
                return f"Advantage {self.player2_name}"
        
        if self.game_is_win():
            if self.m_score1 > self.m_score2:
                return f"Win for {self.player1_name}"
            else:
                return f"Win for {self.player2_name}"
        
        if self.game_is_equal():
            return f"{SCORES[self.m_score1]}-All"

        return f"{SCORES[self.m_score1]}-{SCORES[self.m_score2]}"