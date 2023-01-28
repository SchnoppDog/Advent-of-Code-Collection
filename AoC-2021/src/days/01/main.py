def task1():
    incrNumbers = 0
    decrNumbers = 0
    sonarSweeps = []

    with open("task_1.txt", "r") as task:
        for line in task:
            line = line.strip("\n")
            sonarSweeps.append(int(line))

    oldNum = 0
    for num in sonarSweeps:
        if oldNum != 0:
            if num > oldNum:
                incrNumbers += 1
            else:
                decrNumbers += 1
        oldNum = num

    print("### TASK 1 ###")
    print(f"Counted increased numbers: {incrNumbers}")
    print(f"Counted decreased numbers: {decrNumbers}")

def task2():
    incrNumbers = 0
    decrNumbers = 0
    evenNumbers = 0
    sonarSweeps = []
    sonarWindow = []

    with open("tast_2.txt", "r") as example:
        for line in example:
            line = line.strip("\n")
            sonarSweeps.append(int(line))

    for sweep in sonarSweeps:
        sonarWindow.append(sweep)
        if len(sonarWindow) % 4 == 0:
            firstWindow = sonarWindow[0] + sonarWindow[1] + sonarWindow[2]
            secondWindow = sonarWindow[1] + sonarWindow[2] + sonarWindow[3]

            if secondWindow > firstWindow:
                incrNumbers += 1
            elif secondWindow == firstWindow:
                evenNumbers += 1
            else:
                decrNumbers += 1
            sonarWindow.pop(0)

    print("\n### TASK 2 ###")
    print(f"Counted increased numbers: {incrNumbers}")
    print(f"Counted even numbers: {evenNumbers}")
    print(f"Counted decreased numbers: {decrNumbers}")

task1()
task2()