"""
Description: 

"""

# Imports
from tabulate import tabulate
from betonline import BetOnline
from bovada import Bovada

# Global Variables

# Classes

# Functions

# Main
def main():

    print()
    print('Bet Online')
    betonline = BetOnline()
    bet_online_soccer_games = betonline.get_sport('soccer')
    print(bet_online_soccer_games)

    print()
    print('Bovada')
    bovada = Bovada()
    bovada_soccer_games = bovada.get_sport('soccer')
    print(bovada_soccer_games)

    print()
    game_count = 0
    for i in range(len(bet_online_soccer_games)):
        for j in range(len(bovada_soccer_games)):
            if bet_online_soccer_games['Team 1'][i][:4] == bovada_soccer_games['Team 1'][j][:4] and \
                bet_online_soccer_games['Team 2'][i][:4] == bovada_soccer_games['Team 2'][j][:4]:

                game_count += 1
                headers = ['', bet_online_soccer_games['Team 1'][i], bet_online_soccer_games['Team 2'][i], 'Draw']
                table = [['Bet Online', bet_online_soccer_games['Odds 1'][i], bet_online_soccer_games['Odds 2'][i], bet_online_soccer_games['Draw'][i]],
                        ['Bovada', bovada_soccer_games['Odds 1'][j], bovada_soccer_games['Odds 2'][j], bovada_soccer_games['Draw'][j]]]

                print('Game', game_count, ':', bet_online_soccer_games['Team 1'][i], 'vs', bet_online_soccer_games['Team 2'][i])
                print(tabulate(table, headers=headers, tablefmt='simple_grid', numalign='right', floatfmt='.2f'))
                print()

if __name__ == "__main__":
    main()

