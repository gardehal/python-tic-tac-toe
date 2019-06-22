import random

class Tests:
    def __init__(self, logId):
        print("Running unit tests...")

        testX = self.testX()
        finalRes = testX # + testY + testZ...

        print("testX:               ", "Pass" if testX else "Failed")
        print("All test passed!" if (finalRes == 0) else "One or more tests failed.")

    def testX(self):
        return 0

    def testEmptyBoard(self):
        return 0
