# 664. 奇怪的打印机
import math


class Solution:
    def strangePrinter1(self, s: str) -> int:
        n = len(s)
        memo = [[-1] * n for _ in range(n)]
        return self.dfs(s, 0, len(s) - 1, memo)

    # 方式二:记忆化搜索
    def dfs(self, s: str, start: int, end: int, memo: list[[]]) -> int:

        if memo[start][end] != -1:
            return memo[start][end]
        ans = 0

        if start == end:
            ans = 1
        elif start + 1 == end:
            ans = 1 if s[start] == s[end] else 2
        elif s[start] == s[end]:
            ans = self.dfs(s, start, end - 1, memo)
        else:

            ans = float('inf')
            for i in range(start, end):  # range是左闭右开的end不能-1
                t = self.dfs(s, start, i, memo) + self.dfs(s, i + 1, end, memo)
                ans = min(ans, t)

        memo[start][end] = ans
        return ans

    # 为什么不行
    # def dfs(self, s: str, start: int, end: int) -> int:
    #     if start > end:
    #         return 0
    #     elif start == end:
    #         return 1
    #     elif start + 1 == end:
    #         return 1 if s[start] == s[end] else 2
    #     elif s[start] == s[end]:
    #         return self.dfs(s, start, end - 1)
    #     else:
    #         l: int = start + 1
    #         r: int = end - 1
    #         while s[l - 1] == s[l]:
    #             l += 1
    #         while s[r + 1] == s[r]:
    #             r -= 1
    #
    #         return min(self.dfs(s, start, r), self.dfs(s, l, end)) + 1

    # 方式三:二位动态规划
    def strangePrinter(self, s: str) -> int:

        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for k in range(n):
            start = 0
            end = k
            while start < n and end < n:
                if start == end:
                    ans = 1
                elif start + 1 == end:
                    ans = 1 if s[start] == s[end] else 2
                elif s[start] == s[end]:
                    ans = dp[start][end - 1]
                else:

                    ans = float('inf')
                    for i in range(start, end):  # range是左闭右开的end不能-1
                        t = dp[start][i] + dp[i + 1][end]
                        ans = min(ans, t)

                dp[start][end] = ans
                start += 1
                end += 1
        return dp[0][n - 1]


if __name__ == '__main__':
    s = Solution()
    print(s.strangePrinter("AAB"))
    print(s.strangePrinter("RGBGR"))
    print(s.strangePrinter("aaaabbbb"))
    print(s.strangePrinter("baacdddaaddaaaaccbddbcabdaabdbbcdcbbbacbddcabcaaa"))
