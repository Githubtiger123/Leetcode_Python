# 2606. 找到最大开销的子字符串
from typing import List


class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        n = len(s)
        d = {}
        for i in range(len(chars)):
            d[chars[i]] = vals[i]

        dp = [0] * n
        dp[0] = d.get(s[0], ord(s[0]) - ord('a') + 1)
        for i in range(1, n):
            dp[i] = max(dp[i - 1] + d.get(s[i], ord(s[i]) - ord('a') + 1), d.get(s[i], ord(s[i]) - ord('a') + 1))
        return max(0, max(dp))


if __name__ == '__main__':
    s = Solution()
    print(s.maximumCostSubstring('adaa', 'd', [-1000]))
    print(s.maximumCostSubstring('adaa', 'd', [-1000]))
