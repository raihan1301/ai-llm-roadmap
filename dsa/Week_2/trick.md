Week 2 — Arrays & Hashing Continued

Goal
Apply hashing patterns to validation, encoding, prefix/suffix calculations, and sequence detection.

1. Valid Sudoku
Trigger: When duplicates must be checked independently inside rows, columns, or regions, think separate sets for each group.
Trick: Check every row, every column, and every 3×3 box separately. Ignore "." and fail when a number is already in the current set.

2. Product of Array Except Self
Trigger: When the problem says “for each position, calculate something using all elements except the current one”, especially when a direct solution needs nested loops, think prefix + suffix.
Trick: First store the product of everything to the left of each position, then move backward and multiply by the product of everything to the right.

3. Encode and Decode Strings
Trigger: When multiple strings must be combined and later separated safely, do not rely only on a delimiter because the delimiter may appear inside the data.
Trick: Store each string as length + separator + string, for example 5#Hello. During decoding, read the length first, then take exactly that many characters.

4. Longest Consecutive Sequence
Trigger: When the problem asks for consecutive numbers but says the original order does not matter, think set + sequence start.
Trick: Put all numbers in a set. Only start counting from a number when num - 1 does not exist. Then keep checking the next consecutive numbers.
Simpler alternative: Sort unique numbers and count consecutive differences of 1. Easier to understand, but it becomes O(n log n) because of sorting.

5. Week 1 Revision — Group Anagrams
Trigger: When several items belong together because they share the same underlying pattern, create a dictionary key that represents that pattern.
Trick: For anagrams, the sorted word can be that key.

Week 2 Memory Rules
Except current position → prefix + suffixSafe encode/decode → store lengthConsecutive sequence → start only where previous number is missingValidation groups → reset a set for each independent group