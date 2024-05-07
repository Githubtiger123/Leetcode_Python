# 406. 根据身高重建队列
from typing import List


class Solution:
    @staticmethod
    def myCompare(l: List[int]):
        return (-l[0], l[1])

    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key=self.myCompare)

        ans = [[]]
        print("len", len(ans))
        for p in people:
            ans.insert(p[1], p)
        return ans[0:len(ans) - 1]


if __name__ == '__main__':
    s = Solution()
    ans = s.reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]])
    print(ans)
