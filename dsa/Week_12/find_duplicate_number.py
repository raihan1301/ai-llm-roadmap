"""
You are given an array of integers nums containing n + 1 integers. Each integer in nums is in the range [1, n] inclusive.
There is exactly one repeated integer in nums, and every other integer appears at most once.
Return the repeated integer.

Example 1:
Input: nums = [1,2,3,2,2]
Output: 2

Example 2:
Input: nums = [1,2,3,4,4]
Output: 4

Follow-up: Can you solve the problem without modifying the array nums and using O(1) extra space?

Constraints:
1 <= n <= 10,000
nums.length == n + 1
1 <= nums[i] <= n
"""

class Solution_V2:
    def findDuplicate(self, nums: list[int]) -> int:
        seen = set()

        for num in nums:
            if num in seen:
                return num
            seen.add(num)
"""
Code Explanation : We create an empty set called seen. Then we loop through every num in nums. If num is already inside seen, 
that means we have encountered it before, so it must be the duplicate and we immediately return it. Otherwise, we add the number to seen and continue. 
A set is better than a list here because checking num in seen is O(1) on average.
"""
"""
For nums = [1,2,3,2,2], seen starts as {}. The first number is 1; it is not in seen, so we add it and seen = {1}. Next num = 2; 
it is not there, so seen = {1,2}. Next num = 3; we add it, so seen = {1,2,3}. Next num = 2; this time 2 in seen is True, so we immediately return 2.
"""
"""
Time Complexity: O(n)
We visit every number once, and set lookup is O(1) average.

Space Complexity: O(n)
The set may store up to n values.
"""

"""
But the solution is asked to use O(1) space, so better solution is below
"""
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
"""
We treat the array like a linked list: each index points to another index using its value. 
For example, if nums[1] = 3, imagine index 1 pointing to index 3. Because there are n + 1 positions but values only from 1 to n, one value must repeat, 
which creates a cycle. slow moves one step using nums[slow], while fast moves two steps using nums[nums[fast]]. 
They eventually meet somewhere inside the cycle. Then we reset slow to the beginning and move both pointers one step at a time; 
where they meet again is the entrance to the cycle, which is the duplicate number.
"""
"""
For nums = [1,2,3,2,2], both slow and fast start at nums[0] = 1. First loop: slow = nums[1] = 2, while fast = nums[nums[1]] = nums[2] = 3. 
Next loop: slow = nums[2] = 3, while fast = nums[nums[3]] = nums[2] = 3, so they meet at 3. We reset slow = nums[0] = 1, while fast stays at 3. 
Now slow = nums[1] = 2 and fast = nums[3] = 2. They meet at 2, so we return 2.
"""
"""
Time Complexity: O(n)
Each pointer moves through the array a bounded number of times.

Space Complexity: O(1)
We only use two pointer variables.
"""

def main():
    nums = [1,2,3,2,2]

    solution = Solution()
    Duplicate_Number = solution.findDuplicate(nums)
    
    print("Duplicate Number :", Duplicate_Number)


if __name__ == "__main__":
    main()