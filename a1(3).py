# DO NOT modify or add any import statements
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
        row = coord_seq[row_str]
        col = coord_seq[col_str]
        if row < 0 or col < 0:
            return False
        if row >= game_size or col >= game_size:
            return False
    for  row_str in range(row_str, len(coordinate_sequence)):
        for col_str in range(col_str+1, len(coordinate_sequence)):
            if coordinate_sequence[row_str] == coordinate_sequence[col_str]:
                return False
    return True



def get_action(game_size: int) -> str:
    """Repeatedly prompts the player until they enter a valid coordinate
sequence, or a special command(h/help or q/quit).
Input is case-insensitive and returned in lowercase.
Invalid inputs print INVALID_MESSAGE from support.py"""
    while True:
        user_input = input(COMMAND_PROMPT).strip().lower()

        if user_input == 'h' or user_input == 'help':
            return HELP_COMMAND
        if user_input == 'q' or user_input == 'quit':
            return QUIT_COMMAND
       
        coords = parse_selection(user_input)
        if coords is not None and check_game_bounds(coords, game_size):
            return user_input
        
        print(INVALID_MESSAGE)
          

def generate_visible_state(game_size: int) -> tuple[tuple[str]]:
    """Generate the initial visible board state, filled with HIDDEN ('X')."""
    return tuple(
        tuple('X' for _ in range(game_size))
        for _ in range(game_size)
        )
    

def is_match(flipped: list[tuple[int, int]],
             hidden: tuple[tuple[str]]) -> str | None:
    """Check if all flipped cards have the same value.
Return the value if they match, otherwise None."""
    if len(flipped) != 2:
        return None
    (r1, c1), (r2, c2) = flipped
    if hidden[r1][c1] == hidden[r2][c2]:
        return hidden[r1][c1]
    return None
    

def peek(board: tuple[tuple[str]], hidden: tuple[tuple[str]],
         flipped: list[tuple[int, int]]) -> tuple[tuple[str]]:
    """Return a new board state with tthe specified coordinates
flipped face-up."""
    board_list = [list(row) for row in board]
    for (row, col) in flipped:
        board_list[row][col] = hidden[row][col]
    return tuple(tuple(row) for row in board_list)


def display_board(board: tuple[tuple[str]]) -> None:
    """Print the board in the required format
(including row/column numbers and separagtors)."""
    size = len(board)
    print(" " + " ".join(str(i+1) for i in range(size)) + " ")
    print(" " + "+-+" * size + "+")
    for i in range(size):
        print(f"{i+1}|" + "|".join(board[i]) + "|")
        print(" " + "+-+" * size)
 #""       
        
def play_game() -> None:
    """Play a single game of Memory Mash from start to finish"""
    print(WELCOME_MESSAGE)
    game_size = get_game_size()
    hidden = generate_hidden_state(game_size)
    visible = generate_visible_state(game_size)
    score = 0

    while True:
        all_revealed = all(cell != HIDDEN for row in visible for cell in row)
        if all_revealed:
            print(WIN_MESSAGE)
            print(f"You won in {score} moves!")
            break

        display_board(visible)
        action = get_action(game_size)

        if action == QUIT_COMMAND:
            print(f"Game quit! Your score: {score}")
            return

        selection = parse_selection(action)
        peeked = peek(visible, hidden, selection)
        display_board(peeked)
        score += 1

        match_value = is_match(selection, hidden)
        if match_value is not None:
            visible = peeked
            print (f"Match found! Card value: {match_value}")
        else:
            print("No match! Cards flipped back.")
    

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
