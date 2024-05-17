# 870. 优势洗牌
from typing import List


class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        nums1.sort()
        # 按nums2的大小排序的他们的下标
        index = sorted(range(n), key=lambda x: nums2[x])

        i = 0
        left = 0
        right = n - 1
        ans = [-1] * n
        while i < n:
            if nums1[i] > nums2[index[left]]:

                ans[index[left]] = nums1[i]
                i += 1
                left += 1

            else:

                ans[index[right]] = nums1[i]
                right -= 1
                i += 1

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.advantageCount([2, 7, 11, 15], [1, 10, 4, 11]))
