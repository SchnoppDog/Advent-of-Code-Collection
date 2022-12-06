def format_puzzle_input(puzzle_input:str, return_type:str="list") -> list | tuple | set:
    """Returns the puzzle output as given format.

    Args:
        puzzle_input (str): Absolute or relative path plus filename.
        return_type (str, optional): The type the puzzle is returned. Can be 'list', 'tuple' or 'set'. Defaults to "list".

    Returns:
        list | tuple | set: Returns the puzzle-input in selected format
    """
    with open(puzzle_input, "r") as puzzle:
        puzzle_output = puzzle.read()
    
    puzzle_output = puzzle_output.splitlines()

    match return_type:
        case "tuple":
            return tuple(puzzle_output)
        case "set":
            return set(puzzle_output)
        case _:
            return puzzle_output

def cratemover(puzzle_input:list, crates:list, crate_mover_model:str="9000") -> str:
    """Moves the crates according to the crate_mover_model

    Args:
        puzzle_input (list): The puzzle input as a list.
        crates (list): The crates as a 2d list.
        crate_mover (str, optional): The crate mover model. 9000 => part1; 9001 => part2. Defaults to "9000".

    Returns:
        str: The top crates.
    """
    # Getting only the move commands
    puzzle_input = puzzle_input[puzzle_input.index("")+1:]

    for command in puzzle_input:
        # Splitting to get each command-number
        command = command.split(" ")
        crates_to_move = int(command[1]) * -1
        from_crate_column = int(command[3]) - 1
        to_crate_column = int(command[5]) - 1
        
        # Part1
        if crate_mover_model == "9000":
            tmp_from_crate_column = crates[from_crate_column][crates_to_move:]
            # Reverse == step by step
            tmp_from_crate_column.reverse()
            crates[to_crate_column].extend(tmp_from_crate_column)
        # Part2
        else:
            crates[to_crate_column].extend(crates[from_crate_column][crates_to_move:])
        del crates[from_crate_column][crates_to_move:]

    top_crates = list()
    # Getting only the top crates
    for crate_column in crates:
        top_crates.append(crate_column[-1])

    top_crates = "".join(top_crates)

    return top_crates

example_crates = [
    ['Z', 'N'],
    ['M', 'C', 'D'],
    ['P']
]

task_crates = [
    ['F', 'H', 'B', 'V', 'R', 'Q', 'D', 'P'],
    ['L', 'D', 'Z', 'Q', 'W', 'V'],
    ['H', 'L', 'Z', 'Q', 'G', 'R', 'P', 'C'],
    ['R', 'D', 'H', 'F', 'J', 'V', 'B'],
    ['Z', 'W', 'L', 'C'],
    ['J', 'R', 'P', 'N', 'T', 'G', 'V', 'M'],
    ['J', 'R', 'L', 'V', 'M', 'B', 'S'],
    ['D', 'P', 'J'],
    ['D', 'C', 'N', 'W', 'V']
]

test_puzzle_input = "examples/example1.txt"
test_puzzle_input = format_puzzle_input(test_puzzle_input)
puzzle_input = "tasks/task1.txt"
puzzle_input = format_puzzle_input(puzzle_input)
top_crates = cratemover(puzzle_input, task_crates, crate_mover_model="9001")

print(f"The top row of crates are: {top_crates}")