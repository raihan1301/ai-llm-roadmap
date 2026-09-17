"""
You are given an array of integers nums and an integer k. There is a sliding window of size k that starts at the left edge of the array. 
The window slides one position to the right until it reaches the right edge of the array.
Return a list that contains the maximum element in the window at each step.

Example 1: 
Input: nums = [1,2,1,0,4,2,6], k = 3
Output: [2,2,4,4,6]

Explanation:
Window position            Max
---------------           -----
[1  2  1] 0  4  2  6        2
 1 [2  1  0] 4  2  6        2
 1  2 [1  0  4] 2  6        4
 1  2  1 [0  4  2] 6        4
 1  2  1  0 [4  2  6]       6

Constraints:
1 <= nums.length <= 100,000
-10,000 <= nums[i] <= 10,000
1 <= k <= nums.length
"""

from collections import deque

class Solution_v1:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:

        left = 0
        right = k

        max_list = []

        while right <= len(nums):
            sublist = nums[left : right]

            max_value = max(sublist)
            max_list.append(max_value)

            left += 1
            right += 1

        return max_list
    """
    If the window size is k, both slicing and finding max() can take O(k). 
    Since you do that for about n windows, the total becomes roughly O(n x k), which is too slow when n = 100,000.
    """

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        result = []
        queue = deque()
        """
        we can able to have queue = [] empty list and than we can perform pop or pop operation but list will take,
        O(n) because Python has to shift every remaining item one position to the left.

        while deque is a python structure which is advanced and designed to remove from the front and back efficiently 
        deque, popleft() is O(1)

        Memory rule: Need fast removal from the front and back → use deque.
        Normal list is great for the end, but slow when removing from the front.

        here for example [1,2,1,0,4,2,6]
        """

        for right in range(len(nums)):
            """
            right is 0 to 7 because it is range and queue[0]
            right 1, queue[0,0]
            right 2, queue[0,1]
            right 3, queue [0,1,2]
            """

            while queue and nums[queue[-1]] < nums[right]:
                """
                so queue[-1] is also 0, nums[0], 1 < 1, it will not enter
                queue[-1] is 0, nums[0], 1<2, it will enter
                queue[-1] is 1, nums[1], 2<1 , not enter
                queue[-1] is 2, nums[2], 1<0, not enter
                """
                queue.pop()
                """
                so index 0 is removed so now queue become [0]
                """

            queue.append(right)
            """
            so we add 0 in queue hence now it is [0,0]
            add 1 in queue hence now it is [0,1]
            add 2 in queue so [0,1,2]
            add 3 in queue so [0,1,2,3]
            """

            left = right - k + 1
            """
            0-3+1 = -2
            1-3+1 = -1
            2-3+1 = 0
            3-3+1 = 1
            """

            if queue[0] < left:
                queue.popleft()
                """
                0 < -2, so we do not popleft
                0 < -1 no popleft
                0 < 0 no popleft
                0 < 1 , popleft hence queue = [1,2,3]
                """

            if right >= k - 1:
                result.append(nums[queue[0]])
                """
                0 >= 2, hence it will not append to result
                1 >= 2 not append
                2 >= 2 not append
                3 >= 2 so append queue[0] is 1 , nums[1] is 2, result = [2]
                """ 

        return result



def main():
    solution = Solution()

    input1 = [1,2,1,0,4,2,6]
    input2 = 3

    result = solution.maxSlidingWindow(input1, input2)
    print("result: ", result)

main() 