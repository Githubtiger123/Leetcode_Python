# 926. 将字符串翻转到单调递增
# 每日一题,每天提醒自己是傻逼
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        dp = [[0] * 2 for _ in range(n)]

        dp[0][0] = 1 if s[0] == '1' else 0
        dp[0][1] = 1 if s[0] == '0' else 0

        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] + (1 if s[i] == '1' else 0)
            dp[i][1] = min(dp[i - 1][0], dp[i - 1][1]) + (1 if s[i] == '0' else 0)
            # if s[i] == '0':
            #     dp[i][0] = dp[i - 1][0]
            #     dp[i][1] = min(dp[i - 1][0], dp[i - 1][1]) + 1
            # else:
            #     dp[i][0] = dp[i - 1][0] + 1
            #     dp[i][1] = min(dp[i - 1][0], dp[i - 1][1])

        print(dp)

        return min(dp[n - 1])


if __name__ == '__main__':
    s = Solution()
    print(s.minFlipsMonoIncr("010110"))
    print(s.minFlipsMonoIncr("00011000"))
