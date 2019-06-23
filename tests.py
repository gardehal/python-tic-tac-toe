import game

X = "X"
O = "O"

class Controller:
    def run(logId):
        print("Running unit tests...")

        tests = Tests()
        testEmptyBoard = tests.testEmptyBoard()
        testMarkBoard = tests.testMarkBoard()
        testMarkSameSpot = tests.testMarkSameSpot()
        testValidateMarkSameSpot = tests.testValidateMarkSameSpot()
        testCheckGameNotFinished = tests.testCheckGameNotFinished()
        testCheckGameDraw = tests.testCheckGameDraw()
        testCheckGameXWin = tests.testCheckGameXWin()
        testCheckGameOWin = tests.testCheckGameOWin()
        testBotMarkAny = tests.testBotMarkAny()
        testBotMarkLastSpot = tests.testBotMarkLastSpot()
        testBotMarkAll = tests.testBotMarkAll()

        finalRes = testEmptyBoard + testMarkBoard + testMarkSameSpot + testValidateMarkSameSpot 
        + testCheckGameNotFinished + testCheckGameDraw + testCheckGameXWin + testCheckGameOWin
        + testBotMarkAny + testBotMarkLastSpot + testBotMarkAll

        if(logId > 0):
            print("testEmptyBoard:               ", "Pass" if not testEmptyBoard else "Failed")
            print("testMarkBoard:                ", "Pass" if not testMarkBoard else "Failed")
            print("testMarkSameSpot:             ", "Pass" if not testMarkSameSpot else "Failed")
            print("testValidateMarkSameSpot:     ", "Pass" if not testValidateMarkSameSpot else "Failed")
            print("testCheckGameNotFinished:     ", "Pass" if not testCheckGameNotFinished else "Failed")
            print("testCheckGameDraw:            ", "Pass" if not testCheckGameDraw else "Failed")
            print("testCheckGameXWin:            ", "Pass" if not testCheckGameXWin else "Failed")
            print("testCheckGameOWin:            ", "Pass" if not testCheckGameOWin else "Failed")
            print("testBotMarkAny:               ", "Pass" if not testBotMarkAny else "Failed")
            print("testBotMarkLastSpot:          ", "Pass" if not testBotMarkLastSpot else "Failed")
            print("testBotMarkAll:               ", "Pass" if not testBotMarkAll else "Failed")
        
        print("All test passed!" if (finalRes == 0) else "One or more tests failed.")

    def before(logId):
        print("Preparing unit test...")
        
        state = game.State(logId = 0)
        ttt = game.TTT()

    def after(logId):
        print("Cleaning up after unit test...")

        del state
        del ttt

class Tests:
    # When initating the state, game goard should be an array of 9 strings with a single space: " "
    def testEmptyBoard(self):
        expected = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

        state = game.State(logId = 0)
        ttt = game.TTT()

        if(state.board == expected):
            return 0
        
        return 1

    # When calling markBoard, state should update
    def testMarkBoard(self):
        expected = [X, " ", " ", " ", " ", " ", " ", " ", " "]

        state = game.State(logId = 0)
        ttt = game.TTT()

        ttt.markBoard(1, X, state)

        if(state.board == expected):
            return 0
        
        return 1

    # When calling markBoard on the same spot, state should update and the latest call should override the first since validate is a separate method
    def testMarkSameSpot(self):
        expected = [O, " ", " ", " ", " ", " ", " ", " ", " "]

        state = game.State()
        ttt = game.TTT()

        ttt.markBoard(1, X, state)
        ttt.markBoard(1, O, state)

        if(state.board == expected):
            return 0
        
        return 1

    # When calling markBoard on the same spot with validate, latest call should not override
    def testValidateMarkSameSpot(self):
        expected = [X, " ", " ", " ", " ", " ", " ", " ", " "]

        state = game.State(logId = 0)
        ttt = game.TTT()

        ttt.markBoard(1, X, state)
        if(ttt.validateMark(1, state)):
            ttt.markBoard(1, O, state)

        if(state.board == expected):
            return 0
        
        return 1

    # Test if checkGame does not end prematurely
    def testCheckGameNotFinished(self):
        expected = 1

        state = game.State()
        ttt = game.TTT()

        state.gamestate = ttt.checkGame(state)

        if(state.gamestate == expected):
            return 0
        
        return 1

    # Test if checkGame does not end prematurely
    def testCheckGameNotFinished(self):
        expected = 1

        state = game.State()
        ttt = game.TTT()

        state.gamestate = ttt.checkGame(state)

        if(state.gamestate == expected):
            return 0
        
        return 1

    # Test if checkGame finds a draw (checking both turns = max + gamestate = 1 and board is filled with Xs and Os)
    def testCheckGameDraw(self):
        expected = 4

        # Turns + gametate
        state1 = game.State(turn = 10, gamestate = 1)
        # Board is filled. Draw match:
        #  X | X | O
        # ---+---+---
        #  O | O | X
        # ---+---+---
        #  X | O | X
        state2 = game.State(board = [X, X, O, O, O, X, X, O, X])
        ttt = game.TTT()

        state1.gamestate = ttt.checkGame(state1)
        state2.gamestate = ttt.checkGame(state2)

        if(state1.gamestate == expected and state2.gamestate == expected):
            return 0
        
        return 1

    # Gamestate:
    # 0 = not initated
    # 1 = game active
    # 2 = X won
    # 3 = O won
    # 4 = draw

    # Test if checkGame finds X won
    def testCheckGameXWin(self):
        expected = 2

        #  X | X | X
        # ---+---+---
        #    |   |  
        # ---+---+---
        #    |   |  
        state = game.State(turn = 0, board = [X, X, X, " ", " ", " ", " ", " ", " "])
        ttt = game.TTT()

        state.gamestate = ttt.checkGame(state)

        if(state.gamestate == expected):
            return 0
        
        return 1

    # Test if checkGame finds O won
    def testCheckGameOWin(self):
        expected = 3

        #  O | O | O
        # ---+---+---
        #    |   |  
        # ---+---+---
        #    |   |  
        state = game.State(turn = 1, board = [O, O, O, " ", " ", " ", " ", " ", " "])

        # This would also work, and since checkGame checks on listindex and turn, not symbol, anything except a single space (" ") would work
        # state = game.State(turn = 1, board = [X, X, X, " ", " ", " ", " ", " ", " "])

        ttt = game.TTT()

        state.gamestate = ttt.checkGame(state)

        if(state.gamestate == expected):
            return 0
        
        return 1

    # Test if bot picks a valid spot (1 though 9)
    def testBotMarkAny(self):
        state = game.State(logId = 0)
        ttt = game.TTT()

        res = ttt.botMark(state)

        if(res > 0) and res < 10:
            return 0
        
        return 1

    # Test if bot picks the last spot when only one left
    def testBotMarkLastSpot(self):
        state = game.State(logId = 0, board = [X, X, X, X, X, X, X, X, " "])
        ttt = game.TTT()

        res = ttt.botMark(state)

        if(res == 9):
            return 0
        
        return 1

    # Test if bot can pick all spots
    def testBotMarkAll(self):
        expected = [O, O, O, O, O, O, O, O, O]
        board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

        state = game.State(logId = 0, board = board)
        ttt = game.TTT()

        i = 0
        while i < 9:
            res = ttt.botMark(state)
            state.board[res-1] = O
            i += 1

        if(state.board == expected):
            return 0
        
        return 1