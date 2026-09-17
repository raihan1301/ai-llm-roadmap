"""
You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.
Return the integer that represents the evaluation of the expression.

The operands may be integers or the results of other operations.
The operators include '+', '-', '*', and '/'.
Assume that division between integers always truncates toward zero.

Example 1:
Input: tokens = ["1","2","+","3","*","4","-"]
Output: 5

Explanation: ((1 + 2) * 3) - 4 = 5
Constraints:

1 <= tokens.length <= 10000.
tokens[i] is "+", "-", "*", or "/", or a string representing an integer in the range [-200, 200].
"""

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        """
        it must use the two most recent numbers/results.
        """

        stack = []

        for token in tokens:
            if token not in ["+","-","*","/"]:
                stack.append(int(token))
                """
                so simple, if the token is not operator than we add integer to stack list
                """

            else:
                """
                if its operator than it comes inside else statement
                """
                second = stack.pop()
                first = stack.pop()
                """
                we remove last two integer for our operator
                """

                if token == "+":
                    result = first + second
                   
                if token == "-":
                    result = first - second
                
                if token == "*":
                    result = first * second
                
                if token == "/":
                    result = int(first / second)

                stack.append(result)
                """
                we add a result to our stack, because this result is latest integer now
                """

        """
        we return the last number because that will be the final result
        """
        return stack[-1]

"""
Time complexity: O(n) because we process each character once.
Space complexity: O(n) in the worst case because the stack may store all opening brackets.
"""


def main():
    solution = Solution()

    input1 = ["1","2","+","3","*","4","-"]

    result = solution.evalRPN(input1)
    print("result: ", result)

main() 