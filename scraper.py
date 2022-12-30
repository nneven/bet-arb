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
    driver.get('https://www.betonline.ag/sportsbook/soccer/epl/english-premier-league')
    driver.implicitly_wait(2)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    game_dategroup = soup.find_all('div', class_='offering-games__dategroup ng-star-inserted')

    print()
    for group in game_dategroup:

        date = group.find('span', class_='offering-games__dategroup-date--desktop')
        print(date.text)
        print()

        games_table = group.find_all('table', class_='offering-games__table')
        for idx, game in enumerate(games_table):

            teams = game.find_all('td', class_='lines-row__team-name')
            if (len(teams) != 3):
                continue
            
            team1 = teams[0].span.text.strip()
            team2 = teams[1].span.text.strip()
            draw = teams[2].span.text.strip()
            print('Game', idx + 1, ':', team1, 'vs', team2)

            odds = game.find_all('td', class_='lines-row__money')
            odds1 = american_odds_to_decimal(odds[0].text.strip())
            odds2 = american_odds_to_decimal(odds[1].text.strip())
            odds3 = american_odds_to_decimal(odds[2].text.strip())
            print(tabulate([[odds1, odds2, odds3]], headers=[team1, team2, draw], tablefmt='simple_grid'))

            implied_prob = [1 / odds1, 1 / odds2, 1 / odds3]
            print('Total Implied Probability:', round(sum(implied_prob), 5))

            print()

if __name__ == "__main__":
    main()

