# 2522. 将字符串分割成值不超过 K 的子字符串
from functools import cache


class Solution:
    def minimumPartition1(self, s: str, k: int) -> int:

        n = len(s)

        @cache
        def dfs(index):
            if index == n:
                return 0

            ans = float('inf')
            i = index
            t = ord(s[i]) - ord('0')
            while t <= k:
                i += 1
                ans = min(ans, dfs(i))
                if i >= n:
                    break
                t *= 10
                t += ord(s[i]) - ord('0')

            return ans + 1

        return -1 if dfs(0) == float('inf') else dfs(0)

    def minimumPartition2(self, s: str, k: int) -> int:

        n = len(s)
        dp = [0] * (n + 1)

        for index in range(n - 1, -1, -1):
            ans = float('inf')
            i = index
            t = ord(s[i]) - ord('0')
            while t <= k:
                i += 1
                ans = min(ans, dp[i])
                if i >= n:
                    break
                t *= 10
                t += ord(s[i]) - ord('0')

            dp[index] = ans + 1
        return dp[0] if dp[0] != float('inf') else -1

    # 贪心
    def minimumPartition(self, s: str, k: int) -> int:

        n = len(s)
        x = 0
        ans = 1  # ans是分割的点数，实际的子数组个数要加一，所以初始化为1
        for i in range(0, n):
            v = int(s[i])
            if v > k: return -1
            x *= 10
            x += v
            if x > k:
                ans += 1
                x = v
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.minimumPartition("165462", 60))
    print(s.minimumPartition("238182", 5))
    print(s.minimumPartition("1", 1))
