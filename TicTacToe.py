# prints out the current state of the board
def display_board(board):
  for ls in board:
    print("| {} | {} | {} |".format(ls[0], ls[1], ls[2]))

'''
test cases
display_board([['X', 'X', 'O'], ['X', 'X', 'O'], ['X', 'X', 'O']])
display_board([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
'''

# ask player 1 for its marker and assigns it
def player_input():
  while True:
    p1_marker = input("Player 1: Do you want to be 'X' or 'O'? ").upper()
    if p1_marker == "X":
      return ("X", "O")
      break
    elif p1_marker == "O":
      return ("O", "X")
      break
    else:
      print("Invalid input")

'''
Testing
player_input()
'''

# places marker on board at desired position
def place_marker(board, marker, pos):
  if pos < 4:
    board[0][pos - 1] = marker
  elif pos < 7:
    board[1][pos - 4] = marker
  else:
    board[2][pos - 7] = marker

'''
testing
test_board = [['X','X','O'], ['X','O','X'],['O','X','O']]
place_marker(test_board,'$',8)
display_board(test_board)
'''

#checks the board for a win
def win_check(board, mark):
  return (mark == board[0][0] == board[0][1] == board[0][2] or 
          mark == board[1][0] == board[1][1] == board[1][2] or 
          mark == board[2][0] == board[2][1] == board[2][2] or 
          mark == board[0][0] == board[1][0] == board[2][0] or  
          mark == board[0][1] == board[1][1] == board[2][1] or
          mark == board[0][2] == board[1][2] == board[2][2] or
          mark == board[0][0] == board[1][1] == board[2][2] or 
          mark == board[0][2] == board[1][1] == board[2][0])

'''
test cases
test_board = [['X','X','O'], ['X', 'X', 'X'], ['O','O','X']]
print(win_check(test_board,'X'))
'''

# randomly chooses which player goes first
import random

def choose_first():
    first = random.randint(1, 2)
    if first == 1:
      return "P1"
    else:
      return "P2"

# gets list of legal moves
def legal_moves(board):
  moves = []

  for ls in board:
    for mark in ls:
      if type(mark) == int:
        moves.append(mark)
  
  return moves

'''
test cases
test_board = [['X',2,'O'], [3,'O','X'],['O','X',8]]
print(legal_moves(test_board))
'''

# checks if board is full and returns a boolean value
def is_full(board):
  return legal_moves(board) == []

'''
test cases
test_board = [['X','X','O'], ['O','O','X'],['O','X','x']]
print(is_full(test_board))
'''

# runs game using all of the functions above
def run_game():
  # initialize markers and players
  (p1_marker, p2_marker) = player_input()
  # assigns first player
  turn = choose_first()

  # initializes board
  playing_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

  # prints board for the first time
  display_board(playing_board)

  # plays game
  while not is_full(playing_board):

    # asks and checks for valid move
    while True:
      move = int(input("It is {}'s turn, please enter your move ".format(turn)))
      if move in legal_moves(playing_board):
        break
    
    # Player 1's turn
    if turn == "P1":
      place_marker(playing_board, p1_marker, move)
      display_board(playing_board)
      
      # ends game if P1 wins
      if win_check(playing_board, p1_marker):
        print("P1 wins!")
        exit()
      
      # if game has not ended, change turn
      turn = "P2"

    # Player 2's turn
    elif turn == "P2":
      place_marker(playing_board, p2_marker, move)
      display_board(playing_board)
      
      # ends game if P1 wins
      if win_check(playing_board, p2_marker):
        print("P2 wins!")
        exit()
      
      # if game has not ended, change turn
      turn = "P1"

  # When board is full, end game
  print("Game over. It is a draw!")

# executes the game
run_game()