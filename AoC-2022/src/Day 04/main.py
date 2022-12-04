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

def range_overlap(range_one:list|tuple, range_two:list|tuple, check_any_overlap:bool=False) -> bool:
    """Check if a number-range is fully or partially overlapping another one.

    Args:
        range_one (list | tuple): Range to check against i.e. [1, 4].
        range_two (list | tuple): Range to be checked i.e. [1, 3].
        check_any_overlap (bool, optional): Searching for partially overlapping numbers. Defaults to False.

    Returns:
        bool: True if any number is overlapping, False if not
    """
    if not check_any_overlap:
        if int(range_one[0]) <= int(range_two[0]):
            if int(range_one[1]) >= int(range_two[1]):
                return True
            else:
                return False
        else:
            return False
    else:
        # Using set().intersection to get any overlapping number
        overlapping_nums = set(range(int(range_one[0]), int(range_one[1])+1)).intersection(set(range(int(range_two[0]), int(range_two[1])+1)))
        
        if overlapping_nums:
            return True
        
        else:
            return False

def elf_section_overlap(puzzle_input:list|tuple, check_any_overlap:bool=False) -> int:
    """Checks if camp-sections of elve-pairs are overlapping.

    Args:
        puzzle_input (list | tuple): The puzzle input as simple list or tuple.
        check_any_overlap (bool, optional): Checks for partial overlapping numbers. Defaults to False.

    Returns:
        int: The total number of overlapping sections.
    """
    total_overlaps = 0

    for elve_pair in puzzle_input:
        # Optimizing by using it on one line
        # elf_one = [0], elf_two = [1] of elve_pair.split(",")
        elf_one, elf_two = elve_pair.split(",")
        # elf_one = elve_pair.split(",")[0]
        elf_one = elf_one.split("-")
        # elf_two = elve_pair.split(",")[1]
        elf_two = elf_two.split("-")

        if not check_any_overlap:
            if range_overlap(elf_one, elf_two):
                total_overlaps += 1
            
            elif range_overlap(elf_two, elf_one):
                total_overlaps += 1
            
            else:
                continue
        else:
            if range_overlap(elf_one, elf_two, True):
                total_overlaps += 1
            
            else:
                continue

    return total_overlaps

# puzzle_input = "examples/example1.txt"
puzzle_input = "tasks/task1.txt"

puzzle_input = format_puzzle_input(puzzle_input)
total_section_overlaps = elf_section_overlap(puzzle_input, True)

print(f"Total number of (fully) overlapping sections is: {total_section_overlaps}")