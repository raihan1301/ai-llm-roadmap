"""
You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.
You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.
Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

Example1:
Input: prices = [10,1,5,6,7,1]
Output: 6
Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.

Example2:
Input: prices = [10,8,7,5,2]
Output: 0
Explanation: No profitable transactions can be made, thus the max profit is 0.

Constraints:
1 <= prices.length <= 100
0 <= prices[i] <= 100
"""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0

        left = 0
        right = 1

        """
        Reason we are not using right as last day because the best day to sell can be the next day when you purchase
        so right pointer will next to the left
        """

        while right < len(prices):
            
            if prices[right] > prices[left]:
                """
                this means the next day price is greater as compared to previous day
                hence if we sell we will get profit
                """
                profit = prices[right] - prices[left]

                """
                we than take max from maxprofit or profit 
                """
                max_profit = max(max_profit, profit)

            else:
                left = right
                """
                we move left position ahead to find the next best day of the prices is not more than we bought
                """
            
            right += 1
            """
            we move the right to one more position ahead, to find if we can get more profit
            """   

        return max_profit

"""
Time complexity: O(n) because right moves through the array once. 
Space complexity: O(1) because we only use a few variables.
"""



def main():
    solution = Solution()

    input = [10,1,5,6,7,1]

    result = solution.maxProfit(input)
    print("result: ", result)

main()  