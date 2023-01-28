def task1And2():
    groups          = []
    nestedGroups    = []
    lines           = []
    groupYesCounts  = []
    countaddGroups  = 0
    yesSum          = 0

    with open("files_for_days/day6.txt", "r") as file:
        for line in file:
            line = line.rstrip()    # Stripping \r\n each line
            lines.append(line)      # Return Array with all groups plus empty line. Example: ["abc", "", "a", "b", "c", "", ...]

    for string in lines:
        # If line is empty, add the nested group
        if string == "":
            groups.append(nestedGroups)     # Returns: [["abc"], ["a", "b", "c"], ...]
            nestedGroups = []
            countaddGroups += 1
            continue
        # Creating each group unitl empty line
        else:
            nestedGroups.append(string)
            # Appending the last group
            if countaddGroups == len(lines) - 1:
                groups.append(nestedGroups)

        countaddGroups += 1

    # Tasks for every group
    for group in groups:
        # Task 1:
        groupAnswers    = group[0]
        # Task 2:
        groupLen        = len(group)
        letterDict      = {}
        answerString    = ""

        if len(group) == 1:
            # Task 1 and 2:
            groupYesCounts.append(len(group[0]))    # If a group has only 1 member, each answer is accepted as "yes"
            continue

        for answer in group:
            for letter in answer:
                # Task 1:
                # if letter not in groupAnswers:
                #     groupAnswers = groupAnswers + letter
                # Task 2:
                if letter in letterDict.keys():
                    letterDict[letter] = letterDict[letter] + 1         # E.g: letterDict = { "a": 1, "b": 1, "c": 1} -> "a" in dict = letterDict = { 
                                                                        # "a": 2, "b": 1, "c": 1}
                else:
                    letterDict[letter] = 1

        # Task 1:
        # groupYesCounts.append(len(groupAnswers))
        # Task 2:
        for letter in letterDict.keys():
            if letterDict[letter] == groupLen:          # All correct letters have to be the equal to the length of the group (members)
                answerString = answerString + letter

        groupYesCounts.append(len(answerString))

    for yesCounts in groupYesCounts:
        yesSum += yesCounts

    print("Sum of Yes-Answers: ", yesSum)


task1And2()