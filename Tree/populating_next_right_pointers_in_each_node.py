
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def connect_helper(node1:'Node', node2:'Node') -> None:
            if not node1 or not node2:
                return
            
            node1.next = node2
            
            connect_helper(node1.left, node1.right)
            connect_helper(node2.left, node2.right)
            
            connect_helper(node1.right, node2.left)
        
        if not root:
            return root
        connect_helper(root.left, root.right)
        return root