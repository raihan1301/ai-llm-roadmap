"""
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:
Input: strs = ["act","pots","tops","cat","stop","hat"]
Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

Example 2:
Input: strs = ["x"]
Output: [["x"]]

Example 3:
Input: strs = [""]
Output: [[""]]

Constraints:
1 <= strs.length <= 1000
0 <= strs[i].length <= 100
strs[i] is made up of lowercase English letters.

Answer consist of 3 version : version 3 is best
"""

"""
Version 1:
double-loop approach: take each word, compare it with every remaining word, check whether both are anagrams, and place matching words into the same group. 
You would also need a used set or list so that a word already added to a group is not processed again. 
However, this approach would take roughly O(n² × k log k) time if you sort words during every comparison, 
because each of the n words may be compared with almost every other word. 
The dictionary approach is better because each word is processed only once and placed directly into the correct group.

This will through inefficient code error because of time complexity
"""

class Solution_V1:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:   # return value is list of list string

        final_list = []
        used = set()

        for i in range(len(strs)):

            if i in used:
                continue

            output_list = [strs[i]]
            used.add(i)

            sorted_word = sorted(strs[i])

            for j in range(i+1, len(strs)):

                if j in used:
                    continue

                if sorted_word == sorted(strs[j]):
                    output_list.append(strs[j])
                    used.add(j)

            final_list.append(output_list)

        return final_list

"""
Version 2: 

simpler sorting approach first. Two words are anagrams when their letters become identical after sorting.

The time complexity is O(n × k log k) because we sort every word, where n is the number of words and k is the average word length. 
The space complexity is O(n × k) because all words are stored in the dictionary groups. 
This is slightly slower than the 26-character counting solution, but it is much easier to understand and is acceptable for the given constraints.
"""
            
class Solution_V2:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        groups = {}

        for word in strs:
            sorted_word = "".join(sorted(word))

            """
            sorted(word) sorts the letters but returns them as a list. 
            For example, sorted("cat") gives ["a", "c", "t"]. "".join(...) joins those letters back into one string, so the result becomes "act"
            """

            if sorted_word not in groups:
                groups[sorted_word] = []  # here we store the sorted word as key

            groups[sorted_word].append(word)   # here we store individual word as an value to that sorted word key

        return list(groups.values())

"""
Version 3:

A cleaner solution is to create a character-count signature for every word and use that signature as a dictionary key.

Each word receives a 26-number signature representing how many times each lowercase letter appears. For example, "act" and "cat" produce the same signature, 
so they are stored under the same dictionary key. We convert the character-count list into a tuple because dictionary keys must be immutable. 
If n is the number of words and k is the maximum word length, the time complexity is O(n × k) because every character is visited once, 
and the space complexity is O(n × k) because the dictionary stores all the input words in their groups.
"""
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = {}

        for word in strs:
            char_count = [0] * 26  # we initialize 26 0s in the list

            for char in word:  # now this will loop over each character in the woerd
                index = ord(char) - ord("a") 
                """
                ord(char) gives the numeric code of a character. Since lowercase letters appear in order, 
                subtracting the code of "a" converts letters into indexes:
                For example, when char is "c": so index is 2 = ord("c") - ord("a")
                """
                char_count[index] += 1  #This increases the count for that letter. For the word "cat":  c, a, t is to 1 all other 0

            key = tuple(char_count)
            """
            converts the list into a tuple because a list cannot be used as a dictionary key, but a tuple can. 
            Words such as "act", "cat", and "tac" all produce the exact same tuple because they contain the same letters the same number of times.
            """

            if key not in groups:  # now we use this key to check if it exist in groups or not
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())

def main():
    words = input("Enter words separated by spaces: ").split()

    solution = Solution()
    result = solution.groupAnagrams(words)

    print(result)


if __name__ == "__main__":
    main()

                


                

                
            