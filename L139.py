# 139. 单词拆分
from typing import List


class Solution:

    def dfs(self, index, s, wordDict, dp):
        if index == len(s): return True
        if dp[index] != -1: return True if dp[index] == 1 else False

        ans = False
        for i in range(index, len(s)):
            if s[index:i + 1] in wordDict:
                ans = ans or self.dfs(i + 1, s, wordDict, dp)
        dp[index] = 1 if ans else 0
        return ans

    def wordBreak1(self, s: str, wordDict: List[str]) -> bool:
        dp = [-1] * (len(s))
        return self.dfs(0, s, wordDict, dp)

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(0, i):

                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[n]


if __name__ == '__main__':
    s = Solution()
    ans = s.wordBreak("applepenapple", ["cats", "dog", "sand", "and", "cat"])
    print(ans)

    print(s.wordBreak("leetcode", ["leet", "code"]))

    print(s.wordBreak(
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
        ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]))
