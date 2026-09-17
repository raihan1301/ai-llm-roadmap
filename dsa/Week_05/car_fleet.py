"""
There are n cars traveling to the same destination on a one-lane highway.
You are given two arrays of integers position and speed, both of length n.

position[i] is the position of the ith car (in miles)
speed[i] is the speed of the ith car (in miles per hour)

The destination is at position target miles.
A car can not pass another car ahead of it. It can only catch up to another car and then drive at the same speed as the car ahead of it.

A car fleet is a non-empty set of cars driving at the same position and same speed. A single car is also considered a car fleet.
If a car catches up to a car fleet the moment the fleet reaches the destination, then the car is considered to be part of the fleet.

Return the number of different car fleets that will arrive at the destination.

Example 1:
Input: target = 10, position = [1,4], speed = [3,2]
Output: 1
Explanation: The cars starting at 1 (speed 3) and 4 (speed 2) become a fleet, meeting each other at 10, the destination.

Example 2:
Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]
Output: 3
Explanation: The cars starting at 4 and 7 become a fleet at position 10. The cars starting at 1 and 0 never catch up to the car ahead of them. 
Thus, there are 3 car fleets that will arrive at the destination.

Constraints:
n == position.length == speed.length.
1 <= n <= 100,000
0 < target <= 1,000,000
1 <= speed[i] <= 1,000,000
0 <= position[i] < target
All the values of position are unique.

IMP tip : we have to count fleets, we do not care how many cars are there in each fleet
"""

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:

        stack = []
        cars = list(zip(position, speed))
        """
        position = [4, 1, 0, 7]
        speed = [2, 2, 1, 1]
        so this will give [(4, 2), (1, 2), (0, 1), (7, 1)]
        """

        cars.sort(reverse=True)
        """
        sort the cars based on position so 7 will be top
        """

        for pos, spd in cars:
            time = (target - pos) / spd

            stack.append(time)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                """
                because if the time of last one is less than the last second one, 
                this car already going to catch up to the last second one
                """
                stack.pop()
                """
                so we remove the last value
                """

            """
            (7,1) → time 3
            (4,2) → time 3
            (1,2) → time 4.5
            (0,1) → time 10

            3      → [3]
            3      → [3, 3] → new time <= previous time → merge → [3]
            4.5    → [3, 4.5]
            10     → [3, 4.5, 10]
            """
        return len(stack)

"""
We first combine each car's position and speed, then sort the cars from the one closest to the destination to the one farthest away. 
For each car, we calculate its arrival time using (target - position) / speed and push that time onto the stack. 
If the new car behind would arrive earlier than or at the same time as the fleet ahead, 
it must catch that fleet before or at the destination, so it becomes part of that fleet and we remove its separate time from the stack. 
In the end, each remaining time in the stack represents one car fleet.
"""

"""
Time complexity: O(n log n) because of sorting.
Space complexity: O(n) because of the cars list and stack.
"""

class Solution_v2: 
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # Step 1: pair each car with its time to reach the target
        cars = sorted(zip(position, speed), reverse=True)  # closest to target first

        stack = []  # each entry = the arrival time of a fleet

        for pos, spd in cars:
            time = (target - pos) / spd
            # if this car is slower than the fleet currently in front (top of stack),
            # it can't catch up — it's a brand new fleet, push its time
            if not stack or time > stack[-1]:
                stack.append(time)
            # else: it would catch the fleet ahead before the target,
            # so it merges — do nothing, its time is irrelevant now

        return len(stack)


def main():
    solution = Solution()

    target = 10
    position = [4,1,0,7] 
    speed = [2,2,1,1]

    result = solution.carFleet(target, position, speed)
    print("result: ", result)

main() 