#functions needed: get user input, computer move, find winner, score board
import random

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
def get_user_input(): #returns char of users selection
    print('r = rock, p = paper, s = scissors')
    userVal = None
    while 1:
        print('Make your selection:')
        userVal = input()
        #check for valid input
        userVal = userVal.lower()
        if len(userVal) != 1: 
            userVal = None
        if userVal == 'r' or userVal == 'p' or userVal == 's':
            return userVal
        
        userVal = None
        print('Please enter valid input, try again')
    

def generate_computer_move(): #returns char of machine's move
    move = random.randrange(0,3)
    if move == 0:
        return 'r'
    elif move == 1:
        return 'p'
    else:
        return 's'

def calculate_winner(moveHuman: str, moveComputer: str): #returns int for who won
    #rock -> scissors -> paper -> rock
    rockNode = ListNode('r', None)
    paperNode = ListNode('p', rockNode)
    scissorsNode = ListNode('s', paperNode)
    rockNode.next = scissorsNode
    
    userNode = rockNode
    while (userNode.val != moveHuman):
        userNode = userNode.next

    if userNode.val == moveComputer: #they made the same move, its a draw
        return 0
    elif userNode.next.val == moveComputer: #user wins
        return 1
    else:   #computer wins
        return -1

def update_scoreboard(outcome: int, scoreboard: dict):
    scoreboard[outcome] += 1
    return scoreboard
