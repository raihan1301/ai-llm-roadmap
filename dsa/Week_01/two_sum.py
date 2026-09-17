"""
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
Return the answer with the smaller index first.

Example 1:
Input: 
nums = [3,4,5,6], target = 7
Output: [0,1]
Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

Example 2:
Input: nums = [4,5,6], target = 10
Output: [0,2]

Example 3:
Input: nums = [5,5], target = 10
Output: [0,1]

Constraints:
2 <= nums.length <= 1000
-10,000,000 <= nums[i] <= 10,000,000
-10,000,000 <= target <= 10,000,000
Only one valid answer exists.
"""

#************** Version 1 with O(n2) Complexity *****************************************************#
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        result = []

        for i in range(len(nums)):
            var = nums[i]

            for j in range(i+1, len(nums)):
                sum = nums[j] + var

                if sum == target:
                    result.append(i)
                    result.append(j)
                    return result

def main():
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
    target = int(input("Enter your Target: "))

    solution = Solution()
    result = solution.twoSum(nums, target)
    
    print(result)

if __name__ == "__main__":
    main()

#************** better version *****************************************************#

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}  # empty dict will hold the number as key and its index as value

        for i, num in enumerate(nums):
            needed = target - num  # this will give how much number needed to fulfil the target

            if needed in seen:  # if needed number is in seen key than we got it
                return [seen[needed], i]   # seen[needed] will give the index of that needed number and i is current index

            seen[num] = i  # if above if does not run than we save number as key and i as its value in dict

def main():
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
    target = int(input("Enter your Target: "))

    solution = Solution()
    result = solution.twoSum(nums, target)
    
    print(result)

if __name__ == "__main__":
    main()


"""
For every number, calculate the missing value needed to reach the target. For example, when target = 7 and the current number is 4, the needed value is 3. 
The dictionary lets us check whether 3 was already seen in approximately O(1) time. 
Since we visit each number only once, the total time complexity is O(n). The dictionary may store up to n numbers, so the space complexity is O(n). 
Because the previous index is returned before the current index, the smaller index comes first.

your Version 1 Solution is O(n²) time because the inner loop runs repeatedly for every index. 
Its extra space is actually O(1) because result can only contain two indexes. 
To improve the time complexity, use a dictionary to remember each number and its index while scanning the list once.

"""
