# 28. 找出字符串中第一个匹配项的下标
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        next = self.nextArray(needle)
        n = len(haystack)
        m = len(needle)
        x = y = 0
        while x < n and y < m:
            if haystack[x] == needle[y]:
                y += 1
                x += 1
            elif y == 0:
                x += 1
            else:
                y = next[y]

        return x - y if y == m else -1

    def nextArray(self, s: str):
        n = len(s)
        if n == 1:
            return [-1]
        next = [0] * n
        next.append(-1)
        next.append(0)
        i = 2
        cn = 0
        while i < n:
            if s[i - 1] == s[cn]:
                next[i] = cn + 1
                cn += 1
                i += 1
            elif cn > 0:
                cn = next[cn]
            else:
                next[i] = 0
                i += 1
        return next


if __name__ == '__main__':
    s = Solution()
    print(s.strStr("sadbutsad", "sad"))
    print(s.strStr("leetcode", "leeto"))
    print(s.strStr("leetcode", "eetc"))
    print(s.strStr("mississippi", "issip"))
