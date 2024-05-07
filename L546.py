# 546. 移除盒子
from typing import List


class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        return self.dfs(boxes, 0, len(boxes) - 1)

    def dfs(self, boxes: List[int], start, end):

        if start > end:
            return 0
        elif start == end:
            return 1
        elif start + 1 == end:
            return 4 if boxes[start] == boxes[end] else 2
        elif boxes[start] == boxes[end]:
            num = boxes[start]
            i = start + 1
            j = end - 1
            while i <= j and boxes[i] == num:
                i += 1
            while j > i and boxes[j] == num:
                j -= 1
            return self.dfs(boxes, i, j) + ((i - start) + (end - j)) ** 2
        else:
            ans = float('-inf')
            for k in range(start, end):
                ans = max(ans, self.dfs(boxes, start, k) + self.dfs(boxes, k + 1, end))

            return ans


if __name__ == '__main__':
    s = Solution()
    print(s.removeBoxes([1, 3, 2, 2, 2, 3, 4, 3, 1]))
    print(s.removeBoxes([1, 2, 1]))
    print(s.removeBoxes([1, 3, 3, 4, 3, 1]))
    print(s.removeBoxes([3, 3, 3]))
