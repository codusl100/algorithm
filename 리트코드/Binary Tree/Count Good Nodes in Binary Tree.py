class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = [0]
        def dfs(root, maxi):
            if root:
                maxi = max(maxi, root.val)
                if maxi <= root.val:
                    res[0] += 1
                if root.left:
                    dfs(root.left, maxi)
                if root.right:
                    dfs(root.right, maxi)
        dfs(root, -maxsize)
        return res[0]