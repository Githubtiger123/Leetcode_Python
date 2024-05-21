# 1775. 通过最少操作次数使数组的和相等
from typing import List


class Solution:
    def minOperations1(self, nums1: List[int], nums2: List[int]) -> int:

        ans = 0
        nums1.sort()
        nums2.sort()

        max_nums = nums1 if sum(nums1) > sum(nums2) else nums2
        min_nums = nums1 if sum(nums1) < sum(nums2) else nums2

        max_sum = sum(max_nums)
        min_sum = sum(min_nums)
        max_total = len(max_nums)
        min_total = len(min_nums)

        sub = max_sum - min_sum
        max_index = max_total - 1
        min_index = 0

        while sub != 0:

            m1 = m2 = float("-inf")
            if max_index >= 0:
                m1 = max_nums[max_index] - 1 if max_nums[max_index] - 1 < sub else sub

            if min_index < min_total:
                m2 = 6 - min_nums[min_index] if 6 - min_nums[min_index] < sub else sub

            if m1 >= m2:
                max_index -= 1
                sub -= m1
            else:
                min_index += 1
                sub -= m2

            ans += 1
            if sub == 0:
                return ans
            if max(m1, m2) == float("-inf"):
                return -1
        # 循环一开始就没进去 sub == 0
        return 0

    # 灵神的优化
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        if 6 * len(nums1) < len(nums2) or 6 * len(nums2) < len(nums1):
            return -1  # 优化
        d = sum(nums2) - sum(nums1)  # 数组元素和的差，我们要让这个差变为 0
        if d < 0:
            d = -d
            nums1, nums2 = nums2, nums1  # 统一让 nums1 的数变大，nums2 的数变小
        ans = 0
        # 统计每个数的最大变化量（nums1 的变成 6，nums2 的变成 1）
        from collections import Counter
        cnt = Counter(6 - x for x in nums1) + Counter(x - 1 for x in nums2)
        for i in range(5, 0, -1):  # 从大到小枚举最大变化量 5 4 3 2 1
            if i * cnt[i] >= d:  # 可以让 d 变为 0
                return ans + (d + i - 1) // i  # (d + i - 1) // i很妙
            ans += cnt[i]  # 需要所有最大变化量为 i 的数
            d -= i * cnt[i]


if __name__ == '__main__':
    s = Solution()
    print(s.minOperations([1, 2, 3, 4, 5, 6], [1, 1, 2, 2, 2, 2]))
    print(s.minOperations([1, 1, 1, 1, 1, 1, 1], [6]))
    print(s.minOperations([6, 6], [1]))
