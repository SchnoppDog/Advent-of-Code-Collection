def puzzle_to_list(puzzle_input:str) -> list:
    """Returns the puzzle input as two dimensional array

    Args:
        puzzle_input (str): Puzzle-input as relative or absolute path and filename

    Returns:
        list: Returns a two dimensional list i.e [["A", "B"]]
    """
    puzzle_list = list()

    with open(puzzle_input, "r") as puzzle:
        for line in puzzle:
            line = line.strip()
            line = line.split(" ")
            puzzle_list.append(line)
    
    return puzzle_list

def get_rps_total_wins(puzzle_input:list, true_total_points=False) -> int:
    """Get your total points of the rock, paper, scissor contest

    Args:
        puzzle_input (list): Two dimensional list i.e. [[A, B]]
        true_total_points (bool, optional): Get the output the elf originally meant. Defaults to False.

    Returns:
        int: Total points of the rock, paper, scissor contest
    """
    lose_points = 0
    draw_points = 3
    win_points = 6
    total_points = 0
    for rps_match in puzzle_input:
        match rps_match[0]:
            case "A":
                if rps_match[1] == "X":
                    if not true_total_points:
                        total_points += draw_points + 1
                    else:
                        total_points += lose_points + 3
                elif rps_match[1] == "Y":
                    if not true_total_points:
                        total_points += win_points + 2
                    else:
                        total_points += draw_points + 1
                else:
                    if not true_total_points:
                        total_points += lose_points + 3
                    else:
                        total_points += win_points + 2
            case "B":
                if rps_match[1] == "X":
                    total_points += lose_points + 1
                elif rps_match[1] == "Y":
                    total_points += draw_points + 2
                else:
                    total_points += win_points + 3
            case "C":
                if rps_match[1] == "X":
                    if not true_total_points:
                        total_points += win_points + 1
                    else:
                        total_points += lose_points + 2
                elif rps_match[1] == "Y":
                    if not true_total_points:
                        total_points += lose_points + 2
                    else:
                        total_points += draw_points + 3
                else:
                    if not true_total_points:
                        total_points += draw_points + 3
                    else:
                        total_points += win_points + 1

    return total_points

# input_file = "examples/example1.txt"
input_file = "tasks/task1.txt"

puzzle_list = puzzle_to_list(input_file)
total_points = get_rps_total_wins(puzzle_list, true_total_points=True)

print(f"Total Points: {total_points}")