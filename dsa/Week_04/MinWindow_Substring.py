"""
Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. 
If such a substring does not exist, return an empty string "".
You may assume that the correct output is always unique.

Example 1:
Input: s = "OUZODYXAZV", t = "XYZ"
Output: "YXAZ"
Explanation: "YXAZ" is the shortest substring that includes "X", "Y", and "Z" from string t.

Example 2:
Input: s = "xyz", t = "xyz"
Output: "xyz"

Example 3: 
Input: s = "x", t = "xy"
Output: ""

constraints :
1 <= s.length <= 100,000
1 <= t.length <= 100,000
s and t consist of uppercase and lowercase English letters.
"""
class Solution_V2:
    def minWindow(self, s: str, t: str) -> str:
        need = {}

        for char in t:
            need[char] = need.get(char, 0) + 1

        best = ""

        for i in range(len(s)):
            current = {}

            for j in range(i, len(s)):
                char = s[j]
                current[char] = current.get(char, 0) + 1

                valid = True

                for needed_char in need:
                    if current.get(needed_char, 0) < need[needed_char]:
                        valid = False
                        break

                if valid:
                    substring = s[i:j + 1]

                    if best == "" or len(substring) < len(best):
                        best = substring

                    break

        return best

"""
We first create a need dictionary containing the characters required by t. 
Then i chooses every possible starting position in s, and j moves forward from that position while counting characters in current. 
After adding each character, we check whether current contains enough copies of every character required by need. 
As soon as it does, we have the smallest valid substring for that particular starting position, 
so we compare it with best and then break because making that same window longer cannot improve the answer.
"""

"""
Time complexity: roughly O(n²) here, with an additional small check over the required characters each time. 
With unrestricted characters you could describe it more precisely as O(n² x m), where m is the number of distinct required characters.

Space complexity: O(m) for the frequency dictionaries.
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:        
        if len(t) > len(s):
            return ""
        """
        length of t is more than s it is empty substring
        """

        need = {}

        for char in t:
            need[char] = need.get(char, 0) + 1
            """
            in need dict we count all the t character and add inside
            """

        window = {}

        left = 0
        have = 0
        required = len(need)

        min_length = float("inf")
        result_left = 0
        result_right = 0

        for right in range(len(s)):
            """
            we start for loop for right with string s length example : OUZODYXAZV, so it will be 0 to 10
            """
            char = s[right]
            window[char] = window.get(char,0) + 1
            """
            here we store the char for right index and add to window dict with the count
            """

            if char in need and window[char] == need[char]:
                have += 1
            """
            So here if the char found in need which is t string dict and the count of char is same as we have in need dict
            we found one character and we increment have to +1
            """

            while have == required:
                """
                required is lenght of need and have means we need to match that
                """
                current_length = right - left + 1

                if current_length < min_length:
                    min_length = current_length
                    """
                    we are finding min length so if current lenght is less we will update it
                    """

                    result_left = left
                    result_right = right

                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1

                left += 1

        if min_length == float("inf"):
            return ""

        return s[result_left:result_right + 1]

"""
We first create need, which stores how many of each character t requires. Then we move right through s and count characters inside the current window using window. 
have tells us how many required character types currently have enough copies. 
When have == required, our window contains everything from t, so instead of stopping, we move left forward to make the window as small as possible. 
Every time we find a smaller valid window, we save its left and right indexes. 
If shrinking causes one required character to fall below the amount needed, the window becomes invalid and we resume expanding right.
"""

def main():
    solution = Solution()

    input1 = "OUZODYXAZV"
    input2 = "XYZ"

    result = solution.minWindow(input1, input2)
    print("result: ", result)

main() 

"""
Time: O(n) because right moves forward once and left also only moves forward once. 
Even though there is a while inside the for, neither pointer goes backward.

Space: O(m) where m is the number of distinct characters in s/t; 
since this problem only uses English uppercase/lowercase letters, it is effectively bounded and can be treated as O(1).
"""