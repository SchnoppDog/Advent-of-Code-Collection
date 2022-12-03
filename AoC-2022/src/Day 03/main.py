import string

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

def get_char_priority(char:str) -> int:
    """Get the priority of a char.

    Args:
        char (str): Single character in english alphabet.

    Returns:
        int: Priority of the char.
    """
    # Using the "string" module and "ascii_letters" returns a full string of uppder- and lowercase chars
    alphabet = list(string.ascii_letters)
    # Indexing begins at 0
    priority = alphabet.index(char) + 1
    return priority

def item_priority_calculator(puzzle_input:list|tuple) -> int:
    """Get the total item priority for each rucksack.

    Args:
        puzzle_input (list | tuple): The puzzle input as simple list or tuple.

    Returns:
        int: Returns the total item priority for each rucksack.
    """
    priorities = list()

    for rucksack in puzzle_input:
        rucksack_half = int(len(rucksack) / 2)
        # Get each rucksacks compartment
        compartment_one = rucksack[:rucksack_half]
        compartment_two = rucksack[rucksack_half:]

        # Break needs to be set otherwise chars are duplicated
        # Without "break" may result in a wrong total number
        for char in compartment_one:
            if char in compartment_two:
                char_priority = get_char_priority(char)
                priorities.append(char_priority)
                break

    return sum(priorities)

def group_priority_calculator(puzzle_input:list|tuple) -> int:
    """Returns the total group priority with a group of 3 elves.

    Args:
        puzzle_input (list | tuple): The puzzle input as simple list or tuple.

    Returns:
        int: Returns the total item priority for each group.
    """
    group_priorities = list()

    for group_number, rucksack in enumerate(puzzle_input):
        # First three elves are in a group so modulo works for this
        if group_number % 3 == 0:
            for char in rucksack:
                # Using "+1" and "+2" for the other two elves in the group respectively
                if char in puzzle_input[group_number+1]:
                    if char in puzzle_input[group_number+2]:
                        char_priority = get_char_priority(char)
                        group_priorities.append(char_priority)
                        # Break needs to be set otherwise chars are duplicated
                        # Without "break" may result in a wrong total number
                        break

    return sum(group_priorities)

# puzzle_input = "examples/example1.txt"
puzzle_input = "tasks/task1.txt"
puzzle_input = format_puzzle_input(puzzle_input)
# total_item_priority = item_priority_calculator(puzzle_input)
total_group_priority = group_priority_calculator(puzzle_input)

# print(f"Total Item Priority: {total_item_priority}")
print(f"Total Group Priority: {total_group_priority}")