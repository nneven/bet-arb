# Imports
import time
import pandas as pd
import utils.helper as helper
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
        data = pd.DataFrame(columns=['Bookie', 'Team 1', 'Team 2', 'Odds 1', 'Odds 2', 'Draw'])

        self.driver.get('https://sports.everygame.eu/en/Bets/Soccer/English-Premier-League/923')
        self.driver.implicitly_wait(8)

        # Cloudflare bot detection

        html = self.driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        print(soup.prettify())
        