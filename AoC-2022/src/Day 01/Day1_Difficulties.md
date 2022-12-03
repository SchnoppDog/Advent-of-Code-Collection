# Difficulties for me at day 1

I had some difficulties solving the second puzzle. In the first puzzle I needed to structurize myself and what data I wanted to collect. Where my problem was? Understanding why my results vary so much from the puzzles example result.

I use the following code-snippet to extract the top three elves and their total item-calories:

```python
if len(top_elves) < top_elves_length:
    top_elves.append(elve_counter)
    calories_per_top_elve.append(current_calories)
else:
    if current_calories > calories_per_top_elve[-1]:
        calories_per_top_elve.pop()
        top_elves.pop()
        calories_per_top_elve.append(current_calories)
        top_elves.append(elve_counter)
```

My first thought was that I put this if-else statemant to the the one which gets the highest caloriest. But that wouldnt work in this scenario cause **10000** would not be added to `calories_per_top_elve` since it is not bigger than the total calories of the fourth elve which there is **24000**.
So i threw away that idea an decided that this if-else statemant should be a standalone one.

To handle the elve with the lowest total calories I sorted the list in reverse so I know that the last item in the list will be the elve with the lowest calories. With this, if the next calories are bigger than the lowest in the list, I can easily `pop` the last item and append the other one.
Of course I need to sort again. That's why the sorting is in the main for loop. It isn't nice since it is not only run on changes to the list, but it works in this scenario.

The bigger problem was, that in the puzzle-example the last number in the file was not taken and thus compared to other numbers. That is because my script uses the empty line to get the `calory_items` together. For some reason I can't explain python does not recognize the following as an empty line:

```txt
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
            <------ Python is ignoring this empty line
```

I had to manually add **another empty line** so the python code works and takes the **10000** into account. It is not nice since I had to manually alter the task-input, but I did not find an easy way to manage **EOF** so I do not need to write redundant code for the last number.

As I already mentioned in my main readme: I am not an expert! I am more a beginner. That's why my code looks ugly and can be improved, but I try my best to get those **stars**!

PS: I know I do not need to initialize variables at the start of the script, but I like it more since it displays an overview of which variables are used in the script.
