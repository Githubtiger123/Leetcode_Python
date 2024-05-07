# 135. 分发糖果
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        start = [1] * n
        end = [1] * n
        ans = 0
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                start[i] = start[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                end[i] = end[i + 1] + 1
        for i in range(0, n):
            ans += max(start[i], end[i])

        return ans


if __name__ == '__main__':
    s = Solution()
    ans = s.candy([1, 2, 87, 87, 87, 2, 1])
    print(ans)
