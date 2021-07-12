#116. Populating Next Right Pointers in Each Node
# O(n) | Space: O(1)

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        queue = deque([root])
        
        while queue:
            prev = None
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
                if i == level_size - 1:
                    node.next = None
                    
                if prev != None:
                    prev.next = node
                
                prev = node
                
        return root