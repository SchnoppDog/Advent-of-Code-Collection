def task1():
    binarylist  = []
    bitlist     = []
    zerolist    = []
    onelist     = []
    gamma       = "0b"
    epsilon     = "0b"
    powConsumpt = 0

    with open("task_1.txt", "r") as task:
        for line in task:
            for bit in line:
                if not bit == "\n":
                    bitlist.append(int(bit))
                else:
                    binarylist.append(bitlist)
                    bitlist = []


    for bitPos in range(len(binarylist[0])):
        for bits in binarylist:
            if bits[bitPos] == 0:
                zerolist.append(0)
            else:
                onelist.append(1)
        if len(zerolist) > len(onelist):
            gamma += "0"
            epsilon += "1"

        else:
            gamma += "1"
            epsilon += "0"
        
        zerolist = []
        onelist = []

    powConsumpt = int(gamma, 2) * int(epsilon, 2)

    print("### TASK 1 ###")
    print("Gamma-Value: ", int(gamma, 2))
    print("Epsilon-Value: ", int(epsilon, 2))
    print("--------------------------")
    print("Power-Consumption: ", powConsumpt)

def task2():
    origNumBinList  = []
    numBitlist      = []
    numBinlist      = []
    zerolist        = []
    onelist         = []
    oxygenrateList  = []
    coScrubrateList = []
    oxygenrate      = "0b"
    coScrubrate     = "0b"
    powConsumpt     = 0

    with open("task_2.txt", "r") as task:
        for line in task:
            for bit in line:
                if not bit == "\n":
                    numBitlist.append(int(bit))
                else:
                    numBinlist.append(numBitlist)
                    numBitlist = []
        origNumBinList = numBinlist

        # For loop for oxygen generator rate
        for bitPos in range(len(numBinlist[0])):
            for bits in numBinlist:
                if len(numBinlist) == 1:
                    break
                if bits[bitPos] == 0:
                    zerolist.append(0)
                else:
                    onelist.append(1)
            if len(zerolist) > len(onelist):
                oxygenrateList.append(0)
            else:
                oxygenrateList.append(1)
            oldNumBinlist = numBinlist
            bitPos = len(oxygenrateList) - 1
            numBinlist = []
            for bits in oldNumBinlist:
                if len(oldNumBinlist) == 1:
                    break
                if bits[bitPos] == oxygenrateList[bitPos]:
                    numBinlist.append(bits)
            zerolist = []
            onelist = []

        # For-loop for co2 scrubber rating
        numBinlist = origNumBinList
        oldNumBinlist = []
        zerolist = []
        onelist = []
        for bitPos in range(len(numBinlist[0])):
            for bits in numBinlist:
                if len(numBinlist) == 1:
                    break
                if bits[bitPos] == 0:
                    zerolist.append(0)
                else:
                    onelist.append(1)
            if len(numBinlist) > 1:
                if len(zerolist) > len(onelist):
                    coScrubrateList.append(1)
                else:
                    coScrubrateList.append(0)
            else:
                coScrubrateList = numBinlist[0]
            oldNumBinlist = numBinlist
            bitPos = len(coScrubrateList) - 1
            numBinlist = []
            for bits in oldNumBinlist:
                if bits[bitPos] == coScrubrateList[bitPos]:
                    numBinlist.append(bits)
            zerolist = []
            onelist = []

        for bit in oxygenrateList:
            oxygenrate += str(bit)

        for bit in coScrubrateList:
            coScrubrate += str(bit)

        powConsumpt = int(oxygenrate, 2) * int(coScrubrate, 2)
        print("\n### TASK 2 ###")
        print("Oxygen Generator Rating: ", int(oxygenrate, 2))
        print("CO2 Scrubber Rating: ", int(coScrubrate, 2))
        print("---------------------------")
        print("Power Consumption: ", powConsumpt)
            

task1()
task2()