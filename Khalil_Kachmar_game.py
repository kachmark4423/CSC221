

import Khalil_Kachmar_game_functions as k
import random

# A brief description of the project
# Date
# CSC121- M2Lab Code Modularizing
# Your Name


# Global constants
COMPUTER_WINS = 1
PLAYER_WINS = 2
TIE = 0

# main function
def main():

    result = TIE

    while result==TIE:
        # Get computer number
        computer = random.randint(1, 3)

        # Get player number
        player = int(input('Enter 1 for rock, ' \
                           '2 for paper, 3 for scissors: '))

        print ('Computer chose', k.choiceString(computer))
        print ('You chose', k.choiceString(player))
        
        result = k.rockPaperScissors(computer, player)
        
        if result == TIE:
            print('You made the same choice as ' \
                  'the computer. Starting over')

    if (result == COMPUTER_WINS):
        print ('The computer wins the game')
        play_again = input("Would you like to play again?(yes/no) ")
        if play_again.lower() == 'yes':
            main()
    elif result == PLAYER_WINS:
        print ('You win the game')
        play_again = input("Would you like to play again?(yes/no) ")
        if play_again.lower() == 'yes':
            main()
    else:
        print ('You made an invalid choice. No winner')



# Call the main function.
if __name__ == "__main__":
    main()

