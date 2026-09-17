"""
You are given an array of non-negative integers height which represent an elevation map. 
Each value height[i] represents the height of a bar, which has a width of 1.
Return the maximum area of water that can be trapped between the bars.

Input: height = [0,2,0,3,1,0,1,3,2,1]
Output: 9

Constraints:
1 <= height.length <= 20,000
0 <= height[i] <= 100,000
"""

class Solution_v1:
    def trap(self, height: list[int]) -> int:
        total_water = 0

        for i in range(1, len(height) - 1):
            """
            so we determine the max number in left and right from the i index
            so at i = 0 in this array [0,2,0,3,1,0,1,3,2,1] will be 0,3
            at i = 1, ans will be 2,3
            i= 2 ans will be 2,3
            """
            max_left = max(height[:i])
            max_right = max(height[i+1:])

            """
            now we will check if the water is going to be hold or not
            by taking min of max left and right than minus with current height 
            if the number is greater than 0 that means the water will be hold at that index
            """

            water = min(max_left, max_right) - height[i]
            """
            in i = 0 (0,3) min is 0 and height [0] is also 0 hence 0-0 = 0 so water will not hold
            i = 1 (2,3) min is 2 and height[1] = 2 so it will be 2-2 = 0 water will not hold
            i = 2 (2,3) min is 2 and height[2] = 0 so it will be 2-0 = 2 , greater than 0 so water will hold 2 unit
            """

            if water > 0:
                total_water =  total_water + water

        return total_water
    """
    This version is roughly O(n²) time because for every position we search left and right again. 
    It also creates slices, so it uses additional memory.
    better version is below
    """

class Solution:
    def trap(self, height: list[int]) -> int:

        """
        in this solution we will define the index as left and right
        """
        left = 0
        right = len(height) - 1

        """
        now we take the max number in left from left index and in right from right index
        for right now it will be 0 and 1 respectively for this array [0,2,0,3,1,0,1,3,2,1],
        """
        max_left = height[left]
        max_right = height[right]

        total_water = 0

        while left < right:

            if max_left <= max_right:
                left = left + 1
                """
                here we enter only if max left is smaller and we add 1 to it
                so our example left become 1 because 0< 1
                """     

                max_left = max(max_left, height[left])
                water = max_left - height[left]
                """
                on above lines we take max function of max left and what is the value at index
                left is now 1 , max(0, 2) so result is 2 now height[1] is also 2 
                so water = 2-2 = 0, than we add it in total water
                """
                total_water += water

            else:
                right -= 1
                """
                here we enter only if max left is greater than max right and we decrease 1 to max right
                so our example right become 8
                """  

                max_right = max(max_right, height[right])
                water = max_right - height[right]
                """
                on above lines we take max function of max right and what is the value at index of height[8]
                right is now 8 , max(1, 2) so result is 2 now height[8] is also 2 
                so water = 2-2 = 0, than we add it in total water
                """
                total_water += water

        return total_water

def main():
    solution = Solution()

    height = [0,2,0,3,1,0,1,3,2,1]

    result = solution.trap(height)
    print("result: ", result)

main()  

"""
Time complexity: O(n) because each pointer moves inward only once through the array. 
Space complexity: O(1) because we only store a few variables.

So the key mental picture is not “find two tallest bars and fill everything between them.” 
It is “for each position, ask how high water could rise given the best wall available on its left and right.”
"""