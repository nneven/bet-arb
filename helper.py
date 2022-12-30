def american_to_decimal(american_odds):
    american_odds = int(american_odds) 
    if american_odds >= 0: 
        decimal_odds = (american_odds / 100) + 1
    else:
        decimal_odds = 100 / (-1 * american_odds) + 1
    return decimal_odds