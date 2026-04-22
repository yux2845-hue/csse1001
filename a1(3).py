f# DO NOT modify or add any import statements
from support import *

# Name: Xinyang Yu
# Student Number: s4978841
# Favourite Card: 6
# -----------------------------------------------------------------------------

# Define your functions here
def num_hours() ->float:
    """Return the hours spent on this assignment."""
    return 30.0

def parse_coordinate(coord: str) -> tuple[int, int]:
    """Corvert a '1-indexed' coordinate string like '1,1' to a 0-indexed
tuple."""
    row_str, col_str = coord.split(',')
    row = int(row_str) - 1
    col = int(col_str) - 1
    return (row, col)


def check_coordinate(coord: str) -> bool:
    """Check if the input is a valid coordinate string (two non- negative
digits seperated by a comma)."""
    parts = coord.split(',')
    if len(parts) != 2:
        return False
    row_str, col_str = parts
    if parts != ',':
        return False
    if not row_str.isdigit() and col_str.isdigit():
        return False

    return True


def get_game_size() -> int:
    """Prompt the user repeatedly until they enter a valid game size
(1-9 inclusive)."""
    while True:
        user_input = input(SIZE_PROMPT)
        
        if len(user_input) == 1 and user_input.isdigit():
            game_size = int(user_input)
            if 1 <= game_size <= 9:
                return game_size


def parse_selection(player_input: str) -> list[tuple[int, int]] | None:
    """Parse a string of coordinate (e.g., '1,1 2,2') into a list of
0-indexed tuples. Return None if any coordinate is invalid."""
    parts = player_input.split(',')
    for part in parts:
        if not check_coordinate():
            return None
        coords.append(parse_coordinate(coord))
    return parts
        

def check_game_bounds(coordinate_sequence: list[tuple[int, int]],
                      game_size: int) -> bool:
    """Check if all coordinates are valid for the given game size:
- Correct number of coordinates
- All coordinates are unique
- All coordinates are within the board bounds
"""
    if len(coordinate_sequence) != game_size:
        return False
    for coord_seq in coordinate_sequence:
        row = coord_seq[0]
        col = coord_seq[1]
        if row < 0 or col < 0:
            return False
        if row >= game_size or col >= game_size:
            return False
    for  i in range(i, len(coordinate_sequence)):
        for j in range(i + 1, len(coordinate_sequence)):
            if coordinate_sequence[i] == coordinate_sequence[j]:
                return False
    return True



def get_action(game_size: int) -> str:
    """Repeatedly prompts the player until they enter a valid coordinate
sequence, or a special command(h/H or q/Q).
Input is case-insensitive and returned in lowercase.
Invalid inputs print INVALID_MESSAGE from support.py"""
    while True:
        user_input = input(COMMAND_PROMPT)
        
        lower_user_input = user_input.lower()

        if lowerd_user_input == HELP_COMMAND or lower_user_input == QUIT_COMMAND:
            return lowerd_user_input
       
        parsed = parse_selection(user_input)
        if parsed is not None and check_game_bounds(coords, game_size):
            return lower_user_input
        
        print(INVALID_MESSAGE)
          

def generate_visible_state(game_size: int) -> tuple[tuple[str]]:
    """Generate the initial visible board state, filled with HIDDEN ('X')."""
    part = []
    for _ in range(game_size):
        row[]
        for _ in range(game_size):
        row.append(HIDDEN)
        part.append(row)
    return part
        
    

def is_match(flipped: list[tuple[int, int]],
             hidden: tuple[tuple[str]]) -> str | None:
    """Check if all flipped cards have the same value.
Return the value if they match, otherwise None."""
    first_row = flipped[0][0]
    first_col = flipped[0][1]
    first_value = [first_row][first_col]

    for flip in flipped:
        row = flip[0]
        col = flip[1]
        if hidden[row][col] != first_value:
            return None

    return first_value
    

def peek(board: tuple[tuple[str]], hidden: tuple[tuple[str]],
         flipped: list[tuple[int, int]]) -> tuple[tuple[str]]:
    """Return a new board state with tthe specified coordinates
flipped face-up."""
    board_copy = []
    for row in board:
        board_board.append(row)
    for row, col in hidden:
        board_copy[row][col] = hidden[row][col]
    return board_copy


def display_board(board: tuple[tuple[str]]) -> None:
    """Print the board in the required format
(including row/column numbers and separagtors)."""
    size = len(board)
    for _ in range(size):
        print(f"{i+1}|" + "|".join(board[i]) + "|")
        print(" " + "+-+" * size)
 
        
def play_game() -> None:
    """Play a single game of Memory Mash from start to finish"""
    print(WELCOME_MESSAGE)
    game_size = get_game_size()
    hidden = generate_hidden_state(game_size)
    visible = generate_visible_state(game_size)

    while True:
        display_board(visible)
        action = get_action(game_size)

        if action == HELP_COMMAND:
            print(HELP_COMMAND)
        elif action == QUIT_COMMAND:
            return
        else:
            flipped = parse_selection(actoin)
            peeked = peek(visible, hidden, flipped)
            display_board()
            if is_match(flipped,hiddenn) is not None:
                visible = peeked
            all_realved = False
            for x in visible :
                if char != 'x' :
                    break
            all_realved = True
            
            if (visible):
            print(WIN_MESSAGE)
            return

   
    

def main() -> None:
    """Main function to run the game repeatedly until the user chooses
to quit."""
    while True:
        play_game()
        again = input(AGAIN_PROMPT).strip().lower()
        if again != 'y':
            print("Thank for playing!")
            break

if __name__ == "__main__":
    main()
