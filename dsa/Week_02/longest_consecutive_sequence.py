"""
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. 
The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [2,20,4,10,3,4,5]
Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Example 2:
Input: nums = [0,3,2,5,4,6,1,1]
Output: 7

Constraints:
0 <= nums.length <= 100,000
-10^9 <= nums[i] <= 10^9
"""

class Solution_V2:
    def longestConsecutive(self, nums: list[int]) -> int:

        if not nums: # no number in list
            return 0
        
        sorted_nums = sorted(set(nums))

        longest = 1
        current_length = 1

        """
        there can be multiple sequence but we need to find the longest one
        """

        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] - sorted_nums[i-1] == 1:
                current_length += 1   
            else:
                current_length = 1

            longest = max(longest, current_length) 

            """
            so in if statement it will keep adding 1 to current length
            than that current length will be updated to longest
            for example for start they will have same number

            but let say now sequence is broken after 2,3,4 and 10 comes
            current lenght become 1 in else statement but now the longest function will remember the long one which is 3
            so in future if any sequence comes which is greater than 3 like 10,11,12,13,14 than longest will be updated to that current length
            """

        return longest
    """
    Time complexity: O(n log n) because sorting is the most expensive operation. 
    The loop itself is only O(n). Space complexity: O(n) because set(nums) and the sorted list can contain up to n elements.
    so better version is below
    """

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numbers = set(nums) # this will remove the duplicate
        longest = 0

        for num in nums:

            # Only start counting if this is the beginning of a sequence
            if num - 1 not in numbers:  
                current = num
                length = 1

                """
                we loop through every number, but we only start counting when num - 1 does not exist, 
                meaning this number is the beginning of a sequence. 
                For example, with 2,3,4,5, only 2 starts the sequence because 1 is missing.

                example:
                nums = [2,20,4,10,3,4,5]  ----> set becomes {2, 3, 4, 5, 10, 20}
                when num = 2 ---> 2-1 = 1 not in set
                so it is possible 2 can be a start for the sequence
                """

                while current + 1 in numbers:
                    current += 1
                    length += 1

                """
                so in loop if 3 is in numbers than sequence continue similary adding the length as well
                3 exists → length 2
                4 exists → length 3
                5 exists → length 4
                6 missing → stop
                """
                longest = max(longest, length)

                """
                so if new sequence starts and length will increase we only keep the max sequence number
                """
        return longest



def main():
    solution = Solution()

    input = [2,20,4,10,3,4,5]
    result = solution.longestConsecutive(input)
    print("result: ", result)

main()