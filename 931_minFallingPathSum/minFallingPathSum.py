from typing import List
# Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

# A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return
        rows, cols  = len(matrix), len(matrix[0])
        min_sum = float('inf')

        def dfs(row: int, col: int, curr_sum: int) -> None:
            nonlocal min_sum
            if row == rows:
                min_sum = min(min_sum, curr_sum)
                return
            if col >= 0 and col < cols:
                dfs(row + 1, col - 1, curr_sum + matrix[row][col])
                dfs(row + 1, col, curr_sum + matrix[row][col])
                dfs(row + 1, col + 1, curr_sum + matrix[row][col])

        for col in range(cols):
            dfs(0, col, 0)

        return min_sum
    
# Time complexity: O(N^2)
# Space complexity: O(N^2)


