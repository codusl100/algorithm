# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max, level, maxLevel = -float('inf'), 0, 0
        q = collections.deque()
        q.append(root) # 루트에서 시작
        while q:
            level += 1 # 한 계단씩 갱신
            sum = 0
            for _ in range(len(q)): # 계단에 해당되는 노드들 for문 돌림
                node = q.popleft()
                sum += node.val # 해당 계층의 노드들 값 더해주고
                if node.left: # 왼편
                    q.append(node.left)
                if node.right: # 오른편 queue에 넣어주기
                    q.append(node.right)
            if max < sum: # for문 끝나면 max 최대값과 sum값 비교해서 갱신하기
                max, maxLevel = sum, level
        return maxLevel