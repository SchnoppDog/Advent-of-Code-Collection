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

def repeated_characters(txt:str) -> bool:
    """Check if a string contains repeated characters.

    Args:
        txt (str): The string / text to check.

    Returns:
        bool: True if string contains repeated characters, otherwise False.
    """
    # Set() is using unique characters and deletes duplicates
    if len(set(txt)) == len(txt):
        return False
    else:
        return True

def get_start_of_message(puzzle_input:list|str, search_packet_range:int=4) -> int:
    """Checks the devices character character-stream for a message.

    Args:
        puzzle_input (list | str): The character-stream in which the message should be searched.
        search_packet_range (int, optional): The range in which the start-of-message marker should be searched. Defaults to 4.

    Returns:
        int: The position at which the message will start after.
    """
    packet_counter = 0
    message_start = 0
    search_packets_range = search_packet_range

    for message in puzzle_input:
        for _ in message:
            # Moving like frame-window (mtu) from char to char
            search_packets = message[packet_counter:search_packets_range+packet_counter]

            if repeated_characters(search_packets) == False:
                # Not using index() since index() only returns the first occurence of the char
                message_start = (packet_counter + search_packets_range)
                break
            else:
                packet_counter += 1
                continue

    return message_start

puzzle_input = "tasks/task1.txt"
puzzle_input = format_puzzle_input(puzzle_input)
packet_start = get_start_of_message(puzzle_input)

print(f"The message start after packert number: {packet_start}")