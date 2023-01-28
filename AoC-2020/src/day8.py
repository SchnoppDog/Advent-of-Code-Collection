def task1():
    tasks           = []
    idCounter       = 0
    taskslen        = 0
    taskCounter     = 0
    acc             = 0
    loopCounter     = {}
    changeOperation = True
    oldOperation    = ""
    oldOperationId  = None
    testedOps       = []

    with open("files_for_days/day8.txt", "r") as file:
        for line in file:
            line = line.rstrip()
            line = line.split()
            line.append(idCounter)
            tasks.append(line)
            idCounter += 1
    
    taskslen        = len(tasks)
    while True:
        operation       = tasks[taskCounter][0]
        operationValue  = int(tasks[taskCounter][1])
        operationId     = tasks[taskCounter][2]

        # print("#### First Initializiation ####")
        # print("Operaion: ", operation)
        # print("Operation-Value: ", operationValue)
        # print("Operaiont-ID: ", operationId)
        # print("\n")

        # if taskCounter == taskslen:
        #     taskCounter = 0

        if operationId == taskslen - 1:
            if operation == "acc":
                acc = acc + int(operationValue)
                print("Acc-Value without Loop: ", acc)
                break
            
            else:
                print("Acc-Value without Loop: ", acc)
                break

        if changeOperation == True:
            if operation == "jmp":
                for task in tasks:
                    if task[2] == oldOperationId:
                        task[0] = oldOperation

                if operationId in testedOps:
                    taskCounter += 1
                    continue

                print(f"Change Opration {operation} with ID {operationId} to Operation: 'nop'\n")
                oldOperation            = tasks[taskCounter][0]
                oldOperationId          = operationId
                tasks[taskCounter][0]   = "nop"
                changeOperation         = False
                taskCounter             = 0
                acc                     = 0
                loopCounter             = {}
                testedOps.append(operationId)
                continue

            elif operation == "nop":
                for task in tasks:
                    if task[2] == oldOperationId:
                        task[0] = oldOperation

                if operationId in testedOps:
                    taskCounter += 1
                    continue

                print(f"Change Opration {operation} with ID {operationId} to Operation: 'jmp'\n")
                oldOperation            = tasks[taskCounter][0]
                oldOperationId          = operationId
                tasks[taskCounter][0]   = "jmp"
                changeOperation         = False
                taskCounter             = 0
                acc                     = 0
                loopCounter             = {}
                testedOps.append(operationId)
                continue

        if operationId in loopCounter.keys():
            if loopCounter[operationId] == 2:
                # print("Acc-Value before loop: ", acc)
                changeOperation = True
                # break

        # if tasks[taskCounter][2] == 0:
        #     loopCounter += 1

        #     if loopCounter == 2:
        #         print("Acc-Value before loop: ", acc)
        #         break

        if operation == "acc":
            if operationId not in loopCounter.keys():
                loopCounter[operationId] = 1

            else:
                loopCounter[operationId] = loopCounter[operationId] + 1

                if loopCounter[operationId] == 2:
                    # print("Acc-Value before loop: ", acc)
                    changeOperation = True
                    # break
            
            acc = acc + int(operationValue)
            taskCounter += 1
        
        if operation == "jmp":
            if operationId not in loopCounter.keys():
                loopCounter[operationId] = 1

            else:
                loopCounter[operationId] = loopCounter[operationId] + 1

                if loopCounter[operationId] == 2:
                    # print("Acc-Value before loop: ", acc)
                    changeOperation = True
                    # break
            
            taskCounter = taskCounter + int(operationValue)
            

        if operation == "nop":
            if operationId not in loopCounter.keys():
                loopCounter[operationId] = 1

            else:
                loopCounter[operationId] = loopCounter[operationId] + 1

                if loopCounter[operationId] == 2:
                    # print("Acc-Value before loop: ", acc)
                    changeOperation = True
                    # break
            
            taskCounter += 1

task1()