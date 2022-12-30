"""
Description: 

"""

# Imports
import itertools
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

                odds = [[bet_online_soccer_games['Odds 1'][i], bovada_soccer_games['Odds 1'][j]],
                        [bet_online_soccer_games['Odds 2'][i], bovada_soccer_games['Odds 2'][j]],
                        [bet_online_soccer_games['Draw'][i], bovada_soccer_games['Draw'][j]]]

                combinations = [comb for comb in itertools.product(*odds)]

                implied_probs = []
                for odd_comb in combinations:
                    team1_prob = 1 / odd_comb[0]
                    team2_prob = 1 / odd_comb[1]
                    draw_prob = 1 / odd_comb[2]
                    implied_prob = team1_prob + team2_prob + draw_prob
                    implied_probs.append(implied_prob)

                for idx, comb in enumerate(combinations):
                    formatted_comb = [f'{odd:.2f}' for odd in comb]
                    print(f'Combination {idx + 1}: {formatted_comb}, Implied Probability: {implied_probs[idx]:.2f}')

                print(f'Best Combination: {combinations[implied_probs.index(min(implied_probs))]}, Lowest Implied Probability: {min(implied_probs):.2f}')

                print()


if __name__ == "__main__":
    main()

