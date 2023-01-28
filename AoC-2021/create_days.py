import os
import json

with open("config.json", "r") as conf:
    config = json.load(conf)

defaultPath = config["defaultPath"]

changePath = input(f"Do you want to change the path for the days? Default is: {defaultPath} (y/n)> ")

if changePath == "y" or changePath == "yes":
    defaultPath = input("Enter the new path: ")
    if not defaultPath[-1:] == "/":
        defaultPath += "/"
    
    sessionPath = input (f"Do you want to save the path as default? (y/n)>")
    if sessionPath == "y" or sessionPath == "yes":
        with open("config.json", "w") as conf:
            newConf = { "defaultPath": defaultPath }
            json.dump(newConf, conf)

allDays = input("Do you want to create all days (y/n)?> ")

if allDays == "y" or allDays == "yes":
    if not os.path.exists(defaultPath):
        os.makedirs(defaultPath)
        print("Created path: ", defaultPath)
    else:
        print("Path allready exists! Skipping creating path!")

    for day in range(1, 26, 1):
        if day < 10:
            if not os.path.exists(f"{defaultPath}0{day}"):
                os.makedirs(f"{defaultPath}0{day}")
                open(f"{defaultPath}0{day}/example.txt", "w").close()
                open(f"{defaultPath}0{day}/task_1.txt", "w").close()
                open(f"{defaultPath}0{day}/task_2.txt", "w").close()
                open(f"{defaultPath}0{day}/main.py", "w").close()
                open(f"{defaultPath}0{day}/Readme.md", "w").close()
                print(f"Created: {defaultPath}0{day}")

            else:
                print(f"Day already exists! Skipping day {defaultPath}0{day}")

        else:
            if not os.path.exists(f"{defaultPath}{day}"):
                os.makedirs(f"{defaultPath}{day}")
                open(f"{defaultPath}{day}/example.txt", "w").close()
                open(f"{defaultPath}{day}/task_1.txt", "w").close()
                open(f"{defaultPath}{day}/task_2.txt", "w").close()
                open(f"{defaultPath}{day}/main.py", "w").close()
                open(f"{defaultPath}{day}/Readme.md", "w").close()
                print(f"Created: {defaultPath}{day}")

            else:
                print(f"Day already exists! Skipping day {defaultPath}{day}")
else:
    try:
        day = int(input("Which day do you want to code for?> "))
        
        if day < 10:
            if not os.path.exists(f"{defaultPath}0{day}"):
                os.makedirs(f"{defaultPath}0{day}")
                open(f"{defaultPath}0{day}/example.txt", "w").close()
                open(f"{defaultPath}0{day}/task_1.txt", "w").close()
                open(f"{defaultPath}0{day}/task_2.txt", "w").close()
                open(f"{defaultPath}0{day}/main.py", "w").close()
                open(f"{defaultPath}0{day}/Readme.md", "w").close()
                print(f"Created: {defaultPath}0{day}")

            else:
                print(f"Day already exists! Skipping day {defaultPath}0{day}")

        else:
            if not os.path.exists(f"{defaultPath}{day}"):
                os.makedirs(f"{defaultPath}{day}")
                open(f"{defaultPath}{day}/example.txt", "w").close()
                open(f"{defaultPath}{day}/task_1.txt", "w").close()
                open(f"{defaultPath}{day}/task_2.txt", "w").close()
                open(f"{defaultPath}{day}/main.py", "w").close()
                open(f"{defaultPath}{day}/Readme.md", "w").close()
                print(f"Day created: {defaultPath}{day}")

            else:
                print(f"Day already exists! Skipping day {defaultPath}{day}")
    except:
        print("Only numbers are allowed! Please enter a valid number!")