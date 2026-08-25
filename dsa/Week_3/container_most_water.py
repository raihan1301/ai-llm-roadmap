"""
You are given an integer array heights where heights[i] represents the height of the 
ith bar.
You may choose any two bars to form a container. Return the maximum amount of water a container can store.

Example1:
Input: height = [1,7,2,5,4,7,3,6]
Output: 36

Example 2:
Input: height = [2,2,2]
Output: 4

Constraints:
2 <= height.length <= 100,000
0 <= height[i] <= 10,000
"""

class Solution:
    def maxArea(self, heights: list[int]) -> int:
        """
        I am thinking of using two pointer so if left is small move that or if right is small decrement it
        """
        area = 0
        left = 0
        right = len(heights) - 1

        while left < right:

            if heights[left] > heights[right]:
                container_height = heights[right]
            else:
                container_height = heights[left]

            container_width = right - left          

            temp_area = container_height * container_width

            if temp_area > area:
                area = temp_area

            if heights[left] > heights[right]:
                right -= 1
            else:
                left = left + 1

        return area

    """
    Time complexity: O(n) because left and right only move inward and each moves at most n times. 
    Space complexity: O(1) because we only use a few variables.
    """

def main():
    solution = Solution()

    height = [1,7,2,5,4,7,3,6]

    result = solution.maxArea(height)
    print("result: ", result)

main()  