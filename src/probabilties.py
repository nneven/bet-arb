"""
Description: 

"""

# Imports
import itertools
import numpy as np

# Global Variables


# Classes
from tabulate import tabulate
from adapters.betonline import BetOnline
from adapters.bovada import Bovada
from adapters.mybookie import MyBookie
from adapters.everygame import EveryGame

# Functions

# Main
def main():

    games = {}

    print()
    print('Bet Online')
    betonline = BetOnline()
    games['BetOnline'] = betonline.get_sport('soccer')
    print(games['BetOnline'])

    print()
    print('Bovada')
    bovada = Bovada()
    games['Bovada'] = bovada.get_sport('soccer')
    print(games['Bovada'])

    print()
    print('MyBookie')
    mybookie = MyBookie()
    games['MyBookie'] = mybookie.get_sport('soccer')
    print(games['MyBookie'])

    # print()
    # print('EveryGame')
    # everygame = EveryGame()
    # games['EveryGame'] = everygame.get_sport('soccer')
    # print(games['EveryGame'])

    print()
    matches_found = 0
    max_bookie_key = max(games, key=lambda x: len(games[x]))
    max_bookie_df = games[max_bookie_key]

    for idx, game in max_bookie_df.iterrows():
        cluster = []
        cluster.append(game)
        for bookie in games:
            if bookie == max_bookie_key:
                continue
            bookie_df = games[bookie]
            # print(bookie)
            for idx2, game2 in bookie_df.iterrows():
                # TODO: BAD DATA, should not need to strip whitespace
                # print(game['Team 1'].strip()[0:4], game2['Team 1'].strip()[0:4])
                if game['Team 1'].strip()[0:4] == game2['Team 1'].strip()[0:4]:
                    # print('Match Found')
                    cluster.append(game2)
                    break
        
        # print(cluster)

        if len(cluster) > 1:
            matches_found += 1
            headers = ['', cluster[0]['Team 1'], cluster[0]['Team 2'], 'Draw']
            table = []
            for bookie in cluster:
                table.append([bookie['Bookie'], bookie['Odds 1'], bookie['Odds 2'], bookie['Draw']])
            print('Game', matches_found, ':', cluster[0]['Team 1'], 'vs', cluster[0]['Team 2'])
            print(tabulate(table, headers=headers, tablefmt='simple_grid', numalign='right', floatfmt='.2f'))

            team1_odds = []
            team2_odds = []
            draw_odds = []
            for bookie in cluster:
                team1_odds.append(bookie['Odds 1'])
                team2_odds.append(bookie['Odds 2'])
                draw_odds.append(bookie['Draw'])

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

            best_comb = np.round(combinations[implied_probs.index(min(implied_probs))], 2)
            print(f'Best Bet: {best_comb}, Probability: {min(implied_probs):.2f}')
            print()

    
    # for i in range(len(bet_online_soccer_games)):
    #     for j in range(len(bovada_soccer_games)):
    #         if bet_online_soccer_games['Team 1'][i][:4] == bovada_soccer_games['Team 1'][j][:4] and \
    #             bet_online_soccer_games['Team 2'][i][:4] == bovada_soccer_games['Team 2'][j][:4]:

    #             game_count += 1
    #             headers = ['', bet_online_soccer_games['Team 1'][i], bet_online_soccer_games['Team 2'][i], 'Draw']
    #             table = [['Bet Online', bet_online_soccer_games['Odds 1'][i], bet_online_soccer_games['Odds 2'][i], bet_online_soccer_games['Draw'][i]],
    #                     ['Bovada', bovada_soccer_games['Odds 1'][j], bovada_soccer_games['Odds 2'][j], bovada_soccer_games['Draw'][j]]]

    #             # print('Game', game_count, ':', bet_online_soccer_games['Team 1'][i], 'vs', bet_online_soccer_games['Team 2'][i])
    #             print(tabulate(table, headers=headers, tablefmt='simple_grid', numalign='right', floatfmt='.2f'))

    #             odds = [[bet_online_soccer_games['Odds 1'][i], bovada_soccer_games['Odds 1'][j]],
    #                     [bet_online_soccer_games['Odds 2'][i], bovada_soccer_games['Odds 2'][j]],
    #                     [bet_online_soccer_games['Draw'][i], bovada_soccer_games['Draw'][j]]]

    #             combinations = [comb for comb in itertools.product(*odds)]

    #             implied_probs = []
    #             for odd_comb in combinations:
    #                 team1_prob = 1 / odd_comb[0]
    #                 team2_prob = 1 / odd_comb[1]
    #                 draw_prob = 1 / odd_comb[2]
    #                 implied_prob = team1_prob + team2_prob + draw_prob
    #                 implied_probs.append(implied_prob)

    #             # for idx, comb in enumerate(combinations):
    #             #     formatted_comb = [f'{odd:.2f}' for odd in comb]
    #             #     print(f'Combination {idx + 1}: {formatted_comb}, Implied Probability: {implied_probs[idx]:.2f}')

    #             best_comb = np.round(combinations[implied_probs.index(min(implied_probs))], 2)
    #             print(f'Best Bet: {best_comb}, Probability: {min(implied_probs):.2f}')
    #             print()


if __name__ == "__main__":
    main()

