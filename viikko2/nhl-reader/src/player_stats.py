from player_reader import PlayerReader

class PlayerStats:
    def __init__(self, data):
        self.all_players = data.get_players()

    def top_scorers_by_nationality(self, nationality):
        player_list = [p for p in self.all_players if p.nationality == nationality]
        player_list.sort(key=lambda p: p.points, reverse=True)
        
        return player_list