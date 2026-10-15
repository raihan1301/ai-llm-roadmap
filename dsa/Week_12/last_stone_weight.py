"""
You are given an array of integers stones where stones[i] represents the weight of the ith stone.

We want to run a simulation on the stones as follows:
At each step we choose the two heaviest stones, with weight x and y and smash them togethers
If x == y, both stones are destroyed
If x < y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
Continue the simulation until there is no more than one stone remaining.

Return the weight of the last remaining stone or return 0 if none remain.

Example 1:
Input: stones = [2,3,6,2,4]
Output: 1
Explanation:
We smash 6 and 4 and are left with a 2, so the array becomes [2,3,2,2].
We smash 3 and 2 and are left with a 1, so the array becomes [1,2,2].
We smash 2 and 2, so the array becomes [1].

Example 2:
Input: stones = [1,2]
Output: 1

Constraints:
1 <= stones.length <= 20
1 <= stones[i] <= 100
"""

"""
Simple Solution but it is slow one.
1. Sort from smallest → largest.
2. Remove the two largest stones.
3. Smash them.
4. If they are different, append the difference.
5. Sort again.
6. Continue until only one stone remains.
"""
class Solution_V2:
    def lastStoneWeight(self, stones: list[int]) -> int:

        while len(stones) > 1:
            stones.sort()

            x = stones.pop()
            y = stones.pop()

            if x != y:
                stones.append(x - y)

        if stones:
            return stones[0]

        else:
            return 0
"""
Time Complexity: O(n² log n)
Space Complexity: O(1) auxiliary space
"""


"""
We can use Heap Solution to Solve this
"""
import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:

        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        """
        creating min heap python
        where lowest number is always first
        """

        while len(stones) > 1:
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)

            if x != y :
                heapq.heappush(stones, -(x-y))

        if stones:
            return -stones[0]
        else:
            return 0

"""
For the heapq solution, we first convert every stone to a negative number because Python's heapq is a min-heap, 
while this problem needs the two largest stones repeatedly. So [2,3,6,2,4] becomes [-2,-3,-6,-2,-4], and after heapify(), 
the most negative value (-6) is at the top, which represents the largest original stone 6. 
Each loop uses heappop() twice to get the two heaviest stones, changes them back to positive using -, compares them, 
and if they are different pushes the negative difference back into the heap. The loop continues until at most one stone remains.
"""

"""
For stones = [2,3,6,2,4], after converting to negatives and heapifying, the first two pops give -6 and -4, 
which become x = 6 and y = 4. Their difference is 2, so we push -2. The next two largest stones are 3 and 2, producing 1, so we push -1. 
Then the next two largest are 2 and 2; since they are equal, both disappear and nothing is pushed. Only 1 remains, so we return 1.
"""

"""
Time Complexity: O(n log n) because heapify() is O(n), and each pop/push operation is O(log n).

Space Complexity: O(n) because we create the negative heap list.
"""

def main():
    stones = [2,3,6,2,4]

    solution = Solution()
    Last_Stone_Weight = solution.lastStoneWeight(stones)
    
    print("Last Stone Weight :", Last_Stone_Weight)


if __name__ == "__main__":
    main()
    