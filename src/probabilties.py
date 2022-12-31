"""
Description: 

"""

# Imports
import itertools
import numpy as np
from tabulate import tabulate
from difflib import SequenceMatcher

# Global Variables


# Classes
from adapters.betonline import BetOnline
from adapters.bovada import Bovada
from adapters.mybookie import MyBookie
from adapters.everygame import EveryGame

# Functions

# Main
def main():

    bookie_dict = {}

    print()
    print('Bet Online')
    betonline = BetOnline()
    bookie_dict['BetOnline'] = betonline.get_sport('soccer')
    print(bookie_dict['BetOnline'])

    print()
    print('Bovada')
    bovada = Bovada()
    bookie_dict['Bovada'] = bovada.get_sport('soccer')
    print(bookie_dict['Bovada'])

    print()
    print('MyBookie')
    mybookie = MyBookie()
    bookie_dict['MyBookie'] = mybookie.get_sport('soccer')
    print(bookie_dict['MyBookie'])

    # print()
    # print('EveryGame')
    # everygame = EveryGame()
    # games['EveryGame'] = everygame.get_sport('soccer')
    # print(games['EveryGame'])

    print()
    matches_found = 0
    max_bookie_key = max(bookie_dict, key=lambda bookie: len(bookie_dict[bookie]))
    max_bookie_df = bookie_dict[max_bookie_key]

    for idx, game in max_bookie_df.iterrows():
        cluster = []
        cluster.append(game)
        for bookie in bookie_dict:
            if bookie == max_bookie_key:
                continue
            bookie_games_df = bookie_dict[bookie]
            # print(bookie)
            for idx2, game2 in bookie_games_df.iterrows():
                # TODO: NEED CLEAN DATA
                game1_team1 = game['Team 1'][0:4]
                game1_team2 = game['Team 2'][0:4]
                game2_team1 = game2['Team 1'][0:4]
                game2_team2 = game2['Team 2'][0:4]

                if game1_team1 == game2_team1 and game1_team2 == game2_team2:
                    cluster.append(game2)
                    break
        
        # print(cluster)

        if len(cluster) > 1:
            matches_found += 1
            headers = ['', cluster[0]['Team 1'], cluster[0]['Team 2'], 'Draw']
            table = []
            for bookie_game in cluster:
                table.append([bookie_game['Bookie'], bookie_game['Odds 1'], bookie_game['Odds 2'], bookie_game['Draw']])
            print('Game', str(matches_found) + ':', cluster[0]['Team 1'], 'vs', cluster[0]['Team 2'])
            print(tabulate(table, headers=headers, tablefmt='simple_grid', numalign='right', floatfmt='.2f'))

            team1_odds = []
            team2_odds = []
            draw_odds = []
            for bookie_game in cluster:
                team1_odds.append(bookie_game['Odds 1'])
                team2_odds.append(bookie_game['Odds 2'])
                draw_odds.append(bookie_game['Draw'])

            odds = [team1_odds, team2_odds, draw_odds]
            combinations = [comb for comb in itertools.product(*odds)]
            
            implied_probs = []
            for odd_comb in combinations:
                team1_prob = 1 / odd_comb[0]
                team2_prob = 1 / odd_comb[1]
                draw_prob = 1 / odd_comb[2]
                implied_prob = team1_prob + team2_prob + draw_prob
                implied_probs.append(implied_prob)

            # for idx, comb in enumerate(combinations):
            #     formatted_comb = [f'{odd:.2f}' for odd in comb]
            #     print(f'Combination {idx + 1}: {formatted_comb}, Implied Probability: {implied_probs[idx]:.2f}')

            best_bet = []
            for odd in combinations[np.argmin(implied_probs)]:
                best_bet.append(float(f'{odd:.2f}'))

            print(f'Best Bet: {best_bet}, Probability: {min(implied_probs):.2f}')
            print()


if __name__ == "__main__":
    main()

