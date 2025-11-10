import requests
from player import Player
from player_reader import PlayerReader
from player_stats import PlayerStats
from rich.console import Console
from rich.table import Table


def main():
    console = Console()
    #response = requests.get(url).json()
    #print("JSON-muotoinen vastaus:")
    #print(response)


    season = input("Anna kausi (muodossa 2024-25): ")
    nationality = input("Anna maan koodi (esim. FIN, SWE, CAN): ").upper()
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"


    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality(nationality)

    if not players:
        console.print(f"[red]Ei pelaajia löytynyt kaudelta {season} maalle {nationality}[/red]")
        return

    table = Table(title=f"NHL {season} – {nationality}", show_lines=True)
    table.add_column("Nimi", justify="left", style="cyan", no_wrap=True)
    table.add_column("Joukkue", justify="center", style="magenta")
    table.add_column("Maa", justify="center", style="yellow")
    table.add_column("Maalit", justify="right", style="green")
    table.add_column("Syötöt", justify="right", style="green")
    table.add_column("Pisteet", justify="right", style="bold white")

    for p in players:
        table.add_row(p.name, p.team, p.nationality, str(p.goals), str(p.assists), str(p.points))

    console.print(table)
    

if __name__ == "__main__":
    main()