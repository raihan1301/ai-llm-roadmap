"""
You are given two strings s1 and s2.
Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.
Both strings only contain lowercase letters.

Example 1:
Input: s1 = "abc", s2 = "lecabee"
Output: true
Explanation: The substring "cab" is a permutation of "abc" and is present in "lecabee".

Example 2:
Input: s1 = "abc", s2 = "lecaabee"
Output: false

Constraints:
1 <= s1.length, s2.length <= 10000
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if s1 in s2:
            return True

        if len(s1) > len(s2):
            """
            if length of s1 is more it it automatically false no permutation exist
            """
            return False

        s1_count = {}
        window_count = {}

        for char in s1:
            s1_count[char] = s1_count.get(char,0) + 1
            """
            first we count the character in s1 and how many times they repeat
            so in our example abc = a, b, c all are in 1
            """

        left = 0

        for right in range(len(s2)):
            """
            left initialize to 0
            right will be range so basically s2 in our example lecabee is 7, so right will be 0 to 7
            """

            char = s2[right]  
            window_count[char] = window_count.get(char, 0) + 1
            """
            here char will be l, window count will be 1 for l
            now e, window count will be 1 for e
            now c, window count will be 1 for c
            s2[3] now a, window count will be 1 for a
            s2[4] now b, window count for b is 1

            """

            if right - left + 1 > len(s1):
                """
                so basically 0 - 0 + 1 > 3 false it will not come inside
                1 - 0 + 1 > 3 false it will not come inside
                2 - 0 +  1 > 3 , false
                3 - 0 + 1 > 3, this is true so it will enter the if statement basically at char a for s2
                4 - 1 + 1 > 3 true hence it will enter for b 
                """

                left_char = s2[left]
                window_count[left_char] -= 1
                """
                now we know the right alphabet which is a stored in char, left alphabet s2[0] is l, so we remove that count from window count because window got bigger than 3
                hence l will be 0 in window count
                s2[1] is e, hence e will be 0
                """

                if window_count[left_char] == 0:
                    del window_count[left_char]
                    """
                    so as for s2[0] l become 0 we remove l, now window count is e : 1, c : 1, a: 1, b : 1
                    now, s2[1] e become 0 we remove e, now window count is c : 1, a: 1, b : 1 , it is same as s1 count dict
                    """

                left += 1


            if window_count == s1_count:
                """
                if window count dict and s1 count dict character and value is same it means we found the permutation
                """
                return True
            
        return False

"""
We first create a dictionary containing the character counts of s1. Then we create a sliding window inside s2 whose size is always the same as len(s1). 
As right moves forward, we add the new character to window_count. If the window becomes too large, we remove the character at left and move left forward. 
After every valid-size window, we compare its character counts with s1_count. If they are equal, that substring contains exactly the same letters as s1, 
so it is a permutation and we return True.
"""

def main():
    solution = Solution()

    input1 = "abc"
    input2 = "lecabee"

    result = solution.checkInclusion(input1, input2)
    print("result: ", result)

main() 

"""
Time complexity: approximately O(n) for this problem because the alphabet is limited to lowercase letters, 
so comparing the dictionaries is bounded by at most 26 characters.
Space complexity: O(1) for the same reason—the dictionaries can contain at most 26 lowercase letters.
"""