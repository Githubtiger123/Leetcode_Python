# 1144. 递减元素使数组呈锯齿状
from typing import List


class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        n = len(nums)
        cp_arr = nums[:]
        t1 = 0
        t2 = 0
        for i in range(0, n - 1):
            if i % 2 == 0:
                if nums[i] > nums[i + 1]:
                    continue
                else:
                    t1 += nums[i + 1] - nums[i] + 1
                    nums[i + 1] = (nums[i] - 1)
            else:
                if nums[i] >= nums[i + 1]:
                    t1 += nums[i] - nums[i + 1] + 1
                    nums[i] = (nums[i + 1] - 1)

        nums = cp_arr[:]
        for i in range(0, n - 1):
            if i % 2 == 0:
                if nums[i] < nums[i + 1]:
                    continue
                else:
                    t2 += nums[i] - nums[i + 1] + 1
                    nums[i] = (nums[i + 1] - 1)
            else:
                if nums[i] <= nums[i + 1]:
                    t2 += nums[i + 1] - nums[i] + 1
                    nums[i + 1] = (nums[i] - 1)

        return min(t1, t2)


if __name__ == '__main__':
    s = Solution()
    print(s.movesToMakeZigzag([1, 2, 3]))
