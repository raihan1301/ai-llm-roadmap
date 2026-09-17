"""
Given a string s, return true if it is a palindrome, otherwise return false.
A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.
Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Example 1:
Input: s = "Was it a car or a cat I saw?"
Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Example 2:
Input: s = "tab a cat"
Output: false
Explanation: "tabacat" is not a palindrome.

Constraints:
1 <= s.length <= 1000
s is made up of only printable ASCII characters.
"""

class Solution_V2:
    def isPalindrome(self, s: str) -> bool:

        clean_string = ""  # string can contain other thing as well so remove that and make it lower case

        for char in s:
            if char.isalnum():  # is alnum means is character or not
                clean_string += char.lower()

        length = len(clean_string)
        forward_index = range(length) 

        """
        (length - 1, -1, -1) --> means 1 less length , 
        second -1 means stop value so if index becomes -1 stop
        third -1 means decrement the number by -1
        """
        backward_index = range(length-1, -1, -1)

        """
        imp if we 2 value in 1 loop use zip to unpack
        """
        for i, j in zip(forward_index, backward_index):

            if clean_string[i] != clean_string [j]:
                return False

        return True
    """
    It is still O(n) time, but because you first create clean_string, it uses O(n) extra space.
    better version is below where we use while loop, but the abovbe code is also good for two pointers
    """

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:

            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

            """
            We create two indexes: left starts at the beginning of the string and right starts at the end. 
            If either pointer is sitting on a space or punctuation character that is not isalnum, we move it inward until it reaches an alphanumeric character.
            
            Then we compare the two characters after converting them to lowercase. 
            If they are different, the string cannot be a palindrome, so we return False. 
            
            If they match, we move both pointers inward and repeat until they meet.
            """

        return True
    
    """
    Time complexity: O(n) because each pointer moves through the string only once overall. 
    Space complexity: O(1) because we only use the left and right variables and do not create another string.
    """       

def main():
    solution = Solution()

    input = "tab a cat"
    result = solution.isPalindrome(input)
    print("result: ", result)

main()