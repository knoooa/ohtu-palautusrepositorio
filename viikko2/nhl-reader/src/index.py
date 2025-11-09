import requests
from player import Player
from player_reader import PlayerReader
from player_stats import PlayerStats

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    #response = requests.get(url).json()
    #print("JSON-muotoinen vastaus:")
    #print(response)
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    for p in players:
        print(p)

if __name__ == "__main__":
    main()