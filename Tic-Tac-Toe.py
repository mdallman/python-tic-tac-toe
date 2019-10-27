def play_game():
    ###
    #Ask if One or Two players
    #Then create variables
    #Display Board
    #Get location of player input
    #Check if location has been taken
    # if it has ask for new input
    #if it hasn't then assign that location to player x
    #Change the players turn.
    ###
   pass 

def welcome():
    print('''
X O X O X O X O
X Tic-Tac-Toe O
X O X O X O X O

    
    ''')
    
def display_board():
    print('''

   | 1 | 2 | 3 |
 --|---|---|---|
 A | {A1} | {A2} | {A3} |
 --|---|---|---|
 B | {B1} | {B2} | {B3} |
 --|---|---|---|
 C | {C1} | {C2} | {C3} |
 --|---|---|---|


    
    '''.format(A1=show_symbol(a1), A2=show_symbol(a2), A3=show_symbol(a3),
               B1=show_symbol(b1), B2=show_symbol(b2), B3=show_symbol(b3),
               C1=show_symbol(c1), C2=show_symbol(c2), C3=show_symbol(c3)))

def number_of_players():
    pass

def get_player_input():
   pass 

def square_taken():
    pass

def change_player_turn():
    pass

def computer_turn():
    pass

def check_win():
    pass

def show_symbol(y):
    if y.lower() == 'x':
        return 'X'
    elif y.lower() == 'o':
        return 'O'
    else:
        return ' '

welcome()
a1 = 'a'
a2 = 'a'
a3 = 'a'
b1 = 'a'
b2 = 'a'
b3 = 'a'
c1 = 'a'
c2 = 'a'
c3 = 'a'
