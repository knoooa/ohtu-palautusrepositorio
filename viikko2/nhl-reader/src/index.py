import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    response = requests.get(url).json()

    #print("JSON-muotoinen vastaus:")
    #print(response)

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    print("Oliot:")

#    for player in players:
#        if player.nationality == "FIN":
#            print(player)

    FIN = [p for p in players if p.nationality == "FIN"]
    FIN.sort(key=lambda p: p.points, reverse=True)

    for player in FIN:
        print(player)

if __name__ == "__main__":
    main()