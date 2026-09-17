"""
You are given an array of length n which was originally sorted in ascending order. 
It has now been rotated between 1 and n times. 

For example, the array nums = [1,2,3,4,5,6] might become:
[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.
Notice that rotating the array 4 times moves the last four elements of the array to the beginning. 
Rotating the array 6 times produces the original array.

Assuming all elements in the rotated sorted array nums are unique, return the minimum element of this array.
A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?


Example 1:
Input: nums = [3,4,5,6,1,2]
Output: 1

Example 2:
Input: nums = [4,5,0,1,2,3]
Output: 0

Example 3:
Input: nums = [4,5,6,7]
Output: 4

Constraints:
1 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
"""

class Solution:
    def findMin(self, nums: list[int]) -> int:

        left = 0
        right = len(nums) - 1

        while left < right:
            middle = (left + right) // 2

            if nums[middle] > nums[right]:
                """
                so if middle value is greater than the right most value it means the minimum value is on the right half side
                so we make left to the middle + 1
                """ 
                left = middle + 1

            else:
                right = middle
                """
                if middle is less than right it mmeans min number is in left half so we make right = middle value
                """

        return nums[left]

"""
We start with left and right covering the whole array and calculate the middle. If nums[middle] is greater than nums[right], 
the rotation point and therefore the minimum must be to the right of middle, so we use left = middle + 1. Otherwise, 
the minimum is either the middle itself or somewhere to its left, so we use right = middle. We specifically do not use middle - 1 here 
because middle itself could be the minimum. Eventually left and right meet at exactly the minimum element, which we return.
"""

"""
Time Complexity: O(log n) — every iteration eliminates roughly half of the remaining search area.
Space Complexity: O(1) — we only store left, right, and middle.
"""

def main():
    solution = Solution()

    input1 = [4,5,6,7,0,1,2]

    result = solution.findMin(input1)
    print("result: ", result)

main() 

