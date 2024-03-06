from random import randint

scores = {"computer": 0, "player": 0}


class Board:
    """
    Main board class. Sets board size,
    the number of ships, the player's name
    and the board type(player board or computer board)
    Has methods for adding ships and guesses and printing the board
    """

    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []

    def print_board(self):
        """
        Prints the current state of the board.
        Each cell of the board is represented by a character.
        '_' indicates an empty cell.
        'X' indicates a cell containing a ship.
        '*' indicates a cell that has been guessed.
        """
        for row in self.board:
            print("  ".join(row))

    def guess(self, x, y):
        """
        Records a guess on the board and returns the result.
        x: int, x-coordinate of the guess
        y: int, y-coordinate of the guess
        Returns:
        str: "Hit" if the guess hits a ship, "Miss" otherwise.
        """
        self.guesses.append((x, y))
        self.board[x][y] = "x"

        if (x, y) in self.ships:
            self.board[x][y] = "*"
            return "Hit"
        else:
            return "Miss"

    def add_ship(self, x, y, type="computer"):
        """
        adds a ship to the board at the specified coordinates
        if the number of ships on the board has reached the maximum limit.
        an error message if printed indicating the no more ships can be added.
        otherwise, the ship is added to the board at the specified coordinates,
        and if the board type is "player"
        the corresponding cell on the player's
        board is marked with "@" to represent the ship
        """
        if len(self.ships) >= self.num_ships:
            print("Error: You cannot add anymore ships")
        else:
            self.ships.append((x, y))
            if self.type == "player":
                self.board[x][y] = "@"


def random_point(size):
    """
    Helper function to return a random integer,
    between  0 and size.
    """
    return randint(0, size - 1)


def valid_coordinates(x, y, board):
    """
    Check if the coordinates (x, y) are valid for the given board.
    if the coordinate is valid return true, false otherwise
    """
    if 0 <= x < board.size and 0 <= y < board.size:
        if (x, y) not in board.guesses:
            return True

    return False


def populate_board(board):
    """
    populate  board with the ships in random positions.
    """
    for _ in range(board.num_ships):
        while True:
            x = random_point(board.size)
            y = random_point(board.size)
            if valid_coordinates(x, y, board):
                board.add_ship(x, y)
                break


def make_guess(board):
    """
    Prompt the player to make a guess and return the result.
    while true the player enter row number between 0 to 4,
    and column number between 0 to 4
    if not between 0 to 4 print message "values must be between 0 and 4!
    please try again"
    and if the number guessed before ,
    print message "You've already guessed those coordinates.
    please try again "
    otherwise return the players guessed number and result
    """
    while True:
        x = int(input("Enter row number (0-4):\n"))
        y = int(input("Enter column number (0-4)\n"))

        if not (0 <= x < board.size and 0 <= y < board.size):
            print("Values must be between 0 and 4!.Please try again.")
        elif (x, y) in board.guesses:
            print("You've already guessed those coordinates.Please try again.")
        else:
            result = board.guess(x, y)
            return x, y, result


def play_game(computer_board, player_board):
    """
    Play the battleship game.
    Print the player's board and computer's board
    call function makes guess (computer_board)
    to get the result
    """
    while True:
        # Player's turn
        print("Your board:")
        player_board.print_board()
        print("computer's board:")
        computer_board.print_board()

        print("Your turn:")
        x, y, result = make_guess(computer_board)
        if result == "Hit":
            print("Player guessed:", (x, y))
            print("Player hit this time.")
            scores['player'] += 1
        else:
            print("Player Guessed:" (x, y))
            print("Player missed this time.")

        if all((x, y) in computer_board.ships
               for x in range(computer_board.size)
               for y in range(computer_board.size)):
            print("Congratulations! You've sunk all the computer's ships.")
            print("You Win!")
            break