# 935. 骑士拨号器
from functools import cache

MOD = 1000000007


class Solution:
    def knightDialer1(self, n: int):
        nums = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['*', '0', '#']]

        @cache
        def dfs(i, j, step):
            if i > 3 or i < 0 or j > 2 or j < 0 or nums[i][j] == '*' or nums[i][j] == '#':
                return 0
            if step <= 0:
                return 1
            s = 0
            s += dfs(i + 2, j - 1, step - 1)
            s += dfs(i + 2, j + 1, step - 1)
            s += dfs(i - 2, j - 1, step - 1)
            s += dfs(i - 2, j + 1, step - 1)
            s += dfs(i + 1, j - 2, step - 1)
            s += dfs(i + 1, j + 2, step - 1)
            s += dfs(i - 1, j - 2, step - 1)
            s += dfs(i - 1, j + 2, step - 1)
            return s % MOD

        ans = 0

        for i in range(4):
            for j in range(3):
                ans += dfs(i, j, n - 1)
                ans %= MOD

        return ans

    def knightDialer2(self, n: int):

        moves = {
            0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9],
            5: [],  # 5号按键没有可以直接到达的下一步
            6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4]
        }

        @cache
        def dfs(step, num):
            if step == 1:
                return 1

            ans = 0
            for next_num in moves[num]:
                ans += dfs(step - 1, next_num)
                ans %= MOD

            return ans

        total = 0
        for num in range(10):
            total += dfs(n, num)
            total %= MOD

        return total

    def knightDialer(self, n: int):
        moves = {
            0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9],
            5: [],  # 5号按键没有可以直接到达的下一步
            6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4]
        }

        dp = [[0] * 10 for _ in range(n + 1)]

        for num in range(10):
            dp[1][num] = 1

        for step in range(2, n + 1):
            for num in range(10):
                for next_num in moves[num]:
                    dp[step][num] += dp[step - 1][next_num]
                    dp[step][num] %= MOD

        return sum(dp[n]) % MOD


if __name__ == '__main__':
    s = Solution()

    print(s.knightDialer(1))
