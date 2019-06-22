import sys
import random

# Gamestate:
# 0 = not initated
# 1 = game active
# 2 = X won
# 3 = O won
# 4 = draw

# User interface
# " 1 | 2 | 3 "
# "---+---+---"
# " 4 | 5 | 6 "
# "---+---+---"
# " 7 | 8 | 9 "

# List actual
# " 0 | 1 | 2 "
# "---+---+---"
# " 3 | 4 | 5 "
# "---+---+---"
# " 6 | 7 | 8 "

# Define consts
X = "X"
O = "O"

# Define classes
class State:
    def __init__(self, players = 1, board = [], turn = 0, gamestate = 0, nextPlayer = X):
        self.players = int(players)
        self.board = board
        self.turn = int(turn)
        self.gamestate = int(gamestate)
        self.nextPlayer = nextPlayer

class TTT:
    # Prints board
    def printBoard(self, board):
        print("\n")
        print(" %s | %s | %s " %(board[0], board[1], board[2]))
        print("---+---+---")
        print(" %s | %s | %s " %(board[3], board[4], board[5]))
        print("---+---+---")
        print(" %s | %s | %s " %(board[6], board[7], board[8]))

    # Prints visual guide for input
    def printBoardGuide(self):
        print("Enter a number to set a square")
        print(" 1 | 2 | 3 ")
        print("---+---+---")
        print(" 4 | 5 | 6 ")
        print("---+---+---")
        print(" 7 | 8 | 9 ")

    # Validates users pick is available in board
    def validateMark(self, index, board):
        if(nextMove < 10 and nextMove > 0):
            if(board[index - 1] == " "):
                # Everything OK
                return True
            else:
                print("Invalid input: You cannot override another mark!")
                return False
        else:
            print("Option out of bounds, enter 'help' for more information.")
            return False
        
        # print("Validate done")

    # Marks the board
    def markBoard(self, index, board, mark):
        copy = board
        copy[index - 1] = mark
        return copy
        
        # print("Mark done")

    # From board, find available spaces (" "), add index  to available list, mark random index of available list, aka, a random available index in board
    def botMark(self, turn, board):
        available = []
        i = 0
        while i < len(board):
            if(board[i] == " "):
                available.append(i + 1)

            i += 1

        r = (random.randint(0, (len(available) - 1)) + 0)
        # self.markBoard(available[r], board, O)
        # print("Botpick; random number: %d, on board: %d" %(r, available[r]))
        print("Turn %d, Bot chose: %d" %((turn + 1), available[r]))
        
        # print("Bot done")
        return available[r]

    def checkGame(self, gamestate, turn, board):
        # 3 possible directions to win: horizontal, vertical, and diagonal, 8 combinations

        horizontal = True if(board[0] != " " and board[0] == board[1] and board[1] == board[2]
            or board[3] != " " and board[3] == board[4] and board[4] == board[5]
            or board[6] != " " and board[6] == board[7] and board[7] == board[8]) else False

        vertical = True if(board[0] != " " and board[0] == board[3] and board[3] == board[6]
            or board[1] != " " and board[1] == board[4] and board[4] == board[7]
            or board[2] != " " and board[2] == board[5] and board[5] == board[8]) else False

        diagonal = True if(board[0] != " " and board[0] == board[4] and board[4] == board[8]
            or board[2] != " " and board[2] == board[4] and board[4] == board[6]) else False

        if(horizontal or vertical or diagonal):
            player = (state.turn % maxPlayers) + 1
            return 2 if player == 1 else 3
        if(gamestate == 1 and turn > 7):
            return 4
        
        return 1

        # print("checkGame done ", state.gamestate)

# Handle arguments
maxPlayers = 2
minPlayers = 1
players = 1

argVMax = 2
nArg = len(sys.argv)
if(nArg == argVMax):
    if(int(sys.argv[1]) < 1 or int(sys.argv[1]) > 2):
        print("Incorrect number of players, expecting minimum %d, maximum %d" %(minPlayers, maxPlayers))
        quit()
    players = sys.argv[1]
elif(nArg > argVMax):
    print("Incorrect number of arguments, expecting 1 (filename), or 2 (filename, number of players)")
    quit()

# Initate game loop
board = []
i = 0
while i < 9:
    board.append(" ")
    i += 1

state = State(players, board)
ttt = TTT()
state.gamestate = 1

print("Welcome to Tic Tac Toe, %d player! Enter 'help' any time for more information." %(state.players))

while(state.gamestate == 1):
    ttt.printBoard(state.board)

    # Get and validate input
    player = (state.turn % maxPlayers) + 1
    state.nextPlayer = X if player == 1 else O
    nextMove = input("Turn %d, player %d please enter a space to place your mark: %s: \n\r" %((state.turn + 1), player, state.nextPlayer))

    try:
        nextMove = int(nextMove)

        # If invalid input, report to user and continue game loop
        if(not ttt.validateMark(nextMove, state.board)):
            continue
    except ValueError:
        nextMove = str(nextMove.lower())
        if(nextMove == "h" or nextMove == "help" or nextMove == "rules"):
            ttt.printBoardGuide()
            continue
        if(nextMove == "q" or nextMove == "quit" or nextMove == "x" or nextMove == "exit"):
            print("Quitting game...")
            quit()
        else:
            print("Unrecognized input, enter 'help' for more information")
            continue

    # Place mark
    state.board = ttt.markBoard(int(nextMove), state.board, state.nextPlayer)

    # Bot mark
    if(state.players < 2):
        state.gamestate = ttt.checkGame(state.gamestate, state.turn, state.board)
        if(state.gamestate == 1):
            ttt.printBoard(state.board)
            botsMark = ttt.botMark(state.turn, state.board)
            state.board = ttt.markBoard(botsMark, state.board, O)
            state.turn += 1
        else:
            break
            

    # Check for win/loss/draw
    state.gamestate = ttt.checkGame(state.gamestate, state.turn, state.board)
    state.turn += 1

# Game finished, return result
ttt.printBoard(state.board)
gameRes = ""

print("\nFinal board:")
if(state.gamestate == 2):
    print("Game finished, X won!")
elif(state.gamestate == 3):
    print("Game finished, O won!")
elif(state.gamestate == 4):
    print("Game finished, draw!")
else: #if(state.gamestate == 0 or state.gamestate == 1):
    print("Game finished, internal error.")