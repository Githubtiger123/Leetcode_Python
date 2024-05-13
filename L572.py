# 572. 另一棵树的子树
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def same(self, a, b):

        if a is None and b is None:
            return True
        if a is not None and b is not None:
            return a.val == b.val and self.same(a.left, b.left) and self.same(a.right, b.right)

        return False

    def isTree(self, t1, t2):

        if t1 is not None and t2 is not None:
            return self.same(t1, t2) or self.isSubtree(t1.left, t2) or self.isSubtree(t1.right, t2)
        return t2 is None

    def isSubtree1(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        return self.isTree(root, subRoot)

    def dfs(self, root: Optional[TreeNode], ans):
        if root is None:
            ans.append("null")
            return
        ans.append(str(root.val))
        self.dfs(root.left, ans)
        self.dfs(root.right, ans)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.dfs(root, ans)
        return ans

    def getNext(self, s):

        n = len(s)
        next = [-1] * n
        next[0] = -1
        next[1] = 0
        i = 2
        cn = 0
        while i < n:
            if s[i - 1] == s[cn]:
                cn += 1
                next[i] = cn
                i += 1
            elif cn > 0:
                cn = next[cn]
            else:
                next[i] = 0
                i += 1
        return next

    def KMP(self, s1, s2):

        n = len(s1)
        m = len(s2)
        x = 0
        y = 0
        next = self.getNext(s2)
        while x < n and y < m:
            if s1[x] == s2[y]:
                y += 1
                x += 1
            elif y == 0:
                x += 1
            else:
                y = next[y]

        return x - m if y == m else -1

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        root_str = self.preorderTraversal(root)
        sub_str = self.preorderTraversal(subRoot)

        return True if self.KMP(root_str, sub_str) != -1 else False


if __name__ == '__main__':
    pass
