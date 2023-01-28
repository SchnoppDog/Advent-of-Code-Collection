def task1():
    with open("task_1.txt", "r") as ex:
        positions = [position.strip("\n") for position in ex]

    depth       = 0
    horizontal  = 0

    for position in positions:
        if "forward" in position:
            horizontal += int(position.split()[1])
        elif "down" in position:
            depth += int(position.split()[1])
        else:
            depth -= int(position.split()[1])

    print("### TASK 1 ###")
    print("Horizontal Position: ", horizontal)
    print("Depth is: ", depth)
    print("---------------")
    print("Final position is: ", depth * horizontal)

def task2():
    with open("task_2.txt", "r") as ex:
        positions = [position.strip("\n") for position in ex]

    depth = 0
    forward = 0
    aim = 0

    for pos in positions:
        if "forward" in pos:
            forward += int(pos.split()[1])
            depth = aim * int(pos.split()[1]) + depth
        elif "down" in pos:
            aim += int(pos.split()[1])
        else:
            aim -= int(pos.split()[1])

    print("### TASK 2 ###")
    print("Horizontal Position: ", forward)
    print("Aim is: ", aim)
    print("Depth is: ", depth)
    print("---------------")
    print("Final position is: ", depth * forward)

task1()
task2()