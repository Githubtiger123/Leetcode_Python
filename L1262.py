# 1262. 可被三整除的最大和
from functools import cache
from typing import List


class Solution:
    def maxSumDivThree1(self, nums: List[int]) -> int:
        remainder = 0
        remainder_1 = float("inf")
        remainder_1_2 = float("inf")
        remainder_2 = float("inf")
        remainder_2_2 = float("inf")
        sum = 0
        n = len(nums)

        for i in range(n):
            sum += nums[i]
            remainder = sum % 3
            if nums[i] % 3 == 1:
                temp = [0] * 3
                temp[0] = remainder_1
                temp[1] = remainder_1_2
                temp[2] = nums[i]
                temp.sort()
                remainder_1 = temp[0]
                remainder_1_2 = temp[1]

            elif nums[i] % 3 == 2:
                temp = [0] * 3
                temp[0] = remainder_2
                temp[1] = remainder_2_2
                temp[2] = nums[i]
                temp.sort()
                remainder_2 = temp[0]
                remainder_2_2 = temp[1]

        if remainder == 0:
            return sum

        if remainder == 2:
            sum -= min(remainder_1 + remainder_1_2, remainder_2)
        else:
            sum -= min(remainder_2 + remainder_2_2, remainder_1)
        return sum

    def maxSumDivThree(self, nums: List[int]) -> int:
        @cache
        def dfs(i, j):
            if i == -1:
                return 0 if j == 0 else float("-inf")

            # t = (j + nums[i]) % 3
            # if t == 1:
            #     t = 2
            # if t == 2:
            #     t = 1
            return max(dfs(i - 1, j), dfs(i - 1, (j + nums[i]) % 3) + nums[i])

        n = len(nums)
        return dfs(n - 1, 0)


if __name__ == '__main__':
    s = Solution()
    print(s.maxSumDivThree([3, 6, 5, 1, 8]))
