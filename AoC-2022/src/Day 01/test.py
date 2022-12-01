filename = "examples/example1.txt"

def get_elve_calory_info(filename, top_elves_count=3):
    elves = dict()
    elve_food = list()
    top_elves = list()
    calories_per_top_elve = list()
    top_elves_length = top_elves_count
    elve_counter = 1
    elve_lowest_calories = 0
    lowest_calories = 0
    elve_highest_calories = 0
    highest_calories = 0
    current_calories = 0
    elves["num_of_elves"] = ""
    elves["elve_lowest_calories"] = ""
    elves["lowest_calories"] = ""
    elves["elve_highest_calories"] = ""
    elves["highest_calories"] = ""
    elves["top_elves"] = ""
    elves["calories_per_top_elve"] = ""
    elves["top_elves_total_calories"] = ""

    with open(filename, "r") as ex_input:
        for calory in ex_input:
            try:
                calory = int(calory.split("\n")[0])
            except Exception:
                calory = 0

            if calory == 0:
                current_calories = sum(elve_food)

                if elve_counter == 1:
                    lowest_calories = current_calories
                    
                if current_calories < lowest_calories:
                    lowest_calories = current_calories
                    elve_lowest_calories = elve_counter

                if current_calories > highest_calories:
                    highest_calories = current_calories
                    elve_highest_calories = elve_counter

                if len(top_elves) < top_elves_length:
                    top_elves.append(elve_counter)
                    calories_per_top_elve.append(current_calories)
                else:
                    if current_calories > calories_per_top_elve[-1]:
                        calories_per_top_elve.pop()
                        top_elves.pop()
                        calories_per_top_elve.append(current_calories)
                        top_elves.append(elve_counter)

                calories_per_top_elve.sort(reverse=True)
                top_elves.sort(reverse=True)
                
                elve_food = list()
                elve_counter += 1
                continue
            
            elve_food.append(calory)

        elves["num_of_elves"] = elve_counter
        elves["elve_lowest_calories"] = elve_lowest_calories
        elves["lowest_calories"] = lowest_calories
        elves["elve_highest_calories"] = elve_highest_calories
        elves["highest_calories"] = highest_calories
        elves["top_elves"] = top_elves
        elves["calories_per_top_elve"] = calories_per_top_elve
        elves["top_elves_total_calories"] = sum(calories_per_top_elve)

    return elves

calory_output = get_elve_calory_info(filename)

print(calory_output)