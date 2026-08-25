"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, 
and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:
3 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5
"""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        [-1,0,1,2,-1,-4]
        [-4,-1,-1,0,1,2]
        
        """
        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            """
            so if we take above example i will be range for (4) 6-2 = 4
            now if i is 1 it will be -1 not equal to -4 hence it will not go inside
            if i is 2 it will be -1 and i is 1 is also -1 hence we exit this particular loop with continue and go to i = 3
            """

            left = i + 1
            right = len(nums) - 1
            """
            we initialize the index by fixing 1 int i and making remaining 2 as two sum pointer
            left will be 0 +  1 = 1
            right will be 6 - 1 = 5
            """

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                """
                so 1 < 5 hence
                total = num[0] + num[1] + num[2] = -4 + -1 + 2 = -3
                """

                if total < 0:
                    """
                    now total is less than 0 so we increase left position 
                    because it is sorted so if we decrease the right position it will get more smaller number than 0 
                    example = -4 + -1 + 1 = -4 less than compared to -3
                    """
                    left += 1

                elif total > 0:
                    """
                    if total is greater than 0 we decrease the right position
                    example [-2,-1,0,3,5]  now i = 0 it will be -2 + -1 + 5 = 2
                    so if we increase the left it will be become more greater and far from us -2 + 0 + 5 = 3, hence we reduce the right index
                    so -2 + -1 + 3 = 0
                    """
                    right -=1

                else:
                    """
                    if the total is 0 we got our pair and store in result and increment and decrement both index to find next pair
                    """
                    result.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        """
                        here we check if we check [-4,-1,-1,0,1,2]
                        so after updated let say nums[2] == -1 and nums [1] is also -1 we move forward again
                        otherwise it can give same numbers again
                        """
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        """
                        similar explanation to avoid duplicate pairs we decrement right index one more time if both values are same
                        """
                        right -=1

        return result

"""
Time complexity: O(n²). Sorting is O(n log n), but then for each fixed number the two pointers may scan the remaining array, 
giving O(n * n) = O(n²) overall. The two-pointer portion uses O(1) extra working space, excluding the returned answer; 
Python's sorting itself may use additional memory internally.
"""

def main():
    solution = Solution()

    nums = [-1,0,1,2,-1,-4]

    result = solution.threeSum(nums)
    print("result: ", result)

main()   