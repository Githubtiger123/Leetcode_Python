# LCR 166. 珠宝的最高价值
from functools import cache
from typing import List


class Solution:

    def jewelleryValue1(self, frame: List[List[int]]) -> int:

        @cache
        def dfs(i, j):
            if i < 0 or j < 0:
                return 0
            if i == 0 and j == 0:
                return frame[0][0]

            return max(dfs(i - 1, j), dfs(i, j - 1)) + frame[i][j]

        return dfs(len(frame) - 1, len(frame[0]) - 1)

    def jewelleryValue(self, frame: List[List[int]]) -> int:

        n = len(frame)
        m = len(frame[0])
        dp = [[0] * m for _ in range(n)]
        dp[0][0] = frame[0][0]
        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] + frame[i][0]
        for j in range(1, m):
            dp[0][j] = dp[0][j - 1] + frame[0][j]

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + frame[i][j]

        return dp[n - 1][m - 1]


if __name__ == '__main__':
    s = Solution()
    print(s.jewelleryValue([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
