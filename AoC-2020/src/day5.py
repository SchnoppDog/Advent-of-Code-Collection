def task1():
    highestSeatId   = 0
    seatId          = []
    lines           = []
    fbValues        = []
    rlValues        = []

    with open("files_for_days/day5.txt", "r") as file:
        for line in file:
            lineLetter = line[7]        # Is either R or L
            line = line.replace("\n", "")
            line = line.split(line[7], 1)       # Splitting on position 7
            line[1] = lineLetter + line[1]      # Adding Position 7 to the front since it has been split
            lines.append(line)      # Returns: [["FBFBBFF", "RLR"], ["BFFFBBF", "RRR"], ...]

    for lineList in lines:
        upperHalfFB = 128
        upperHalfRL = 8
        lowerHalfFB = 0
        lowerHalfRL = 0
        lenFbList   = len(lineList[0]) - 1
        lenRlList   = len(lineList[1]) - 1

        for fbLetter in lineList[0]:
            if fbLetter == "F":
                upperHalfFB = ((upperHalfFB - lowerHalfFB) / 2) + lowerHalfFB
                # i.e: 1. 128 = ((128 - 0) / 2) + 0 = 64
                # i.e: 3. 64 = ((64 - 32) / 2) + 32 = 48
                # ...

            elif fbLetter == "B":
                lowerHalfFB = ((upperHalfFB - lowerHalfFB) / 2) + lowerHalfFB
                # i.e: 2. 0 = ((64 - 0) / 2) + 0 = 32
                # i.e: 4. 32 = ((48 - 32) / 2) + 32 = 40
                # ...

        if lineList[0][lenFbList] == "F":
            upperHalfBinaryFB = upperHalfFB - 1     # Binary Expression: 0-7 (8), 0-15 (16), 0-31 (32) etc.
            fbValues.append(upperHalfBinaryFB)

        elif lineList[0][lenFbList] == "B":
            fbValues.append(lowerHalfFB)

        # Same procedure like F and B
        for rlLetter in lineList[1]:
            if rlLetter == "R":
                lowerHalfRL = ((upperHalfRL - lowerHalfRL) / 2) + lowerHalfRL

            elif rlLetter == "L":
                upperHalfRL = ((upperHalfRL - lowerHalfRL) / 2) + lowerHalfRL
        
        if lineList[1][lenRlList] == "R":
            rlValues.append(lowerHalfRL)

        elif lineList[1][lenRlList] == "L":
            upperHalfBinaryRL = upperHalfRL - 1
            rlValues.append(upperHalfBinaryRL)
    
    for counter in range(len(fbValues)):
        seatId.append(fbValues[counter] * 8 + rlValues[counter])
    
    for seatIds in seatId:
        if highestSeatId < seatIds:
            highestSeatId = seatIds

        else:
            highestSeatId = highestSeatId
        
        print("Seat-IDs: ", seatIds)

    print("Highest Seat-ID is: ", highestSeatId)
    # print(fbValues)
    # print(rlValues)
    # print(seatId)
    # print(highestSeatId)


task1()

# Task 2 will be missing since I don't understand the task and what I should do...