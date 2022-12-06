# Day05 Difficulties and Thoughts

## Part1

First, I had serious problems with parsing the crates accordingly. Since I didn't find a solution by myself and solutions I found on the [Day 05 Solutions Reddit Page](https://www.reddit.com/r/adventofcode/comments/zcxid5/2022_day_5_solutions/) were too difficult to understand for me, I decided to **hardcode** the crates and their order. It's not a good solution, but I didn't want to think for more than a hour to get **only the crate-parsing**.

When I hardcoded the crates I put them in the following order:

```python
example_crates = [
    ['N', 'Z'],
    ['D', 'C', 'M'],
    ['P']
]
```

That was a terrible idea, since I first wanted to use `pop()` to remove entries in the `from_crate_column` list (Note: I didn't use `pop`). But I already hardcoded my task-crates in that format and using `list.reverse()` did not work for me as expected. So I wasted another 10 minutes re-arranging the crate-columns to the following order:

```python
example_crates = [
    ['Z', 'N'],
    ['M', 'C', 'D'],
    ['P']
]
```

With this order I was able to work with it better. I came up with a solution quite quick, but I did a mistake by first using the following code to *move crates to another crate_column*:

```python
crates[to_crate_column].extend(crates[from_crate_column][:crates_to_move])
```

Now what's wrong with this line of code you might wonder? Well using `[:crates_to_move]` I don't select crates from `-1 to 0`, but from `0 to -1` instead. This means that a crate column like `['M', 'C', 'D']` wouldn't move `'D'` to another crate-column, but `'M', 'C'` instead.
So using `[crates_to_move:]` fixed the problem for me.

What I overread was the part "*Crates are moved one at a time*". With using the above mentioned code-line I do, what is asked in the second part: not moving crates **step by step**, but all crates **directly** instead. Until I found out, another 40 minutes had passed.

So using a simple step by using `reverse()` I fixed the problem with the following code:

```python
tmp_from_crate_column = crates[from_crate_column][crates_to_move:]
# Reverse == step by step
tmp_from_crate_column.reverse()
crates[to_crate_column].extend(tmp_from_crate_column)
```

And finally finished part1 after about 1h 30min.

## Part2

As explained in part1, I first did part2 without knowing it. So using `crates[to_crate_column].extend(crates[from_crate_column][crates_to_move:])` got me part2 really quick.
