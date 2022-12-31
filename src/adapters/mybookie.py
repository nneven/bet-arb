# Imports
import pandas as pd
import utils.helper as helper
from selenium import webdriver
from bs4 import BeautifulSoup
from tabulate import tabulate

class MyBookie:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.sports = ['soccer']

    def list_sports(self):
        print('MyBookie Sports:')
        for sport in self.sports:
            print(sport)
    
    def get_sport(self, sport):
        if sport == 'soccer':
            return self.get_soccer()
        else:
            print('Sport not supported.')

    def get_soccer(self):
        data = pd.DataFrame(columns=['Bookie', 'Team 1', 'Team 2', 'Odds 1', 'Odds 2', 'Draw'])

        self.driver.get('https://www.mybookie.ag/sportsbook/english-premier-league/')
        self.driver.implicitly_wait(8)

        html = self.driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        games = soup.find_all('div', class_='game-line py-3')

        # print()
        for idx, game in enumerate(games):

            if (idx >= len(games) / 2):
                break

            team1 = game.find('div', class_='game-line__home-team').text.strip()
            team2 = game.find('div', class_='game-line__visitor-team').text.strip()
            # print('Game', idx + 1, ':', team1, 'vs', team2)

            odds = game.find_all('button', class_='lines-odds')
            odds1 = helper.american_to_decimal(odds[4].text.strip())
            odds2 = helper.american_to_decimal(odds[1].text.strip())
            odds3 = helper.american_to_decimal(odds[6].text.strip().replace('Draw ', ''))
            # print(tabulate([[odds1, odds2, odds3]], headers=[team1, team2, 'Draw'], tablefmt='simple_grid'))

            implied_prob = [1 / odds1, 1 / odds2, 1 / odds3]
            # print('Total Implied Probability:', round(sum(implied_prob), 5))
            # print()

            data = data.append({'Bookie': 'MyBookie', 'Team 1': team1, 'Team 2': team2, 'Odds 1': odds1, 'Odds 2': odds2, 'Draw': odds3}, ignore_index=True)

        return data
