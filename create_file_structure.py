import os
from datetime import date

def create_file_structure(abspath:str, dirname:str, src_dirname:str):
    """Creates my file structure for advent of code

    Args:
        abspath (str): Absolute path where the new AoC directory should be created.
        dirname (str): The name of the AoC root directory.
        src_dirname (str): The name where to create the day-dirs and files.
    """

    # Join path for easier use
    root_dir = os.path.join(abspath, dirname)
    src_dir = os.path.join(root_dir, src_dirname)

    # Replacing Backslashes for compatibility
    root_dir = root_dir.replace("\\", "/")
    src_dir = src_dir.replace("\\", "/")

    os.mkdir(root_dir)
    open(f"{root_dir}/Readme.md", "w").close()
    os.mkdir(src_dir)

    for day_number in range(1, 26):
        if day_number < 10:
            day = f"Day 0{day_number}"
        else:
            day = f"Day {day_number}"

        os.makedirs(f"{src_dir}/{day}/examples")
        os.makedirs(f"{src_dir}/{day}/tasks")
        open(f"{src_dir}/{day}/examples/example1.txt", "w").close()
        open(f"{src_dir}/{day}/examples/example2.txt", "w").close()
        open(f"{src_dir}/{day}/tasks/task1.txt", "w").close()
        open(f"{src_dir}/{day}/tasks/task2.txt", "w").close()
        open(f"{src_dir}/{day}/main.py", "w").close()
        open(f"{src_dir}/{day}/test.py", "w").close()
        open(f"{src_dir}/{day}/Task.md", "w").close()

absolute_path = os.path.dirname(os.path.realpath(__file__))
root_dir_name = "AoC-" + str(date.today().year)
source_dirname = "src"

create_file_structure(absolute_path, root_dir_name, source_dirname)