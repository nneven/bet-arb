# Imports
import helper
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from tabulate import tabulate

class Bovada:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.sports = ['soccer']

    def list_sports(self):
        print('Bovada Sports:')
        for sport in self.sports:
            print(sport)

    def get_sport(self, sport):
        if sport == 'soccer':
            return self.get_soccer()
        else:
            print('Sport not supported.')

    def get_soccer(self):
        data = pd.DataFrame(columns=['Team 1', 'Team 2', 'Odds 1', 'Odds 2', 'Draw'])

        self.driver.get('https://www.bovada.lv/sports/soccer/europe/england/premier-league')
        self.driver.implicitly_wait(8)

        html = self.driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        games = soup.find_all('sp-coupon')

        # print()
        for idx, game in enumerate(games):

            teams = game.find('div', class_='competitors')
            teams = teams.find_all('span', class_='name')
            team1 = teams[0].text
            team2 = teams[1].text
            # print('Game', idx + 1, ':', team1, 'vs', team2)

            odds = game.find_all('sp-three-way-vertical', class_='market-type')[1]
            odds = odds.find_all('span', class_='bet-price')
            odds1 = helper.american_to_decimal(odds[0].text.strip())
            odds2 = helper.american_to_decimal(odds[1].text.strip())
            odds3 = helper.american_to_decimal(odds[2].text.strip())
            # print(tabulate([[odds1, odds2, odds3]], headers=[team1, team2, 'Draw'], tablefmt='simple_grid'))

            implied_prob = [1 / odds1, 1 / odds2, 1 / odds3]
            # print('Total Implied Probability:', round(sum(implied_prob), 5))
            # print()

            data = data.append({'Team 1': team1, 'Team 2': team2, 'Odds 1': odds1, 'Odds 2': odds2, 'Draw': odds3}, ignore_index=True)

        return data
