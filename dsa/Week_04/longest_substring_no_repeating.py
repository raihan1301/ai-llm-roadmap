"""
Given a string s, find the length of the longest substring without duplicate characters.
A substring is a contiguous sequence of characters within a string.

Example 1:
Input: s = "zxyzxyz"
Output: 3
Explanation: The string "xyz" is the longest without duplicate characters.

Example 2:
Input: s = "xxxx"
Output: 1

Constraints:
0 <= s.length <= 50,000
s may consist of printable ASCII characters.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        right = 0
        max_length = 0

        seen = set()
        """
        we create empty set to make unique substring character
        """

        while right < len(s):

            while s[right] in seen:
                """
                if the character new character from string is already in the seen set
                it means this character is repeat from the previous one so we remove the previous same character
                """
                seen.remove(s[left])

                """
                now we add 1 to the left so it point to next character in string
                """
                left += 1

            seen.add(s[right])
            """
            we add the character to seen set
            and if it was repeated we already removed that from the top while loop
            """

            current_length = right - left + 1
            """
            we want the length so left and right index difference give us the length
            """
            max_length = max(max_length , current_length)

            right += 1

        return max_length

    """
    Example visualize : zxyzxyz
    z       → length 1
    zx      → length 2
    zxy     → length 3
    zxyz    → duplicate z

    remove left z
    window becomes xyz → length 3
    """

def main():
    solution = Solution()

    input = "zxyzxyz"

    result = solution.lengthOfLongestSubstring(input)
    print("result: ", result)

main() 

"""
Time complexity: O(n) because although there is a while loop inside another while, each character is added to the set once and removed at most once. 
So the pointers only move forward through the string overall.

Space complexity: O(n) in the worst case because the seen set may contain every character if there are no duplicates.
"""