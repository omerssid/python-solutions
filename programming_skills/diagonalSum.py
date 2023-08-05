"""
1572. Matrix Diagonal Sum
Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.
"""

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        cols = len(mat[0])
        for i, row in enumerate(mat):
            for j, num in enumerate(row):
               if i == j or (i+j) == (cols-1):
                   ans += num
        return ans
