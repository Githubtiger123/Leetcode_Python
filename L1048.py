from functools import cache
from typing import List


class Solution:
    def longestStrChain1(self, words: List[str]) -> int:
        ws = set(words)

        @cache
        def dfs(s):
            ans = 0
            for i in range(len(s)):
                t = s[:i] + s[i + 1:]
                if t in ws:
                    ans = max(ans, dfs(t))

            return ans + 1

        return max(dfs(s) for s in words)

    def longestStrChain1(self, words: List[str]) -> int:

        n = len(words)
        ws = set(words)
        words.sort(key=len)
        dp = [0] * n
        f = {}

        for i in range(n):
            f[words[i]] = i
            ans = 0
            for j in range(len(words[i])):
                t = words[i][:j] + words[i][j + 1:]
                if t in ws:
                    ans = max(ans, dp[f.get(t)])
            dp[i] = ans + 1

        return max(dp)

    def longestStrChain(self, words: List[str]) -> int:
        n = len(words)
        words.sort(key=len)
        dp = {}

        for i in range(n):
            dp[words[i]] = 1
            ans = 0
            for j in range(len(words[i])):
                t = words[i][:j] + words[i][j + 1:]
                ans = max(ans, dp.get(t, 0))
            dp[words[i]] = ans + 1

        return max(dp.values())


if __name__ == '__main__':
    s = Solution()
    print(s.longestStrChain(["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]))
    print(s.longestStrChain(["a", "b", "ba", "bca", "bda", "bdca"]))
