# My difficulties with day 02

Today there weren't as much difficulties as yesterday - if any. I knew what I needed to do, but I wanted to create a way **not using so many if-statemants** to reduce redundant code.

I thought about it for like 45 minutes and tried many different things, but in the end I could not get any solution up in my mind. So I stuck with boring if-statemants and the newly introduced **match-case** statemants in **python 3.10**.

When I ran my code for the first time the output seemed alright, but the AoC-website said, my result was wrong. I tried to figure out the problem for 15 minutes straigt until I saw a little mistake:

```python
case "C":
    if rps_match[1] == "X":
        total_points += win_points + 1
    if rps_match[1] == "Y":                 # <---- this is the problematic line
        total_points += lose_points + 2
    else:
        total_points += draw_points + 3
```

The code did not work as expected since the **second** if-statemant was a **normal** `if`. When changed to an `elif`-statement my code worked perfectly fine and I solved the first part of day 02.

For the second part I quickly saw that the task would be in reversed order so I added to my `get_rps_total_wins()`-function another parameter `true_total_points` which added several if-statements whether the total rock, paper, scissor points shall be calculated for task1 oder task2.

Whats interesting is that I did not need to add the if-statements to the `case "B"` since the calculation is the same as in task one. Atleast I somehow prevent putting more if-statements in my code ^^.
