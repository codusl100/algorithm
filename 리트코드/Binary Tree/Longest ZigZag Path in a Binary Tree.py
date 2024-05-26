# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        max_length = 0

        def dfs(node, deep, dir):

            nonlocal max_length

            max_length = max(max_length, deep)

            if node.left:
                dfs(node.left, deep+1, 'left') if dir != 'left' else dfs(node.left, 1, 'left')
            if node.right:
                dfs(node.right, deep+1, 'right') if dir != 'right' else dfs(node.right, 1, 'right')

        dfs(root, 0, '')

        return max_length