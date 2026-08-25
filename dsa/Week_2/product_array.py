"""
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].
Each product is guaranteed to fit in a 32-bit integer.

Example 1:
Input: nums = [1,2,4,6]
Output: [48,24,12,8]

Example 2:
Input: nums = [-1,0,1,2,3]
Output: [0,-6,0,0,0]

Constraints:
2 <= nums.length <= 100,000
-30 <= nums[i] <= 30
"""

class Solution_V1:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        result = []

        for i in range(len(nums)):   # range is 4
            product = 1

            for j in range(len(nums)):
                if i != j :
                    product *= nums[j]

            result.append(product)
            
        return result

""""
Code Explanation :
We create an empty result list, then the outer loop selects each index i. For every index, we reset product = 1, 
then the inner loop goes through every index j. If j is not the same position as i, we multiply that number into product. 
After checking all numbers, we append the completed product into result. Finally, we return the full result list.

IMP Notes:
This version is O(n²) time because for every element, we loop through the entire array again. 
The output list takes O(n) space.

For nums containing 100,000 elements, O(n²) is too slow, so NeetCode expects us to improve this to O(n) time
so better version is below
"""

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        result = [1] * len(nums)
        prefix = 1

        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        """
        The idea is to first create a result list filled with 1.
        In the first loop, prefix stores the product of everything to the left of the current index, 
        and we save that into result[i]

        Example : nums = [1, 2, 4, 6]  ---> result = [1, 1, 2, 8]
        index 0 → nothing on left → 1
        index 1 → 1
        index 2 → 1 * 2 = 2
        index 3 → 1 * 2 * 4 = 8
        """

        suffix = 1

        for i in range(len(nums) -1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        """
        range(len(nums) -1, -1, -1) means --> len(nums) is 4, so: range(3, -1, -1) which produces 3,2,1,0
        Remember range(start, stop, step): start at 3, move by -1, and stop before -1. So we visit the array backwards.

        Then the suffix loop multiplies the right-side products:
        suppose after the prefix loop result = [1, 1, 2, 8]
        
        i = 3, nums[i] = 6, result = 8 * 1 , because suffix right now is 1
        now suffix will become = 1 * 6 = 6

        i = 2, nums[i] = 4, result = 2 * 6 = 12, after suffix = 6 * 4 = 24
        """

        return result

def main():
    solution = Solution()

    input = [-1,0,1,2,3]
    result = solution.productExceptSelf(input)
    print("result: ", result)

main()

"""
The order is very important. We use suffix before multiplying it by nums[i], because the answer at index i must exclude nums[i] itself.
That is the whole trick: first loop collects everything on the left; second backward loop collects everything on the right.

Time complexity: O(n) because we loop through the array twice, and O(n) + O(n) simplifies to O(n), not O(n²), 
because the loops are separate rather than nested. Extra space complexity is O(1) if we do not count the required output array, 
because prefix and suffix are just two variables. If you count the output list itself, total space is O(n).

Tip:
when the problem says “for each position, calculate something using all elements except the current one,” 
especially when doing it directly would require nested loops, think prefix + suffix.
"""
