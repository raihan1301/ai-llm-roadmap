"""
You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.
Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day. 
If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.

Example 1:
Input: temperatures = [30,38,30,36,35,40,28]
Output: [1,4,1,2,1,0,0]

Example 2:
Input: temperatures = [22,21,20]
Output: [0,0,0]

Constraints:
1 <= temperatures.length <= 100,000.
1 <= temperatures[i] <= 100

Important TIP : we just have to find the next warmer day than current and save the index, 
there can be more warmer days but we just have to find the immediate one
"""

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        result = [0] * len(temperatures)
        """
        we did this because if there is no warmer days than that current temp it should return 0 for that day
        example = temperatures = [30,38,30,36,35,40,28]
        """

        for i,temp in enumerate(temperatures):

            """
            i = 0 and temp = 30 , not getting in while loop as stack is empty
            i= 1 and temp = 38, stack[-1] =  0, tempratures[0] = 30, 30<38 hence go inside while loop
            i=2, temp = 30 , stack[-1] =  1, tempratures[1] = 38, 38<30, not going inside
            i=3, temp = 36, stack[-1] = 2, temp[2] = 30, 30<36 , we go inside
            """

            while stack and temperatures[stack[-1]] < temp:
                previous_index = stack.pop()
                """
                previous index = 0 , 0 is removed from stack list
                previous index = 2, 2 is removed from stack list
                """
                result[previous_index] = i - previous_index
                """
                result[0] = 1-0 = 1
                result[2] = 3-2 = 1
                """

            stack.append(i)
            """
            now stack contains 0 , [0]
            now stack = [1]
            now stack = [1,2]
            """
        return result

"""
We create result filled with zeros because days that never get a warmer future temperature should stay 0. 
The stack stores indexes, not temperatures. As we move through the array, 
if the current temperature is warmer than the temperature at the index on top of the stack, that previous day has finally found its answer. 
We pop that index and store the number of days between them using i - previous_index. 
We keep doing that while the current temperature is warmer than unresolved previous temperatures, then we add the current index to the stack.
"""

"""
Time complexity: O(n) because each index is pushed once and popped at most once.
Space complexity: O(n) because the stack and result can grow with the input size.
"""


def main():
    solution = Solution()

    input1 = [30,38,30,36,35,40,28]

    result = solution.dailyTemperatures(input1)
    print("result: ", result)

main() 