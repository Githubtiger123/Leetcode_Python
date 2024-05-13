# 144. 二叉树的前序遍历
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def dfs(self, root: Optional[TreeNode], ans):
        if root is None: return
        ans.append(root.val)
        self.dfs(root.left, ans)
        self.dfs(root.right, ans)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.dfs(root, ans)
        return ans


if __name__ == '__main__':
    pass
