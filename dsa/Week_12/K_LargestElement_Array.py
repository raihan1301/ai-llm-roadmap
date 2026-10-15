"""
Given an unsorted array of integers nums and an integer k, return the kth largest element in the array.
By kth largest element, we mean the kth largest element in the sorted order, not the kth distinct element.
Follow-up: Can you solve it without sorting?

Example 1:
Input: nums = [2,3,1,5,4], k = 2
Output: 4

Example 2:
Input: nums = [2,3,1,1,5,5,4], k = 3
Output: 4

Constraints:
1 <= k <= nums.length <= 10000
-1000 <= nums[i] <= 1000
"""

import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        result = []

        nums = [-num for num in nums]

        heapq.heapify(nums)

        for i in range(k):
            result.append(heapq.heappop(nums))
        
        return -result[k-1]
"""
We first convert every number into its negative version because Python's heapq gives us a min-heap, but this problem needs the largest values first. 
For example, 5 becomes -5, and because -5 is smaller than -4, it will come out of the min-heap before -4. 
After converting the numbers, heapq.heapify(nums) rearranges the list into a valid heap. Then we pop from the heap exactly k times. 
The first pop represents the largest original number, the second pop represents the second largest, and so on. 
We keep replacing result with the value we popped. After the kth pop, result contains the negative version of the kth largest value, 
so we return -result.
"""
"""
For nums = [2,3,1,1,5,5,4] and k = 3, we first convert the numbers to [-2,-3,-1,-1,-5,-5,-4]. 
After heapify(), the heap is arranged so that the smallest negative value, representing the largest original number, is at the top. 
On the first loop, heappop() removes -5, so result = -5, representing the largest value 5. On the second loop, another -5 is removed, 
so the second largest value is also 5. On the third loop, heappop() removes -4, so result = -4. The loop ends because we have popped k = 3 times, 
and we return -(-4) = 4.
"""
"""
Time Complexity: O(n + k log n)
heapify() takes O(n), and we perform k heap pops, each costing O(log n).

Space Complexity: O(n)
We create a new list of negative values for all n elements.
"""

def main():
    nums=[2,3,1,5,4]
    k = 2

    solution = Solution()
    Largest_Element = solution.findKthLargest(nums, k)
    
    print("Largest Element :", Largest_Element)


if __name__ == "__main__":
    main()
    