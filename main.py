import sys
import game
import tests
import ai

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
ttt = game.TTT()

# Handle arguments
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

            tests.Controller.run(logId)
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
        elif(arg == "-ai"):
            ai.AI.printExample()
            quit()

    except ValueError:
        print("Invalid arguments, please refer to the guide below.")
        ttt.printArgsGuide()
        quit()

    i += 1

# Initate game
state = game.State(players, logId)

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
        if(not ttt.validateMark(nextMove, state)):
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
    state.board = ttt.markBoard(int(nextMove), state.nextPlayer, state)

    # Bot mark
    if(state.players < 2):
        state.gamestate = ttt.checkGame(state)
        if(state.gamestate == 1):
            ttt.printBoard(state.board)
            botsMark = ttt.botMark(state)
            state.board = ttt.markBoard(botsMark, O, state)
            state.turn += 1
        else:
            break
            

    # Check for win/loss/draw
    state.gamestate = ttt.checkGame(state)
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