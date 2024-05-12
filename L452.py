# 452. 用最少数量的箭引爆气球
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[1], x[1] - x[0]))
        print(points)
        ans = 1
        end = points[0][1]
        index = 1
        while index < len(points):
            if points[index][0] > end:
                ans += 1
                end = points[index][1]
            index += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    ans = s.findMinArrowShots([[9, 12], [1, 10], [4, 11], [8, 12], [3, 9], [6, 9], [6, 7]])
    print(ans)
