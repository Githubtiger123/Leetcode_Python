# 1247. 交换字符使得字符串相同
from collections import Counter


class Solution:
    def minimumSwap1(self, s1: str, s2: str) -> int:
        n = len(s1)
        ans = 0
        x1 = 0
        x2 = 0
        y1 = 0
        y2 = 0
        s1_list = list(s1)
        s2_list = list(s2)
        for i in range(n):
            if s1[i] == 'x':
                x1 += 1
            else:
                y1 += 1
            if s2[i] == 'x':
                x2 += 1
            else:
                y2 += 1
        if (x1 + x2) % 2 != 0 or (y1 + y2) % 2 != 0:
            return -1
        i = 0

        while i < n:
            if s1_list[i] == s2_list[i]:
                i += 1
                continue
            else:
                c = s1_list[i]
                b = False
                for j in range(i + 1, n):
                    if c == s1_list[j] and s1_list[j] != s2_list[j]:
                        s1_list[j] = 'y' if s1_list[j] == 'x' else 'x'
                        ans += 1
                        b = True
                        i += 1
                        break
                if not b:
                    t = s1_list[i]
                    s1_list[i] = s2_list[i]
                    s2_list[i] = t
                    ans += 1
        return ans

    def minimumSwap(self, s1: str, s2: str) -> int:
        cnt = Counter(x for x, y in zip(s1, s2) if x != y)
        d = cnt['x'] + cnt['y']
        return -1 if d % 2 else d // 2 + cnt['x'] % 2


if __name__ == '__main__':
    s = Solution()
    print(s.minimumSwap("xx", "yy"))
