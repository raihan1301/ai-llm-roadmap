"""
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:
Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.

Example 1:
Input: s = "[]"
Output: true

Example 2:
Input: s = "([{}])"
Output: true

Example 3:

Input: s = "[(])"
Output: false
Explanation: The brackets are not closed in the correct order.

Constraints:
1 <= s.length <= 1000
"""

class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        """
        we create empty list to store the opening brackets and remove when it is close
        take an example = ([{}])
        """

        brackets = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for char in s:

            if char in brackets.values():
                stack.append(char)
                """
                so we check if the character in string is open bracket if yes we append to stack,
                so 1st is ( , we can see this in value so we add ) : stack = [(]
                2nd is [, so we add ] : stack = [([]
                3rd s {, so we add }  : stack = [([{]
                4th is }, so it is not a value hence we do not add it
                """

            else:
                if not stack:
                    return False
                """
                if it comes to else we check if stack is not empty, if its empty it is wrong
                """

                last_one = stack.pop()
                """
                now it is not returned false yet, it means it is in stack hence we pop it it will remove last one
                so it will remove : stack = ([{ "{" , hence : stack = ([
                """

                if last_one != brackets[char]:
                    return False
                """
                "{" !=  "{" , so it is not false
                """

        return len(stack) == 0

"""
Time complexity: O(n) because we process each character once.
Space complexity: O(n) in the worst case because the stack may store all opening brackets.
"""

def main():
    solution = Solution()

    input1 = "([{}])"

    result = solution.isValid(input1)
    print("result: ", result)

main() 