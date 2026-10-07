"""
You are given an array of integers heights where heights[i] represents the height of a bar. The width of each bar is 1.
Return the area of the largest rectangle that can be formed among the bars.

Example 1:
Input: heights = [7,1,7,2,2,4]
Output: 8

Example 2:
Input: heights = [1,3,7]
Output: 7

Constraints:
1 <= heights.length <= 100,000.
0 <= heights[i] <= 10,000
"""

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:

        stack = []
        max_area = 0

        for i, height in enumerate(heights):
            start = i 
            """
            as we have to find the next short bar because than rectangle height will be capped at that, example = [7,1,7,2,2,4]
            """
            """
            start = 0, stack is empty not going inside
            start = 1, stack[-1] means (0,7) and stack[-1][1] means 2nd value from (0,7) which is 7 > height (1), so we go inside
            """
            while stack and stack[-1][1] > height:
                index, previous_height = stack.pop()
                """
                so we stored the index = 0 and previous height = 7 , stack is empty again
                """

                width = i - index
                area = previous_height * width
                """
                width = 1 - 0 = 1, area = 7 * 1 = 7
                """

                max_area = max(max_area, area)
                start = index
                """
                max area (0,7) = 7, start = 0
                """


            stack.append((start, height))
            """
            here we append stack with the bar index and height so,
            (0, 7)
            (0, 1)
            """

        while stack:
            index, height = stack.pop()

            width = len(heights) - index
            area = height * width
            max_area = max(max_area, area)

        return max_area
    
"""
We create a stack that stores pairs like (start_index, height). As we move from left to right, 
if the current bar is taller than or equal to the stack top, we keep it because it may extend farther. 
But if the current bar is shorter, then every taller bar on top of the stack has reached its right boundary, 
so we pop it, calculate its rectangle area, and remember how far left that bar had started. 
The shorter current bar can inherit that earlier starting point because it can extend across all those previous taller bars. 
After the main loop finishes, any bars still in the stack can extend all the way to the end, so we calculate those areas too.
"""

"""
Time complexity: O(n) because every bar is pushed once and popped at most once. 
Space complexity: O(n) because the stack can hold up to all bars.
"""

def main():
    solution = Solution()

    input1 = [7,1,7,2,2,4]

    result = solution.largestRectangleArea(input1)
    print("result: ", result)

main() 
