"""
You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

Each row must contain the digits 1-9 without duplicates.
Each column must contain the digits 1-9 without duplicates.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.

Return true if the Sudoku board is valid, otherwise return false
Note: A board does not need to be full or be solvable to be valid.

Example 1:
Input: board =
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:
Input: board =
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: There are two 1's in the top-left 3x3 sub-box.

Constraints:
board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
"""

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        #check_rows
        for row in board:
            seen = set()

            for num in row:   # num can be dot . so thats y it is not int
                if num == ".":
                    continue
                if num in seen:
                    return False
                seen.add(num)

        #check columns
        for col in range(9):  # it is given sudoku will be 9*9
            seen = set()

            for row in range(9):
                num = board[row][col]

                if num == ".":
                    continue
                if num in seen:
                    return False
                seen.add(num)

        #check 3*3 columns
        for box_row in range(0,9,3):
            for box_col in range(0,9,3):
                seen = set()

                for row in range(box_row, box_row + 3):
                    for col in range(box_col, box_col + 3):
                        num = board[row][col]

                        if num == ".":
                            continue
                        if num in seen:
                            return False
                        seen.add(num)
        """
        Think of the 9*9 board as nine separate 3*3 boxes. The starting row of each box can only be 0, 3, or 6, and the starting column can only be 0, 3, or 6.
        so loop will generate starting point 1st two for loop
        (0,0)  (0,3)  (0,6)
        (3,0)  (3,3)  (3,6)
        (6,0)  (6,3)  (6,6)

        for row in range(0, 3):   # 0, 1, 2
            for col in range(0, 3):   # 0, 1, 2
        
            board[0][0] board[0][1] board[0][2]
            board[1][0] board[1][1] board[1][2]
            board[2][0] board[2][1] board[2][2]

        Then the next box_col becomes 3, so it checks rows 0-2 and columns 3-5, which is the top-middle box. After that box_col = 6, 
        which checks the top-right box. Then box_row becomes 3, and the same process checks the middle three boxes.

        The key thing to remember is: outer two loops choose which 3*3 box to inspect; inner two loops inspect the 9 cells inside that box.
        """
        return True

"""
This question is a little special because Sudoku is always 9*9. 
So technically the work never grows beyond 81 cells, meaning you could call it O(1) time and O(1) space.

But for learning DSA, imagine it was an n * n board. 
Then we examine roughly every cell a few times, so it would be O(n²) time. 
The sets only hold a maximum of 9 numbers in real Sudoku, so space is O(1).
"""

def main():
    solution = Solution()

    input =[["1","2",".",".","3",".",".",".","."],
            ["4",".",".","5",".",".",".",".","."],
            [".","9","8",".",".",".",".",".","3"],
            ["5",".",".",".","6",".",".",".","4"],
            [".",".",".","8",".","3",".",".","5"],
            ["7",".",".",".","2",".",".",".","6"],
            [".",".",".",".",".",".","2",".","."],
            [".",".",".","4","1","9",".",".","8"],
            [".",".",".",".","8",".",".","7","9"]]
    
    result = solution.isValidSudoku(input)
    print("result: ", result)

main()