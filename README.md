# python-tic-tac-toe

A simple python Tic Tac Toe in the terminal.
Singleplayer against random pick bot or 2 players.

## Usage (Windows)
1. [Install Python](https://www.python.org/downloads/)
2. Make sure Python is defined on PATH
3. Navigate to folder in CLI
4. $python main.py [flag value, ...]

Flags:
- -help, -h: prints all help available and quit, default off
- -tests, -t: run tests and quit, default off
- -players, -p + [players]: number of players, 1 or 2, default 1
    - Example:
        - Start with two players: $ python main.py -p 2 
- -logId, -l + [id]: log id, higher id means more information is printed, 0, 1, or 2, default 1
    - Example:
        - Run with the least ammount of information: $ python main.py -l 0 

### My Thoughts

From getting started with Python in the weather project, I wanted to get to learn more of the internal logic by recreating a Tic Tac Toe game. Overall works, well, might be a good place to test homemade AI in the future...