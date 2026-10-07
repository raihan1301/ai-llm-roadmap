"""
You are given two integer arrays nums1 and nums2 of size m and n respectively, where each is sorted in ascending order. 
Return the median value among all elements of the two arrays.

Your solution should run in O(log(m+n)) time.

Example 1:
Input: nums1 = [1,2], nums2 = [3]
Output: 2.0
Explanation: Among [1, 2, 3] the median is 2.

Example 2:
Input: nums1 = [1,3], nums2 = [2,4]
Output: 2.5
Explanation: Among [1, 2, 3, 4] the median is (2 + 3) / 2 = 2.5.


Constraints:
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-10^6 <= nums1[i], nums2[i] <= 10^6
"""

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:

        """
        we can take the first index and compare with the second add them in the final list in order
        than we know the total lenght so when middle number hits we return that value or if its even we add middle 2 numbers and return value
        This thinking will take O(m + n) because we are merging two array we need o(lon(m+n))
        """

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        left = 0
        right = m

        while left <= right:
            partition1 = (left + right) //2
            partition2 = (m + n + 1) // 2 - partition1

            max_left1 = float("-inf") if partition1 == 0 else nums1[partition1 - 1]
            min_right1 = float("inf") if partition1 == m else nums1[partition1]

            max_left2 = float("-inf") if partition2 == 0 else nums2[partition2 - 1]
            min_right2 = float("inf") if partition2 == n else nums2[partition2]

            if max_left1 <= min_right2 and max_left2 <= min_right1:
                if (m + n) % 2 == 1:
                    return float(max(max_left1, max_left2))

                return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2

            elif max_left1 > min_right2:
                right = partition1 - 1

            else:
                left = partition1 + 1
"""
Instead of actually merging the arrays, we try to split both arrays into a left half and a right half 
so that the combined left side contains half of all elements. 
We Binary Search where to split the smaller array, and from that split we calculate where the second array must be split. 
A valid split means every value on the combined left side is less than or equal to every value on the combined right side. 
Once that condition is true, the median must sit exactly at the boundary: 
for an odd number of values, it is the largest value on the left; 
for an even number, it is the average of the largest left value and smallest right value.
"""
"""
For nums1 = [1,3] and nums2 = [2,4], we can split them as [1] | [3] and [2] | [4]. 
The combined left side is [1,2] and the combined right side is [3,4]. 
The largest value on the left is 2, and the smallest value on the right is 3. Since there are four total numbers, 
the median is (2 + 3) / 2 = 2.5. The code uses Binary Search to find this correct partition without ever building [1,2,3,4].
"""
"""
Time Complexity: O(log(min(m, n))) — we only Binary Search the smaller array.
Space Complexity: O(1) — no merged array is created.
"""

"""
Below example does the same bu tin O(m+n)
"""
class Solution_v2:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged = []

        i = 0
        j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        while i < len(nums1):
            merged.append(nums1[i])
            i += 1

        while j < len(nums2):
            merged.append(nums2[j])
            j += 1

        length = len(merged)
        middle = length // 2

        if length % 2 == 1:
            return float(merged[middle])

        return (merged[middle - 1] + merged[middle]) / 2
"""
We use two pointers i and j to compare the current values from both sorted arrays. 
Whichever value is smaller gets added to merged, and that pointer moves forward. 
When one array finishes, we append the remaining values from the other array. 
Then if the merged length is odd, we return the middle element; if it is even, we average the two middle elements. 
"""
"""
Example : 
For nums1 = [1,3] and nums2 = [2,4], we first compare 1 and 2, so merged = [1]; then compare 3 and 2, giving [1,2]; 
then compare 3 and 4, giving [1,2,3]; finally 4 remains, so we get [1,2,3,4]. 
The length is 4, so the middle indexes are 1 and 2, containing 2 and 3, and (2 + 3) / 2 = 2.5.
"""
"""
Time Complexity: O(m + n)
Space Complexity: O(m + n)
"""

def main():
    solution = Solution()

    nums1 = [1,3]
    nums2 = [2,4]

    result = solution.findMedianSortedArrays(nums1, nums2)
    print("result: ", result)

main() 