# 572. 另一棵树的子树
from typing import Optional


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

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        return self.isTree(root, subRoot)


if __name__ == '__main__':
    pass
