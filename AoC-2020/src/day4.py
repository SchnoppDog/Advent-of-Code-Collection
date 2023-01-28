import re as re

def task1():
    lines = []
    with open("files_for_days/day4.txt", "r") as file:
        for line in file:
            line = line.replace("\n", "")
            lines.append(line.replace("\r", ""))        # Example-Output: ["ecl:gry pid:860033327 eyr:2020 hcl:#fffffd", 
                                                        # "byr:1937 iyr:2017 cid:147 hgt:183cm", ""]
    
    passports = []
    for line in lines:
        lineContents = line.split(" ")
        for lineContent in lineContents:
            passports.append(lineContent)       # Example-Output: ["ecl:gry", "pid:860033327", "eyr:2020", "hcl:#fffffd" ..., "", ...]
    
    passportObj         = {}
    passportCounter     = 1
    passportObj[f"passport_{passportCounter}"] = {}
    for passportEntry in passports:
        if len(passportEntry) == 0:
            passportCounter += 1
            passportObj[f"passport_{passportCounter}"] = {}
            continue

        if passportEntry.split(":")[0] == "cid":
            continue
        
        entryId     = passportEntry.split(":")[0]
        entryValue  = passportEntry.split(":")[1]
        # Example-Output: passportObj = {"passport_1": {"ecl": "gry", "pid": "860033327", "eyr": "2020" ...}, "passport_2": {...}}
        passportObj[f"passport_{passportCounter}"][entryId] = entryValue

    # Looping through nested dictionary
    validPassports = 0
    for nestedPassport in passportObj.keys():
        # nestedPassport = passport_1, passport_2 etc.
        passportKeys = 0
        for passport in passportObj[nestedPassport].keys():
            # passport = keys of passportObj with passport_1, passport_2 etc. 
            passportKeys += 1
        
        if passportKeys >= 7:
            validPassports += 1
    
    print("Valid Passports: ", validPassports)

def validatePassports(passportObj):
    eyeColor        = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    validPassports  = 0
    passportKeys    = 7

    for nestedPassport in passportObj:
        validPassportKeys = 0
        if "byr" not in passportObj[nestedPassport].keys(): validPassportKeys -= 1
        if "iyr" not in passportObj[nestedPassport].keys(): validPassportKeys -= 1
        if "eyr" not in passportObj[nestedPassport].keys(): validPassportKeys -= 1
        if "hgt" not in passportObj[nestedPassport].keys(): validPassportKeys -= 1
        if "hcl" not in passportObj[nestedPassport].keys(): validPassportKeys -= 1
        if "ecl" not in passportObj[nestedPassport].keys(): validPassportKeys -= 1
        if "pid" not in passportObj[nestedPassport].keys(): validPassportKeys -= 1

        for passport in passportObj[nestedPassport].items():
            if passport[0] == "byr":
                if len(passport[1]) > 0:
                    if int(passport[1]) >= 1920 and int(passport[1]) <= 2002:
                        validPassportKeys += 1
            
            if passport[0] == "iyr":
                if len(passport[1]) > 0:
                    if int(passport[1]) >= 2010 and int(passport[1]) <= 2020:
                        validPassportKeys += 1

            if passport[0] == "eyr":
                if len(passport[1]) > 0:
                    if int(passport[1]) >= 2020 and int(passport[1]) <= 2030:
                        validPassportKeys += 1

            if passport[0] == "hgt":
                if len(passport[1]) > 0:
                    if "cm" in passport[1]:
                        tmp = passport[1].replace("cm", "")
                        if int(tmp) >= 150 and int(tmp) <= 193:
                            validPassportKeys += 1

                    elif "in" in passport[1]:
                        tmp = passport[1].replace("in", "")
                        if int(tmp) >= 59 and int(tmp) <= 76:
                            validPassportKeys += 1
            
            if passport[0] == "hcl":
                if len(passport[1]) != 0:
                    if len(passport[1]) == 7:
                        if re.match("[0-9a-f#]", passport[1]):
                            validPassportKeys += 1

            if passport[0] == "ecl":
                if len(passport[1]) > 0:
                    if passport[1] in eyeColor:
                        validPassportKeys += 1
            
            if passport[0] == "pid":
                if len(passport[1]) != 0:
                    if len(passport[1]) == 9:
                        if passport[1].isdigit():
                            validPassportKeys += 1
        
        if validPassportKeys >= passportKeys:
            validPassports += 1
    
    return validPassports


def task2():
    lines = []
    with open("files_for_days/day4.txt", "r") as file:
        for line in file:
            line = line.replace("\n", "")
            lines.append(line.replace("\r", ""))        # Example-Output: ["ecl:gry pid:860033327 eyr:2020 hcl:#fffffd", 
                                                        # "byr:1937 iyr:2017 cid:147 hgt:183cm", ""]
    
    passports = []
    for line in lines:
        lineContents = line.split(" ")
        for lineContent in lineContents:
            passports.append(lineContent)       # Example-Output: ["ecl:gry", "pid:860033327", "eyr:2020", "hcl:#fffffd" ..., "", ...]
    
    passportObj         = {}
    passportCounter     = 1
    passportObj[f"passport_{passportCounter}"] = {}
    for passportEntry in passports:
        if len(passportEntry) == 0:
            passportCounter += 1
            passportObj[f"passport_{passportCounter}"] = {}
            continue

        if passportEntry.split(":")[0] == "cid":
            continue
        
        entryId     = passportEntry.split(":")[0]
        entryValue  = passportEntry.split(":")[1]
        # Example-Output: passportObj = {"passport_1": {"ecl": "gry", "pid": "860033327", "eyr": "2020" ...}, "passport_2": {...}}
        passportObj[f"passport_{passportCounter}"][entryId] = entryValue

    print("Valid Passports: ", validatePassports(passportObj))

task1()
task2()