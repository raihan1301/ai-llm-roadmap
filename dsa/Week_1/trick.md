Week 1 — Arrays & Hashing

Goal
Learn when to use sets and dictionaries to avoid repeated searching and nested loops.

1. Contains Duplicate
Trigger: When the problem asks whether a value has appeared before, think set.
Trick: Store seen values in a set. If the current value is already there, a duplicate exists.

2. Valid Anagram
Trigger: When two strings must contain the same characters with the same counts, think frequency counting.
Trick: Use a dictionary to count characters in one string, then subtract/check using the second string.

3. Two Sum
Trigger: When you need two numbers that add to a target, think target - current number.
Trick: Store previously seen numbers and their indexes in a dictionary. For each number, check whether the needed value already exists.

4. Group Anagrams
Trigger: When words should be grouped by having the same characters, think common signature/key.
Trick: Convert each word into a signature, such as its sorted letters. Words with the same signature go under the same dictionary key.

5. Top K Frequent Elements
Trigger: When the problem asks for the most frequent values, think count first, rank second.
Trick: Use a dictionary to count occurrences, then sort or otherwise rank the numbers by their frequency.

Week 1 Memory Rule
Set = have I seen this?Dictionary = what information belongs to this value?