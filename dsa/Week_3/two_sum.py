"""
Given an array of integers numbers that is sorted in non-decreasing order.
Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. 
Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.
There will always be exactly one valid solution.

Your solution must use O(1) additional space.

Example 1:
Input: numbers = [1,2,3,4], target = 3
Output: [1,2]
Explanation: The sum of 1 and 2 is 3. Since we are assuming a 1-indexed array, index1 = 1, index2 = 2. We return [1, 2].

Constraints:
2 <= numbers.length <= 30000
-1000 <= numbers[i] <= 1000
-1000 <= target <= 1000
"""

class Solution_V1:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        stored = []
        result = []

        for num in numbers:
            remainder = target - num

            if remainder in stored:
                result.append(stored.index(remainder)+1)
                result.append(numbers.index(num)+1)
            stored.append(num)

        return result

    """
    stored list makes the space O(n), and if remainder in stored is also O(n), 
    so the overall time can become O(n²). Since the array is sorted, 
    this is a classic Two Pointers problem. better version is below
    """

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            """
            array is sorted so left should be less than right, if it goes above that means something is wrong in list or code
            number for the first lets say array [1,2,3,4,7,8,9] and target is 6 
            current sum will be 10
            """
            if current_sum == target:
                return [left + 1, right + 1]

            elif current_sum > target:
                right -= 1

            else:
                left += 1

            """
            now according to above example sum is 10 so we reduce the right index by 1
            hence now current sum is 1+8 = 9 still greater we keep on it till it achieve target or become less than target
            so 1+4 = 5 which is less than target so we do not reduce the right now
            we add 1 to left index hence it becomes 2+4 = 6 and target achieved.
            """
            
"""
Time complexity: O(n) because each pointer moves inward at most n times total. 
Space complexity: O(1) because we only use left, right, and current_sum.
"""

def main():
    solution = Solution()

    input = [2,3,4]
    target = 6

    result = solution.twoSum(input, target)
    print("result: ", result)

main()    