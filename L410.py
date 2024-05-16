# 410. 分割数组的最大值
from typing import List


class Solution:

    def dfs(self, start, partition, nums):

        if partition == 0 and start != len(nums):
            s = 0
            for i in range(start, len(nums)):
                s += nums[i]
            return s
        if len(nums) - 1 - start < partition:
            return

        ans = 0
        for i in range(start, len(nums)):
            t = self.dfs(i, partition - 1, nums)
            ans = ans if ans >= t else t

        return ans

    def splitArray(self, nums: List[int], k: int) -> int:

        n = len(nums)
        # array = [0] * n
        ans = nums[0]
        s = nums[0]
        for i in range(1, n):
            t = self.dfs(i, k - 1, nums)
            ans = ans if ans < t else t
            s += nums[i]


if __name__ == '__main__':
    pass
