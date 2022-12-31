# Imports
import helper
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from tabulate import tabulate

class EveryGame:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.sports = ['soccer']

    def list_sports(self):
        print('EveryGame:')
        for sport in self.sports:
            print(sport)

    def get_sport(self, sport):
        if sport == 'soccer':
            return self.get_soccer()
        else:
            print('Sport not supported.')

    def get_soccer(self):
        data = pd.DataFrame(columns=['Team 1', 'Team 2', 'Odds 1', 'Odds 2', 'Draw'])

        self.driver.get('https://sports.everygame.eu/en/Bets/Soccer/English-Premier-League/923')
        self.driver.implicitly_wait(8)

        html = self.driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        match_winner = soup.find_all('div', id='1')
        games = match_winner.find_all('div', class_='onemarket tr')
        print(games)

        # print()
        for idx, game in enumerate(games):

            if (idx >= len(games) / 2):
                break

            team1 = game.find('div', class_='game-line__home-team').text
            team2 = game.find('div', class_='game-line__visitor-team').text
            # print('Game', idx + 1, ':', team1, 'vs', team2)

            odds = game.find_all('button', class_='lines-odds')
            odds1 = helper.american_to_decimal(odds[4].text.strip())