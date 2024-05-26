# 2110. 股票平滑下跌阶段的数目
from typing import List


class Solution:

    def getDescentPeriods2(self, prices: List[int]) -> int:
        n = len(prices)
        con = [0] * n
        con[n - 1] = 0
        for i in range(n - 2, -1, -1):
            if prices[i] - 1 == prices[i + 1]:
                con[i] = con[i + 1] + 1

        dp = [0] * n
        dp[n - 1] = 1
        for i in range(n - 2, -1, -1):
            if prices[i] - 1 == prices[i + 1]:
                dp[i] = dp[i + 1] + 1 + con[i]
            else:
                dp[i] = dp[i + 1] + 1
        return dp[0]

    def getDescentPeriods1(self, prices: List[int]) -> int:
        n = len(prices)
        con = [0] * n
        con[n - 1] = 0

        dp = [0] * n
        dp[n - 1] = 1
        for i in range(n - 2, -1, -1):
            if prices[i] - 1 == prices[i + 1]:
                con[i] = con[i + 1] + 1

            if prices[i] - 1 == prices[i + 1]:
                dp[i] = dp[i + 1] + 1 + con[i]
            else:
                dp[i] = dp[i + 1] + 1
        return dp[0]

    def getDescentPeriods3(self, prices: List[int]) -> int:
        n = len(prices)
        con_pre = 0
        con = 0

        sum_pre = 1
        sum = 1
        for i in range(n - 2, -1, -1):
            if prices[i] - 1 == prices[i + 1]:
                con = con_pre + 1
            else:
                con = 0

            if prices[i] - 1 == prices[i + 1]:
                sum = sum_pre + 1 + con
            else:
                sum = sum_pre + 1

            sum_pre = sum
            con_pre = con
        return sum

    def getDescentPeriods(self, prices: List[int]) -> int:

        n = len(prices)
        if n == 1: return 1
        con = 1
        s = 0
        for i in range(n - 2, -1, -1):
            if prices[i] - 1 == prices[i + 1]:
                con += 1
            else:
                s += ((con + 1) * con) / 2
                con = 1
        if prices[0] - 1 == prices[1]:
            s += ((con + 1) * con) / 2
        else:
            s = s + 1
        return int(s)


if __name__ == '__main__':
    s = Solution()
    print(s.getDescentPeriods([3, 2, 1, 4]))
