# 1402. 做菜顺序
from typing import List


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        n = len(satisfaction)
        satisfaction.sort()
        sums = [-1] * n
        sums[n - 1] = satisfaction[n - 1]

        index = -1
        for i in range(n - 2, -1, -1):
            sums[i] = satisfaction[i]
            sums[i] += sums[i + 1]
        print(sums)

        dp = [0] * (n)
        dp[n - 1] = satisfaction[n - 1]
        for i in range(n - 2, -1, -1):
            ans = dp[i + 1] + sums[i]
            dp[i] = max(ans, dp[i + 1])

        return max(0, dp[0])


if __name__ == '__main__':
    s = Solution()
    print(s.maxSatisfaction([-1, -8, 0, 5, -9]))
