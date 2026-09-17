"""
You are given an integer array piles where piles[i] is the number of bananas in the ith pile. 
You are also given an integer h, which represents the number of hours you have to eat all the bananas.

You may decide your bananas-per-hour eating rate of k. Each hour, you may choose a pile of bananas and eats k bananas from that pile. 
If the pile has less than k bananas, you may finish eating the pile but you can not eat from another pile in the same hour.

Return the minimum integer k such that you can eat all the bananas within h hours.

Example 1:
Input: piles = [1,4,3,2], h = 9
Output: 2
Explanation: With an eating rate of 2, you can eat the bananas in 6 hours. 
With an eating rate of 1, you would need 10 hours to eat all the bananas (which exceeds h=9), thus the minimum eating rate is 2.

Example 2:
Input: piles = [25,10,23,4], h = 4
Output: 25

Constraints:
1 <= piles.length <= 10,000
piles.length <= h <= 1,000,000,000
1 <= piles[i] <= 1,000,000,000
"""

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left = 1 
        """
        minimum possible speed is 1 banana per hour
        """
        right = max(piles)
        """
        max speed is greatest number in the piles so for this example [1,4,3,2] it is 4
        """
        result = right
        """
        we will keep making this number smaller as found
        """

        while left <= right:
            middle = (left + right) // 2
            """
            (1+4) // 2 = 2
            """
            hours = 0

            for pile in piles:
                hours += (pile + middle - 1) // middle
                """
                here we will calculate how much hours it will take according to middle = 2
                (1 + 2 - 1) // 2 = [1] , (4 + 2 - 1) // 2 = [1,3] like that it will comes [1,3,2,1], total hours will be 7
                """

            if hours <= h:
                """
                7 <= 9, we update the result with middle value so it will be 2 from 4
                """
                result = middle
                right = middle - 1
                """
                now we check if decrease the middle can we able to find the solution with the hours mentioned
                """
            else:
                left = middle + 1
                """
                not in this example, but let say middle is going more than the hour mentioned 
                than we increase the left, which will increase the middle also
                """
        return result

"""
We use Binary Search on the possible eating speed, not on the piles array. The minimum possible speed is 1 banana/hour and the maximum 
needed speed is max(piles). For each middle speed, we loop through every pile and calculate how many hours it would take using ceiling division:
(pile + middle - 1) // middle. If the total hours is within h, that speed works, so we save it and search for an even smaller speed on the left.
If it takes too many hours, the speed is too slow, so we search higher speeds on the right. 
Finally, result contains the minimum valid eating speed.
"""

"""
Time Complexity: O(n log(max(piles))) — Binary Search tests about log(max(piles)) possible speeds, 
    and for every speed we loop through all n piles.

Space Complexity: O(1) — only a few variables are used regardless of the number of piles.
"""

def main():
    solution = Solution()

    input1 = [1,4,3,2]
    target = 9

    result = solution.minEatingSpeed(input1, target)
    print("result: ", result)

main() 