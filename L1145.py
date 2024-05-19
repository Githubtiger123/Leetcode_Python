# 1145. 二叉树着色游戏
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.target = 0
        self.n = 0

    def dfs(self, root: Optional[TreeNode]):

        if root is None: return 0

        if root.val == self.target:
            self.n = max(self.dfs(root.left), self.dfs(root.right))
            return 0

        return self.dfs(root.left) + self.dfs(root.right) + 1

    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:

        self.target = x
        if x == 1:
            t = max(self.dfs(root.left), self.dfs(root.right))
        else:
            t = self.dfs(root)

        return t > n - t or self.n > n - self.n
