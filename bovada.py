"""
Description: 

"""

# Imports
from selenium import webdriver
from bs4 import BeautifulSoup
from tabulate import tabulate

# Global Variables

# Classes

# Functions
def american_odds_to_decimal(american_odds):
    american_odds = int(american_odds) 
    if american_odds >= 0: 
        decimal_odds = (american_odds / 100) + 1
    else:
        decimal_odds = 100 / (-1 * american_odds) + 1
    return decimal_odds

# Main
def main():
    driver = webdriver.Chrome()
    driver.get('https://www.bovada.lv/sports/soccer/europe/england/premier-league')
    driver.implicitly_wait(1)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    games = soup.find_all('sp-coupon')

    print()
    for idx, game in enumerate(games):

        teams = game.find('div', 'competitors')
        team1 = teams.find('span', 'name').text
        team2 = teams.find('span', 'name').text
        print('Game', idx + 1, ':', team1, 'vs', team2)

if __name__ == "__main__":
    main()

