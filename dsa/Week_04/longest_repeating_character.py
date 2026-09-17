"""
You are given a string s consisting of only uppercase english characters and an integer k. 
You can choose up to k characters of the string and replace them with any other uppercase English character.
After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

Example 1:
Input: s = "XYYX", k = 2
Output: 4
Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.

Example 2:
Input: s = "AAABABB", k = 1
Output: 5

constraints:
1 <= s.length <= 100,000
0 <= k <= s.length
s consists of only uppercase english characters.
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Key Question : For the current window, how many characters would I need to replace so that the whole window becomes the same character?
        it means we can point right till we find any different character and k integer because we can replace that and than check if next character is same
        if not than we return the length if same than we continue counting
        """

        left = 0
        right = 0
        count = {}

        max_frequency = 0
        max_length = 0

        while right < len(s):
            char = s[right]
            """
            we save the 1st charcater so we can compare with the left one
            also we store the char in dictornary with the count, if found add +1, if not add +1 in 0

            Take example of s = "AABABC" k = 1
            
            s[0] = A and count is 1
            s[1] = A and count is 2
            s[2] = B and count is 1
            s[3] = A and count is 3
            s[4] = B and count is 2
            """
            count[char] = count.get(char, 0) + 1

            max_frequency = max(max_frequency, count[char])
            """
            here we compare max frequency if that is greater or the value of count for that character and store in max frequency
            max frequency is 1
            max frequency is 2
            max frequency (2,1) is 2
            max frequency is (2,3) is 3
            max frequency is (3,2) is 3
            """ 

            window_length = right - left + 1
            """
            window length = 0 - 0 + 1 = 1 hence window length - max frequency is 0 > k false, so it will not go inside the below while loop
            window length = 1 - 0 + 1 = 2, now window length - max frequency is 2-2 = 0 > 1 false,  so it will not go inside the below while loop
            window length = 2 - 0 + 1 = 3, now 3 - 2 = 1, 1> 1 false
            window length = 3 - 0 + 1 = 4, now 4 - 3 = 1, 1> 1 false
            window length = 4 - 0 + 1 = 5, now 5 - 3 = 2, 2>1 and hence this time it will enter the while loop on s[4] right
            """

            while window_length - max_frequency > k:
                count[s[left]] -=  1
                left += 1
                """
                here we remove 1 count from dict and increment left to 1 
                so, count[s[0]] which is count[a] ia 3, 3-1 = 2
                left = 0 + 1 = 1 
                """

                window_length = right - left + 1
                """
                window length will be 4 - 1 + 1 = 4
                """

            max_length = max(max_length, window_length)
            """
            max length will be 1 because (0,1) max is 1 and increment right to + 1 so right will be 0 + 1 = 1
            max lenght will be 2 and increment right to 2
            max length will be 3 and incremeent right to 3
            max lenght will be 4 and increment right to 4
            max length will be (4,4) is 4 and increment right to 5
            """

            right += 1

        return max_length

"""
We create a dictionary count to store how many times each character appears inside the current window. 
right expands the window and we keep track of max_frequency, which is the count of the most common character. 
We calculate how many replacements are needed using window_length - max_frequency. If that is greater than k, the window is invalid, 
so we move left forward and shrink the window. Once the window is valid again, we compare its length with max_length.
"""


def main():
    solution = Solution()

    input = "AAABABB"
    k = 1

    result = solution.characterReplacement(input, k)
    print("result: ", result)

main() 

"""
Time complexity: O(n) because left and right only move forward. 
Space complexity: O(1) in this problem because the string contains only uppercase English letters, so the dictionary can contain at most 26 keys.
"""