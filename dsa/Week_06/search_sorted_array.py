"""
You are given an array of length n which was originally sorted in ascending order. 
It has now been rotated between 1 and n times. 

For example, the array nums = [1,2,3,4,5,6] might become:
[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.
Given the rotated sorted array nums and an integer target, return the index of target within nums, or -1 if it is not present.

You may assume all elements in the sorted rotated array nums are unique,
A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?

Example 1:
Input: nums = [3,4,5,6,1,2], target = 1
Output: 4

Example 2:
Input: nums = [3,5,6,0,1,2], target = 4
Output: -1

Constraints:
1 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
-1000 <= target <= 1000

All values of nums are unique. nums is an ascending array that is possibly rotated.
"""

class Solution:
    def search(self, nums: list[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target:
                return middle

            if nums[left] <= nums[middle]:
                """
                it means the target will be on left side
                """
                if nums[left] <= target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1

            else:
                """
                if it does not went above means target is on right side of half
                """
                if nums[middle] < target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1

        return -1

"""
We create left and right and repeatedly calculate the middle. Since the array is rotated, one side of middle must still be normally sorted. 
First we check whether the left half is sorted using nums[left] <= nums[middle]. 
If it is, we check whether the target falls inside that sorted range; if yes, we search left, otherwise right. 
If the left half is not sorted, then the right half must be sorted, so we check whether the target belongs there and 
move the boundaries accordingly. Every loop removes half of the remaining search space, and if we find the target we return its index; 
otherwise we return -1.
"""

"""
Time Complexity: O(log n) — each iteration removes about half of the remaining array.

Space Complexity: O(1) — we only use left, right, and middle.
"""

def main():
    solution = Solution()

    input1 = [4,5,6,7,0,1,2]
    target = 0

    result = solution.search(input1, target)
    print("result: ", result)

main() 
