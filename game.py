import random

# Define classes
class State:
    def __init__(self, players = 1, logId = 1, board = [" ", " ", " ", " ", " ", " ", " ", " ", " "], turn = 0, gamestate = 0, nextPlayer = "X"):
        self.players = int(players)
        self.logId = int(logId)
        self.board = board
        self.turn = int(turn)
        self.gamestate = int(gamestate)
        self.nextPlayer = nextPlayer

        if(logId > 1):
            print("Initiating game with state:")
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
    def validateMark(self, index, state):
        if(index < 10 and index > 0):
            if(state.board[index - 1] == " "):
                if(state.logId > 1):
                    print("Validate done")

                return True
            else:
                if(state.logId > 0):
                    print("Invalid input: You cannot override another mark!")
                return False
        else:
            print("Option out of bounds, enter 'help' for more information.")
            return False

    # Marks the board
    def markBoard(self, index, mark, state):
        copy = state.board
        copy[index - 1] = mark
        
        if(state.logId > 1):
            print("Mark done")

        return copy

    # From board, find available spaces (" "), add index  to available list, mark random index of available list, aka, a random available index in board
    def botMark(self, state):
        available = []
        i = 0
        while i < len(state.board):
            if(state.board[i] == " "):
                available.append(i + 1)

            i += 1

        r = (random.randint(0, (len(available) - 1)) + 0)
        
        if(state.logId > 0):
            print("Turn %d, Bot chose: %d" %((state.turn + 1), available[r]))
        
        if(state.logId > 1):
            print("botMark; r: %d, available[r]: %d, available: %s" %(r, available[r], str(available)))
            print("botMark done")

        return available[r]

    def checkGame(self, state):
        # 3 possible directions to win: horizontal, vertical, and diagonal, 8 combinations
        board = state.board

        horizontal = True if(board[0] != " " and board[0] == board[1] and board[1] == board[2]
            or board[3] != " " and board[3] == board[4] and board[4] == board[5]
            or board[6] != " " and board[6] == board[7] and board[7] == board[8]) else False

        vertical = True if(board[0] != " " and board[0] == board[3] and board[3] == board[6]
            or board[1] != " " and board[1] == board[4] and board[4] == board[7]
            or board[2] != " " and board[2] == board[5] and board[5] == board[8]) else False

        diagonal = True if(board[0] != " " and board[0] == board[4] and board[4] == board[8]
            or board[2] != " " and board[2] == board[4] and board[4] == board[6]) else False

        draw = True if(state.gamestate == 1 and state.turn > 7 or not " " in (",".join(board))) else False

        if(state.logId > 1):
            print("horizontal:    ", horizontal)
            print("vertical:      ", vertical)
            print("diagonal:      ", diagonal)
            print("draw:          ", draw)
            print("checkGame done ")

        if(horizontal or vertical or diagonal):
            player = (state.turn % 2) + 1
            return 2 if player == 1 else 3
        if(draw):
            return 4

        return 1