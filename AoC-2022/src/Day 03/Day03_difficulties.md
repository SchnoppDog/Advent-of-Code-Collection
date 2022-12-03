# Difficulties and thoughts of day 03

## Part 1

For the past two days I was lookin at other python results from other persons at the [solutions subreddit](https://www.reddit.com/r/adventofcode/comments/zac2v2/2022_day_2_solutions/) of advent of code 2022. I got more or less inspired by some solutions solving the problems. What I did not think of in the past two days was using pythons `slicing` function. This helped me a lot in the first part of this days task. By simply using the following code you can get the two compartments of the rucksack really easy:

```python
compartment_one = rucksack[:int(len(rucksack) / 2)]
compartment_two = rucksack[int(len(rucksack) / 2):]
```

What those two lines simply do are slicing first from `0` to the **middle** of the string and second from the **middle** of the string to the **end**. Pretty simple and yet fast.

For the **alphabet-priority** / **char-priority** I first wanted to hardcode `["a", "b", "c", ...]`. For uppercase characters I would simply convert them to lowercase, search them in the hardcoded alphabet and add `+26` to it, to get the uppercase-priority. This, of course, works, but there needed sto be omething more simple.

So I searched the web and found out about the `string` module. It can create an output of all `ascii_lowercase` and `ascii_uppercase` combined. That was perfect for my usecase. Converting it to a list is easy by using the `list()` inbuilt function. Adding `+1` for indexing and tadaa- you get the **char-priority**.

## Part 2

While part one was about 30 minutes of thinking, part two was done in like 5 mins. It was really easy. The first three elves are in a group, what would fit more than using **modulo** operation? So I used `x modulo 3`, x being an enumerated `rucksack`. If the `rucksack modulo 3` is 0 a new elve-group appears.
The rest was done by checking **if a char in the first rucksack also occurs in the two consecutive rucksacks in the group**. If yes the **char-priority** is checked, returned and added to the `group_priorities` list. Summing up the priorities returns the total priority-number of all groups.

## Conclusion

It's been only three days, but day three has yet been the easiest one to solve for me.
