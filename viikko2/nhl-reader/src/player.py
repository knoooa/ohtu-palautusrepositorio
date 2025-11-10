"""moduuli pelaaja-luokalle"""
class Player:
    """luokka joka luo lista pelaajista"""


    def __init__(self, player_dict):
        self.name = player_dict['name']
        self.team = player_dict['team']
        self.goals = player_dict['goals']
        self.assists = player_dict['assists']
        self.nationality = player_dict['nationality']
        self.points = player_dict['goals'] + player_dict['assists']

    def testi(self):
        """minimimmäärä"""
        return None

    def __str__(self):
        return f"{self.name:25} {self.nationality:6} {self.team:15} {self.points:6}"
