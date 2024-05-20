# 918. 环形子数组的最大和
from typing import List


class Solution:

    def maxSubArray(self, nums):
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        ans = dp[0]
        for i in range(1, n):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            ans = max(ans, dp[i])

        return ans

    def minSubArray(self, nums):
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        ans = dp[0]
        for i in range(1, n):
            dp[i] = min(dp[i - 1] + nums[i], nums[i])
            ans = min(ans, dp[i])

        return ans

    def maxSubarraySumCircular1(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0] + nums[1], nums[0], nums[1])

        case1 = self.maxSubArray(nums)
        case2 = self.minSubArray(nums[1:n - 1:])

        print(case1)
        return max(case1, sum(nums) - case2)

    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0] + nums[1], nums[0], nums[1])

        t_max = ans_max = nums[0]
        t_min = ans_min = nums[1]
        s = nums[0]
        for i in range(1, n):
            s += nums[i]
            t = t_max
            t_max = max(t + nums[i], nums[i])
            ans_max = max(ans_max, t_max)

            if 1 < i < n - 1:
                t = t_min
                t_min = min(t + nums[i], nums[i])
                ans_min = min(ans_min, t_min)

        return max(ans_max, s - ans_min)


if __name__ == '__main__':
    s = Solution()
    print(s.maxSubarraySumCircular([1, -2, 3, -2]))
    print(s.maxSubarraySumCircular([5, -3, 5]))
