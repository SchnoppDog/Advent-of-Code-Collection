# Difficulties and Thoughts of day 04

On this day I did not encounter any problems I could not solve in mere seconds. As always I read through the entire text, copied everything I needed for the script and took notes with a pen and paper on my desk, how I wanted to solve this problem.

For the range-overlapping in the first part I thought of something like using `if range(a,b) in range(c,d)`, but I quickly discarded this idea. Since one of the ranges needs to be lower with the first number and the second being equal to the other at minimum, I decided just using a comparison between those two elves numbers.

Part two was easy too. I used to look at the solutions of other people and found an interesting method of the inbuilt-function `set()`: `set.intersection()` which looks for anything, in my case numbers, that a set shares with other sets. This was perfect for my case.

It is a bit long, but it works:

```python
set(range(int(range_one[0]), int(range_one[1])+1)).intersection(set(range(int(range_two[0]), int(range_two[1])+1)))
```

which does the following:

- `range_one` and `range_two` are lists (or tuples) with the content i.e. `["2", "8"]` and `["3", "7"]`
- Using `set()` to get a set of items.
- Using `range()` in `set()` to create a set of the specified range
- Using `intersection()` with the same set-range-setup as for `range_one` and get a set returned which contains all overlapping numbers.

I only needed some modifications in my script to inplement part two. And day 04 was solved quite fast (but not as fast as other programming-gods at aoc).