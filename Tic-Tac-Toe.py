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
    new_game_variables()    
    welcome()
    number_of_players()
    display_board()
   

def welcome():
#Prints a welcome message.
    print('''
X O X O X O X O
X Tic-Tac-Toe O
X O X O X O X O
 
    ''')
    
def display_board():
#Displays the board.
    global a1
    global a2
    global a3
    global b1
    global b2
    global b3
    global c1
    global c2
    global c3
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

def show_symbol(y):
    #This Function determines what to show in the square in display board.
    #Either an X, O or a space.
    if y.lower() == 'x':
        return 'X'
    elif y.lower() == 'o':
        return 'O'
    else:
        return ' '

def number_of_players():
    #Gets the number of players and sets the second_player variable
    global second_player
    x = input('Please enter how many players, 1 or 2:')
    if x == '2':
        second_player = True
    else:
        second_player = False
    

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

def new_game_variables():
    #Sets the variables back to default for a new game.
    #Sets grid variables back to default
    global a1
    global a2
    global a3
    global b1
    global b2
    global b3
    global c1
    global c2
    global c3

    a1 = 'a'
    a2 = 'a'
    a3 = 'a'
    b1 = 'a'
    b2 = 'a'
    b3 = 'a'
    c1 = 'a'
    c2 = 'a'
    c3 = 'a'
    
    #Sets second player to false at start.
    global second_player
    second_player = False
    
    #Sets the players turn to player 1
    global player_turn
    player_turn = 1




    
#creates variables for the squares.
a1 = 'a'
a2 = 'a'
a3 = 'a'
b1 = 'a'
b2 = 'a'
b3 = 'a'
c1 = 'a'
c2 = 'a'
c3 = 'a'

#Sets second player to false at start.
second_player = False

#Sets the players turn to player 1
player_turn = 1

