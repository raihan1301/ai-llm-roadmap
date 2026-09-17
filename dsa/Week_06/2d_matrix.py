"""
You are given an m x n 2-D integer array matrix and an integer target.

Each row in matrix is sorted in non-decreasing order.
The first integer of every row is greater than the last integer of the previous row.
Return true if target exists within matrix or false otherwise.

Can you write a solution that runs in O(log(m * n)) time?

Example 1:
Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10
Output: true

Example 2:
Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15
Output: false

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10000 <= matrix[i][j], target <= 10000
"""

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        rows = len(matrix)
        columns = len(matrix[0])

        left = 0
        right = (rows * columns) - 1

        """
        lets take an example of [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 11
        rows = 3, columns = 4, left = 0, right = 11 (which is the last row last column)
        """
        
        while left <= right:
            middle = (left + right) // 2 
            row = middle // columns
            column = middle % columns  
            """
            middle = (0+11)//2 = 5 , row = 5//4 = 1, column = 5%4 = 1
            middle = (6+11)//2 = 8, row = 8//4 = 2, column = 8%4 = 0
            middle = (6+7)//2 = 6, row = 6//4 = 1, column = 6%4 = 2
            """

            value = matrix[row][column]    
            """
            value = 10
            value = matrix[2][0] = 14
            value = matrix[1][2] = 11
            """    

            if value == target:
                """
                value and target is 11 hence it is true
                """
                return True

            elif value < target:
                left = middle + 1
                """
                10 < 11, left = 6
                """

            else:
                right = middle - 1
                """
                14 > 11, right = 8-1 = 7
                """

        return False

"""
We first get the number of rows and columns, then treat the entire 2D matrix as if it were one long sorted array. 
left starts at index 0 and right at the last imaginary flattened index. Each loop calculates middle, 
converts that index back into a real row and column using // and %, and compares that matrix value with the target. 
If the value is too small, we discard the left half; if it is too large, we discard the right half. If the target is never found, 
we return False.
"""
"""
Time Complexity: O(log(m * n)) — each iteration eliminates half of all remaining matrix elements.
Space Complexity: O(1) — we only use a few variables regardless of matrix size.
"""


def main():
    solution = Solution()

    input1 = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
    target = 11

    result = solution.searchMatrix(input1, target)
    print("result: ", result)

main() 