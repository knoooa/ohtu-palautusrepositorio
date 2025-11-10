"""testi"""
import requests
from player import Player

class PlayerReader:
    """luokka pelaajatietojen hakemiseen linkistä"""
    def __init__(self, url):
        self.url = url
    def get_players(self):
        """hakee pelaajatiedot tiedostosta"""
        response = requests.get(self.url, timeout=10).json()
        players = [Player(player_dict) for player_dict in response]
        return players
    def testi(self):
        """minimimmäärä"""
        return None
