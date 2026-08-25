"""
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:
Input: s = "racecar", t = "carrace"
Output: true

Example 2:
Input: s = "jar", t = "jam"
Output: false

constraint:
1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) !=  len(t):
            return False    # if no of characters are not same it is not valid anagram

        char_count = {}

        for char in s:
            char_count[char] = char_count.get(char, 0) + 1  # it is dictionary so get will return the value of key

            """
            char_count.get(char, 0) checks whether char already exists in the dictionary. If it exists, it returns its current count; 
            if it does not exist, it returns the default value 0. Then + 1 increases the count and stores it back in the dictionary.

            {}
            {'r': 1}
            {'r': 1, 'a': 1}
            {'r': 1, 'a': 1, 'c': 1}
            {'r': 1, 'a': 1, 'c': 1, 'e': 1}
            {'r': 1, 'a': 1, 'c': 2, 'e': 1}
            {'r': 1, 'a': 2, 'c': 2, 'e': 1}
            {'r': 2, 'a': 2, 'c': 2, 'e': 1}

            Longer version for line 27
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

            """

        for char in t:
            if char not in char_count:
                return False   # because if t character not in s string it is false

            char_count[char] -= 1 # if found reduce the value

            if char_count[char] < 0:  # if the count goes negative than it is false
                return False

        return True
               

def main():
    s = input("Enter your 1st string: ")
    t = input("Enter your 2nd string: ")

    solution = Solution()
    result = solution.isAnagram(s,t)

    print(result)


if __name__ == "__main__":
    main()


"""
First, we check whether both strings have the same length because anagrams must contain the same number of characters. 
Then we use a dictionary to count every character in s. While going through t, we subtract from those counts. 
If a character does not exist in the dictionary or its count becomes negative, the strings are not anagrams. 

The solution takes O(n) time because it loops through both strings once, and O(n) space for the character-count dictionary, 
although with only 26 lowercase letters the practical space is constant.
"""