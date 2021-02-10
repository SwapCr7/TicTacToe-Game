'''
Game TicTacToe
Made By: Swapnil Nakum
'''
import random
from enum import Enum

class TicTacToe:
    class STATES(Enum):
        CROSS_TURN = 0
        NAUGHT_TURN = 1
        DRAW = 2
        CROSS_WON = 3
        NAUGHT_WON = 4
    def __init__(self):
        pass
    #displaying the board
    def show_board(self,board):
        print("  " + board[7] + " |  " + board[8] + " |  " + board[9] + "  ")
        print("--------------")
        print("  " + board[4] + " |  " + board[5] + " |  " + board[6] + "  ")
        print("--------------")
        print("  " + board[1] + " |  " + board[2] + " |  " + board[3] + "  ")

    #asking for player1 which symbol to Choose and returning it as a tuple
    def players_choice(self):
        symbol = ''
        while not (symbol == 'X' or symbol == 'O'):
            symbol = input('Player 1: Do you want to be X or O? ').upper()
        if symbol == 'X':
            return ('X', 'O')
        else:
            return ('O', 'X')

    #placing the symbol to the position given by the player
    def place_marker(self,board, symbol, position):
        board[position] = symbol

    #check condition for all the possible combination
    def win_condition(self,board,symbol):
        return ((board[3] == symbol and board[2] == symbol and board[1] == symbol) or # across the bottom
        (board[6] == symbol and board[5] == symbol and board[4] == symbol) or # across the middle
        (board[9] == symbol and board[8] == symbol and board[7] == symbol) or # across the top
        (board[1] == symbol and board[4] == symbol and board[7] == symbol) or # down the middle
        (board[2] == symbol and board[5] == symbol and board[8] == symbol) or # down the middle
        (board[3] == symbol and board[6] == symbol and board[9] == symbol) or # down the right side
        (board[1] == symbol and board[5] == symbol and board[9] == symbol) or # diagonal
        (board[3] == symbol and board[5] == symbol and board[7] == symbol))   # diagonal

    #randomly accessing the first turn
    def first_turn(self):
        if random.randint(0, 1) == 0:
            return 'Player 2'
        else:
            return 'Player 1'

    #checking if the position if empty or not
    def empty_space(self,board, position):
        return board[position] == ' '

    #checking if the board is full
    def full_board_check(self,board):
        for i in range(1,10):
            if self.empty_space(board, i):
                return False
        return True

    #ask for the player for their position
    def ask_choice(self,board,player_marker):
        position = 0
        while position not in [1,2,3,4,5,6,7,8,9] or not self.empty_space(board, position):
            if player_marker == 'X':
                position = int(input('{}(CROSS_TURN) choose your next position: (1-9) '.format(player_marker)))
            else:
                position = int(input('{}(NAUGHT_TURN) choose your next position: (1-9) '.format(player_marker)))
        return position
    def play_again(self):
        user_input = input('Do you want to play again? Enter Yes or No: ').lower()
        while user_input != "yes" and user_input != "no":
            user_input = input('Do you want to play again? Enter Yes or No: ').lower()
        if user_input == 'yes' :
            return True
        else:
            return False

def main():
    print('Welcome')
    while True:
        theBoard = [' '] * 10 #empty list of 10 elements long. Ignore position at zero for the simplicity of the game.
        game = TicTacToe() # create a instance of the TicTacToegame
        player1_marker, player2_marker = game.players_choice() #assigning the symbol(X or O) to the players
        player_turn = game.first_turn() #randomly choosing which player to go
        if player_turn == "Player 1":
            print(player1_marker+ '({}) will go first.'.format(player_turn)) #displaying the player's marker and turn
        else:
            print((player2_marker) + '({}) will go first.'.format(player_turn))
        game_state = True
        # this loop will run till there is tie or any one player has won the game
        while game_state:
            if player_turn == 'Player 1':
                game.show_board(theBoard) #display the board
                position = game.ask_choice(theBoard,player1_marker) # ask for player 1 choice and checks if that position is available or not
                game.place_marker(theBoard, player1_marker, position) # place the marker at the position
                if game.win_condition(theBoard, player1_marker): #checks for player1 condition
                    game.show_board(theBoard)
                    if player1_marker == 'X' :
                        print('Congratulations CROSS_WON(3)')
                    else:
                        print('Congratulations NAUGHT_WON(4)')
                    game_state = False
                else:
                    if game.full_board_check(theBoard): #checks if the board is full then it's a draw and break out of the loop
                        game.show_board(theBoard)
                        print("It's a DRAW(2)")
                        break
                    else:
                        player_turn = 'Player 2' # if there is not a tie then it's player 2 turn
            else:
                game.show_board(theBoard) #display the board
                position = game.ask_choice(theBoard, player2_marker) # ask for player 2 choice and checks if that position is available or not
                game.place_marker(theBoard, player2_marker, position) # place the marker at the position
                if game.win_condition(theBoard, player2_marker): #checks for player12 condition
                    game.show_board(theBoard)
                    if player2_marker == 'X':
                        print('Congratulations CROSS_WON(3)')
                    else:
                        print('Congratulations NAUGHT_WON(4)')
                    game_state = False
                else:
                    if game.full_board_check(theBoard): #checks if the board is full then it's a draw and break out of the loop
                        game.show_board(theBoard)
                        print('The game is a draw!')
                        break
                    else:
                        player_turn = 'Player 1'  # if there is not a tie then it's player 1 turn

        if not game.play_again():
            break

if __name__ == '__main__':
    main()
