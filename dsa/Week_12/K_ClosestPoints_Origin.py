"""
You are given an 2-D array points where points[i] = [xi, yi] represents the coordinates of a point on an X-Y axis plane. 
You are also given an integer k.
Return the k closest points to the origin (0, 0).

The distance between two points is defined as the Euclidean distance (sqrt((x1 - x2)^2 + (y1 - y2)^2)).
You may return the answer in any order. The answer is guaranteed to be unique(except for the order in which the points are returned.)

Example 1:
Input: points = [[0,2],[2,2]], k = 1
Output: [[0,2]]
Explanation : The distance between (0, 2) and the origin (0, 0) is 2. The distance between (2, 2) and the origin is sqrt(2^2 + 2^2) = 2.82842. 
So the closest point to the origin is (0, 2).

Example 2:
Input: points = [[0,2],[2,0],[2,2]], k = 2
Output: [[0,2],[2,0]]
Explanation: The output [2,0],[0,2] would also be accepted.

Constraints:
1 <= k <= points.length <= 1000
-100 <= points[i][0], points[i][1] <= 100
"""

"""
First let look into easy solution without heap
calculate the distance for every point, store [distance, x, y], sort by distance, and return the first k. 
After that, I’ll show the Heap version because Heap is the Week 12 pattern.
"""
class Solution_V2:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        distances = []

        for x,y in points:
            distance = (x * x) + (y * y)
            """
            origin is 0,0 so it will be x^2 + y^2
            """

            distances.append([distance, x, y])

        distances.sort()

        result = []

        for i in range(k):
            distance, x, y = distances[i]
            result.append([x,y])

        return result
"""
Code Explanation :We create distances to store every point together with its distance from (0,0). Inside the for loop, x and y come from each point. 
We calculate x² + y²; we do not need sqrt() because if one squared distance is smaller than another, its actual distance is also smaller. 
We store [distance, x, y] in distances. After every point has been processed, we sort distances, so the smallest distances come first. 
We then run another loop k times, take the first k points, put only [x,y] into result, and return it.
"""
"""
Time Complexity: O(n log n)
We calculate all distances in O(n), but sorting the n points costs O(n log n).

Space Complexity: O(n)
We store all points and their distances in another list.
"""


"""
Now we will use Heap to make solution better and faster
"""
import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        min_heap = []

        for x,y in points:
            distance = (x * x) + (y * y)

            heapq.heappush(min_heap, (distance, x, y))
            """
            push the tuple (distance, x, y) into the heap
            Python's heap always keeps the smallest first value at the top
            """

        result = []

        for i in range(k):
            distance, x, y = heapq.heappop(min_heap)
            result.append([x,y])

        return result
"""
We create an empty min_heap. For every [x,y], we calculate distance = x² + y² and push the tuple (distance, x, y) into the heap. 
Python's heap always keeps the smallest first value at the top, so the point with the smallest distance will always be removed first. 
After all points are inserted, we call heappop() exactly k times. Each pop gives us the currently closest point, and we add [x,y] to result.
"""
"""
For points = [[0,2],[2,0],[2,2]] and k = 2, min_heap starts empty. For [0,2], the distance is 4, so we push (4,0,2). 
For [2,0], the distance is 4, so we push (4,2,0). For [2,2], the distance is 8, so we push (8,2,2). Now we need two points. 
The first heappop() removes (4,0,2), so [0,2] goes into result. The second heappop() removes (4,2,0), so [2,0] is added. 
We have collected k = 2 points, so we return [[0,2],[2,0]].
"""
"""
Time Complexity: O(n log n) with this simple push-every-point version.

Space Complexity: O(n) because the heap stores all points.
"""

def main():
    points = [[0,2],[2,0],[2,2]] 
    k = 2

    solution = Solution()
    Closest_points = solution.kClosest(points, k)
    
    print("Closet Points from Origin :", Closest_points)

  
if __name__ == "__main__":
    main()