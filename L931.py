# 931. 下降路径最小和
from functools import cache
from typing import List


class Solution:

    def minFallingPathSum1(self, matrix: List[List[int]]) -> int:

        m = len(matrix[0])
        n = len(matrix)

        @cache
        def dfs(i, j):

            if j < 0 or j >= m:
                return float('inf')

            if i == 0:
                return matrix[i][j]
            else:
                return min(dfs(i - 1, j - 1), dfs(i - 1, j - 1), dfs(i - 1, j - 1)) + matrix[i][j]

        ans = float('inf')
        for t in range(m):
            ans = min(dfs(n - 1, t), ans)
        return ans

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        n = len(matrix)
        m = len(matrix[0])
        dp = [[0] * m for _ in range(n)]
        dp[0] = matrix[0]

        for i in range(1, n):
            for j in range(0, m):
                dp[i][j] = dp[i - 1][j]
                if j >= 1:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])
                if j < m - 1:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j + 1])
                dp[i][j] = dp[i][j] + matrix[i][j]
        return min(dp[n - 1])


if __name__ == '__main__':
    s = Solution()
    print(s.minFallingPathSum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]))
    print(s.minFallingPathSum([[1], [2], [3], [4], [5]]))
    print(s.minFallingPathSum([[-80, -13, 22], [83, 94, -5], [73, -48, 61]]))
