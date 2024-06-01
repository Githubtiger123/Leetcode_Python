# 313. 超级丑数
from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        index = [1] * len(primes)
        ans = primes[::]
        dp = [1] * (n + 1)
        dp[0] = float('inf')

        for i in range(2, n + 1):
            min_index = 0
            # for j in range(len(primes)):
            #     if ans[j] < ans[min_index]:
            #         min_index = j
            # dp[i] = ans[min_index]
            # temp = ans[min_index]
            temp = min(ans)
            dp[i] = temp
            for t in range(len(primes)):
                if ans[t] == temp:
                    index[t] += 1
                    ans[t] = primes[t] * dp[index[t]]
        print(dp)
        return dp[n]


if __name__ == '__main__':
    s = Solution()
    print(s.nthSuperUglyNumber(10, [2, 3, 5]))
    print(s.nthSuperUglyNumber(12, [2, 7, 13, 19]))
