# Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

# A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return
        rows, cols  = len(matrix), len(matrix[0])
        dp = [[float('inf')] * cols for _ in range(rows)]

        for col in range(cols):
            dp[0][col] = matrix[0][col]

        for row in range(1, rows):
            for col in range(cols):
                dp[row][col] = matrix[row][col] + min(dp[row - 1][max(0, col -1)],
                dp[row - 1][col],
                dp[row - 1][min(cols - 1 , col + 1)]
                )
        return min(dp[rows - 1])
    
# Time complexity: O(N^2)
# Space complexity: O(N^2)

