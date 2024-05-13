# 330. 按要求补齐数组
from typing import List


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        ans = 0
        s = 1
        i = 0
        while s - 1 < n:
            if i < len(nums) and nums[i] <= s:
                s += nums[i]
                i += 1
            else:
                s += s
                ans += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.minPatches([1, 3], 6))
