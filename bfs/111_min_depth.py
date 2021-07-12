
# 111. Minimum Depth of Binary Tree
# O(n) | Space: O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        queue = deque([root])
        current_level = 0
        
        while queue:
            current_level += 1
            queue_size = len(queue)
            
            for _ in range(queue_size):
                node = queue.popleft()
                
                if not node.left and not node.right:
                    return current_level
                
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
            
            
        return current_level