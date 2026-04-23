# DO NOT modify or add any import statements
from support import *

# Name: Xinyang Yu
# Student Number: s4978841
# Favourite Card: 6
# -----------------------------------------------------------------------------

# Define your functions here
def num_hours() -> float:
    """Return the hours spent on this assignment."""

    return float(30);


def parse_coordinate(coord: str) -> tuple[int, int]:
    """
    Corvert a '1-indexed' coordinate string like '1,1' to a 
    0-indexed tuple
    """

    parts = coord.split(",")
    row = int(parts[0]) - 1
    col = int(parts[1]) - 1

    return (row, col);


def check_coordinate(coord: str) -> bool:
    """
    Check if the input is a valid coordinate string (two non-negative
    digits seperated by a comma).

    """ 
    if len(coord) != 3:
        return False

    if coord[1] != ",":
        return False

    if not coord[0].isdigit():
        return False
    if not coord[2].isdigit():
        return False
    
    return True;


def get_game_size() -> int:
    """
    Prompt the user repeatedly until they enter a valid game size
    (1-9 inclusive).
    """
    while True:
        user_input = input(SIZE_PROMPT)

        if len(user_input) == 1 and user_input.isdigit():
            size = int(user_input)
            if 1 <= size <= 9:
                return size;


def parse_selection(player_input: str) -> list[tuple[int, int]] | None:
    """
    Parse a string of coordinate (e.g., '1,1 2,2') into a list of 0-indexed
    tuples. Return None if any coordinate is invalid.
    """

    coords = player_input.split(' ')

    result = []

    for coord in coords:
        if not check_coordinate(coord):
            return None
        result.append(parse_coordinate(coord))

    return result


def check_game_bounds(coordinate_sequence: list[tuple[int,int]],
                       game_size: int) -> bool:
    """
    Check if all coordinates are valid for the given game size:
    - Correct number of coordinates.
    - All coordinates are unique.
    - All coordinates are within the board bounds.
    """

    if len(coordinate_sequence) != game_size:
        return False
    
    for cord_seq in coordinate_sequence:

        row = cord_seq[0]
        col = cord_seq[1]

        if row < 0 or col < 0:
            return False
        
        if row >= game_size or col >= game_size:
            return False
        
    for i in range(len(coordinate_sequence)):
        for j in range(i + 1, len(coordinate_sequence)):
            if coordinate_sequence[i] == coordinate_sequence[j]:
                return False;

    return True;


def get_action(game_size: int) -> str:
    """
    Repeatedly prompts the player until they enter a valid coordinate
    sequence, or a special command(h/help or q/quit).
    Input is case-insensitive and returned in lowercase.
    Invalid inputs print INVALID_MESSAGE from suppoet.py
    """

    while True:

        user_input = input(COMMAND_PROMPT)
        lowerd_user_input = user_input.lower()

        if lowerd_user_input == HELP_COMMAND or lowerd_user_input == QUIT_COMMAND:
            return lowerd_user_input
         
        parsed = parse_selection(lowerd_user_input) 
        
        if parsed is not None and check_game_bounds(parsed, game_size):
            return lowerd_user_input
        
        print(INVALID_MESSAGE)


def generate_visible_state(game_size: int) -> tuple[tuple[str]]:
    """
    Generate the initial visible board state, filled with HIDDEN ('X').
    """

    res = []

    for _ in range(game_size):

        row = []

        for _ in range(game_size):
            row.append(HIDDEN)

        res.append(tuple(row))

    return tuple(res);


def is_match(flipped: list[tuple[int, int]], hidden: tuple[tuple[str]]) -> str | None:
    """
    Check if all flipped cards have same value. Return the value if they
    match, otherwise None.
    """
    first_row, first_col = flipped[0]
    first_value = hidden[first_row][first_col]

    for row, col in flipped:

        if hidden[row][col] != first_value:
            return None
    
    return first_value


def peek(board: tuple[tuple[str]], hidden: tuple[tuple[str]], flipped: list[tuple[int,int]]) -> tuple[tuple[str]]:
    """
    Return a new board state with the specified coordinates flipped face-up.
    """

    board_copy = []

    for row in board:
        board_copy.append(list(row))
    

    for row, col in flipped:
    
        board_copy[row][col] = hidden[row][col]

    new_board = []
    for row in board_copy:
        new_board.append(tuple(row))

    return tuple(new_board)


def display_board(board: tuple[tuple[str]]) -> None:
    """
    Print the board in the required format(including row/column numbers
    and separagtors).   
    """

    size = len(board)
    print(" ", end="")
    for col_num in range(1, size + 1):
        print(" " + f"{col_num}" + " ", end="")
    print()

    border = " " + "+-+" * size

    print(border)

    for row_num in range(size):
        print(row_num + 1, end="")
        for value in board[row_num]:
            print(f"|{value}|",end="")
        print()
        print(border)


def play_game() -> None:
    """
    Play a single game of Memory Mash from start to finish.   
    """
    print(WELCOME_MESSAGE)
    moves = 0

    game_size = get_game_size()
    hidden = generate_hidden_state(game_size)
    visible = generate_visible_state(game_size)

    while True:
        display_board(visible)
        action = get_action(game_size)

        if action == HELP_COMMAND:
            print(HELP_MESSAGE)
            continue

        if action == QUIT_COMMAND:
            return
        
        
        flipped = parse_selection(action)
        peeked = peek(visible, hidden, flipped)
        moves += 1
        display_board(peeked)

        
        if is_match(flipped, hidden) is not None:
            visible = peeked

        all_realved = True;

        for row in visible:
            for value in row:
                if value == HIDDEN:
                    all_realved = False
        
        if all_realved:
            print(f"{WIN_MESSAGE} It took you {moves} moves!")
            return


def main() -> None:
    """Main function to run the game repeatedly until the user chooses
to quit."""
    while True:
        play_game()
        again = input(AGAIN_PROMPT)

        if again.lower() != "y":
            break
        
if __name__ == "__main__":
    main()
