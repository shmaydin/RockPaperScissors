import game_mechanics as mechs
import time

#promp user for input
#tell user if they won or lost
#show them the match score - maybe format it
#ask if they want to play again



scoreboard = {1:0, -1:0, 0:0}
charToName = {'r': 'Rock', 's': 'Scissors', 'p' : 'Paper'}
continuePlaying = 'y'
while continuePlaying == 'y':
    userMove = mechs.get_user_input()
    print('\nYou chose: ' + charToName[userMove])
    time.sleep(0.5)

    computerMove = mechs.generate_computer_move()
    print('The machine chose: ' + charToName[computerMove] + '\n')
    time.sleep(1)

    winner = mechs.calculate_winner(userMove, computerMove)
    if winner == 0:
        print("It's a draw")
    elif winner > 0:
        print('You win! Nice playin')
    else:
        print('Machine wins, nice try loser')

    time.sleep(1)
    
    scoreboard = mechs.update_scoreboard(winner, scoreboard)
    print('------------------------------')
    print("User: {userPoints} | Machine: {machinePoints} | Draws: {draws}".format(
        userPoints = scoreboard[1],
        machinePoints = scoreboard[-1],
        draws = scoreboard[0]))
    print('------------------------------\n')

    print("Would you like to play again? ('y' to continue)")
    continuePlaying = input()



