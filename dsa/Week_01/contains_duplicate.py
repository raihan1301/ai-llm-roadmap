"""
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:
Input: nums = [1, 2, 3, 3]
Output: true

Example 2:
Input: nums = [1, 2, 3, 4]
Output: false

constraints:
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""

class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        seen = set() # we create empty set and it will store all the seen variables

        for num in nums:  # this will directly give the value of list not index
            if num in seen:  # do not use is, is means equal num == seen but use in means that number is inside seen or not
                return True   # return true if its in seen

            seen.add(num)  # add the num in set if not exist

        return False  # return false if no duplicate exist


def main():
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))

    """
    input("Enter numbers separated by spaces: ") reads the user’s input as one string, such as "1 2 3 3". .split() separates that string 
    at spaces and produces ["1", "2", "3", "3"]. map(int, ...) converts each string into an integer, producing 1, 2, 3, 3. 
    Finally, list(...) collects those integers into the list [1, 2, 3, 3].
    """

    solution = Solution()
    result = solution.hasDuplicate(nums)

    print(result)

if __name__ == "__main__":
    main()


"""
To determine time complexity, count how the amount of work grows as the input size n grows. 
In the set solution, the loop visits each number once, and checking or adding an item to a set is normally O(1), so n operations × O(1) gives O(n) time. 
The set may store all n numbers when there are no duplicates, so it requires O(n) space. 

Your previous solution has one loop inside another loop: for each number, it compares that number with most of the remaining numbers. 
The total comparisons are approximately n × n, so its time complexity is O(n²). 
It only uses a few variables and does not create another collection based on the input size, so its extra space complexity is O(1).

"""
