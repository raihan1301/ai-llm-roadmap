"""
You are given an array of distinct integers nums, sorted in ascending order, and an integer target.
Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.

Your solution must run in O(logn) time.

Example 1:
Input: nums = [-1,0,2,4,6,8], target = 4
Output: 3

Example 2:
Input: nums = [-1,0,2,4,6,8], target = 3
Output: -1

Constraints:
1 <= nums.length <= 10000.
-10000 < nums[i], target < 10000
All the integers in nums are unique.
"""

class Solution_V2:
    def search(self, nums: list[int], target: int) -> int:
        middle = len(nums) // 2

        if(nums[middle] == target):
            return middle
        elif(nums[middle] < target):
            while middle < len(nums):
                if nums[middle] == target:
                    return middle
                middle += 1

        else:
            while middle >= 0:
                if nums[middle] == target:
                    return middle
                middle -=1

        return -1
"""
we can use this code but it will create o(n) time complexity which is not good
"""

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        idea is to look in middle and remove them from list as needed
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target:
                return middle

            elif nums[middle] < target:
                left = middle + 1

            else:
                right = middle - 1

        return -1

"""
We create left at the beginning of the list and right at the end. While there is still a valid search range, 
we calculate the middle index. If the middle value is the target, we return its index. 
If the middle value is too small, we move left past the middle and discard the entire left half. If it is too large, 
we move right before the middle and discard the entire right half. If left eventually passes right, the target does not exist, 
so we return -1.
"""

"""
Time: O(log n) : Every comparison removes approximately half of the remaining numbers.
Space: O(1)
"""


def main():
    solution = Solution()

    input1 = [-1,0,2,4,6,8]
    target = 3

    result = solution.search(input1, target)
    print("result: ", result)

main() 
            
