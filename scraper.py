from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get('https://www.betonline.ag/sportsbook/soccer/epl/english-premier-league')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

game_dategroup = soup.find_all('div', class_='offering-games__dategroup ng-star-inserted')
print(len(game_dategroup))
