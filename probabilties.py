"""
Description: 

"""

# Imports
from betonline import BetOnline
from bovada import Bovada

# Global Variables

# Classes

# Functions

# Main
def main():
    
    print()
    print('Bet Online')
    betonline = BetOnline()
    soccer_games = betonline.get_sport('soccer')
    print(soccer_games)

    print()
    print('Bovada')
    bovada = Bovada()
    soccer_games = bovada.get_sport('soccer')
    print(soccer_games)

if __name__ == "__main__":
    main()

