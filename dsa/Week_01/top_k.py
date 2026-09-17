"""
Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements within the array.
The test cases are generated such that the answer is always unique.
You may return the output in any order.

Example 1:
Input: nums = [1,2,2,3,3,3], k = 2
Output: [2,3]

Example 2:
Input: nums = [7,7], k = 1
Output: [7]

Constraints :
1 <= nums.length <= 10^4
-1000 <= nums[i] <= 1000
1 <= k <= number of distinct elements in nums
"""

"""
I interpreted question wrong, I belived K means all the number repeating more than k frequesncy should be output
for example if k is 3 then in list all the numbers who repeats 3 times or more should be the output list

correct version is frequency, it means if k is three than in the list what are the 3 most repeated numbers code is below with name class solution
"""

class Solution_v1:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        seen = {}
        output = set()

        for num in nums:
            seen[num] = seen.get(num,0) + 1
            """
            instead of if else you can use this pythonf see line 28
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
            """
            if seen[num] >= k:
                output.add(num)


        return list(output)


"""
correct question code is below
""" 
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        frequency = {}

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        sorted_numbers = sorted(frequency, key=frequency.get, reverse=True)  # parameters are (dict/list, if its dict what is the key to sort other wise it will sort according to keys)
        #frequency.get will tell sort according to value and reverse means big to small
        return sorted_numbers[:k]

"""
We first create an empty dictionary called frequency and loop through every number, 
storing each number as a key and its occurrence count as the value. 
Then we sort the dictionary keys according to their frequency values from highest to lowest. 
Finally, sorted_numbers[:k] returns only the first k most frequent numbers.

The time complexity is O(n log n) because of sorting, and the space complexity is O(n).
"""        


def main():
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
    target = int(input("Enter your Target: "))

    solution = Solution()
    result = solution.topKFrequent(nums, target)
    
    print(result)

if __name__ == "__main__":
    main()


"""
Additional Notes

A loop that processes all n items once is normally O(n). Two nested loops are commonly O(n²) when both loops can run approximately n times. 
However, nested loops are not automatically O(n²); 
for example, if the inner loop always runs exactly 26 times, the complexity is O(26n), which simplifies to O(n).

Sorting n items normally takes O(n log n). In our Top K solution, we technically sort the distinct numbers. 
If there are m distinct numbers, sorting takes O(m log m). 
Since m can be as large as n, we commonly describe the worst case as O(n log n).

Creating a list does not automatically mean O(n) space. It depends on how many items the list can store as the input grows. 
A list containing all n input items uses O(n) space. A result list that always stores exactly two indexes uses O(1) space because its size never grows beyond two.
In Top K Frequent Elements, the returned list uses O(k) space, while the frequency dictionary and sorted list may each store all distinct numbers, 
making the overall auxiliary space O(n) in the worst case.

Space is O(1) when the amount of additional memory does not grow with the input size.

This uses only a few variables regardless of whether nums has 10 elements or one million elements, so the extra space is O(1). 
A fixed-size array of 26 positions for lowercase English letters is also considered O(1) because it always contains exactly 26 entries.

Other common space complexities include O(k) when storing only k results, 
O(log n) for some recursive algorithms, and O(n) when using a dictionary, set, list, or recursion stack that may grow with every input item.
"""



        


