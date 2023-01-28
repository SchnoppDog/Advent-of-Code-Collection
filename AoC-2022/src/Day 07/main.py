# Changed function after conversation on day 04.
def format_puzzle_input(puzzle_input:str, type=list):
    """Return the puzzle-input given format.

    Args:
        puzzle_input (str): The absolute or relative path to the puzzle-input file.
        type (any): The type you want to convert your puzzle input to. Defaults to list.

    Returns:
        any: Puzzle-input in given format. May not work with number-types like int or float.
    """
    with open(puzzle_input, "r") as puzzle:
        puzzle_output = puzzle.read()
    
    puzzle_output = puzzle_output.splitlines()

    return type(puzzle_input)