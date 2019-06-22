import sys
import random
import tests

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
    def __init__(self, players = 1, logId = 1, board = [], turn = 0, gamestate = 0, nextPlayer = X):
        self.players = int(players)
        self.logId = int(logId)
        self.board = board
        self.turn = int(turn)
        self.gamestate = int(gamestate)
        self.nextPlayer = nextPlayer

        if(logId > 1):
            print("Initiating gave with state:")
            print("\tplayers:    ", players)
            print("\tlogId:      ", logId)
            print("\tboard:      ", board)
            print("\tturn:       ", turn)
            print("\tgamestate:  ", gamestate)
            print("\tnextPlayer: ", nextPlayer)

class TTT:
    # Prints board
    def printBoard(self, board):
        print("\n")
        print(" %s | %s | %s " %(board[0], board[1], board[2]))
        print("---+---+---")
        print(" %s | %s | %s " %(board[3], board[4], board[5]))
        print("---+---+---")
        print(" %s | %s | %s " %(board[6], board[7], board[8]))
    
    # Prints arguments guide
    def printArgsGuide(self):
        print("\nWhen starting the program, enter any of these flags in any order to activate them:")
        print("\t-help, -h: prints all help available and quit, default off")
        print("\t-tests, -t: run tests and quit, default off")
        print("\t-players, -p + int: number of players, 1 or 2, default 1")
        print("\t-logId, -l + int: log id, higher id means more information is printed, 0 to 2, default 1")

    # Prints visual guide for input
    def printBoardGuide(self):
        print("\nEnter a number to set a square")
        print("\t 1 | 2 | 3 ")
        print("\t---+---+---")
        print("\t 4 | 5 | 6 ")
        print("\t---+---+---")
        print("\t 7 | 8 | 9 ")

    # Validates users pick is available in board
    def validateMark(self, index, board):
        if(nextMove < 10 and nextMove > 0):
            if(board[index - 1] == " "):
                # if(self.logId > 1):
                #     print("Validate done")

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
        
        # if(state.logId > 1):
        #     print("Mark done")

        return copy

    # From board, find available spaces (" "), add index  to available list, mark random index of available list, aka, a random available index in board
    def botMark(self, turn, board):
        available = []
        i = 0
        while i < len(board):
            if(board[i] == " "):
                available.append(i + 1)

            i += 1

        r = (random.randint(0, (len(available) - 1)) + 0)
        
        # if(state.logId > 0):
        print("Turn %d, Bot chose: %d" %((turn + 1), available[r]))
        
        # if(state.logId > 1):
        #     print("botMark done")

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
        
        # if(state.logId > 1):
        #     print("checkGame done ")

        return 1

# Handle arguments
ttt = TTT()

minPlayers = 1
maxPlayers = 2
minLogId = 0
maxLogId = 2
players = 1
logId = 1

argVMax = 7
nArg = len(sys.argv)
i = 1
while i < nArg:
    try:
        arg = str(sys.argv[i])

        if(arg == "-logid" or arg == "-l"):
            try:
                nextArg = int(sys.argv[i + 1])
                if(nextArg < minLogId or nextArg > maxLogId):
                    print("Incorrect log id, expecting whole number: minimum %d, maximum %d" %(minLogId, maxLogId))
                    quit()

                logId = nextArg
                i += 1
                if(logId > 1):
                    print("Log ID set to ", logId)
            except ValueError and IndexError:
                print("Incorrect log id, expecting whole number: minimum %d, maximum %d" %(minLogId, maxLogId))
                quit()
        elif(arg == "-help" or arg == "-h"):
            if(logId > 1):
                print("Printing help")

            ttt.printArgsGuide()
            ttt.printBoardGuide()
            quit()
        elif(arg == "-test" or arg == "-t"):
            if(logId > 1):
                print("Running tests")

            tests.Tests(logId)
            quit()
        elif(arg == "-players" or arg == "-p"):
            try:
                nextArg = int(sys.argv[i + 1])
                if(nextArg < minPlayers or nextArg > maxPlayers):
                    print("Incorrect number of players, expecting whole number: minimum %d, maximum %d" %(minPlayers, maxPlayers))
                    quit()

                players = nextArg
                i += 1
                if(logId > 1):
                    print("Players set to ", players)
            except ValueError and IndexError:
                print("Incorrect number of players, expecting whole number: minimum %d, maximum %d" %(minPlayers, maxPlayers))
                quit()

    except ValueError:
        print("Invalid arguments, please refer to the guide below.")
        ttt.printArgsGuide()
        quit()

    i += 1

# Initate game loop
board = []
i = 0
while i < 9:
    board.append(" ")
    i += 1
    
state = State(players, logId, board)

if(state.logId > 0):
    print("Welcome to Tic Tac Toe, %d player! Enter 'help' any time for more information." %(state.players))

state.gamestate = 1
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
if(state.logId > 0):
    print("\nFinal board:")

ttt.printBoard(state.board)

if(state.gamestate == 2):
    print("Game finished, X won!")
elif(state.gamestate == 3):
    print("Game finished, O won!")
elif(state.gamestate == 4):
    print("Game finished, draw!")
else: #if(state.gamestate == 0 or state.gamestate == 1):
    print("Game finished, internal error.")