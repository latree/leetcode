class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class lowestCommonAncestor:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # Time: O(3*logN) logN is the height of tree. 
        # Space: O(2*logN)
        def get_path_to_root(node):
            path = [node]
            while node.parent:
                path.append(node.parent)
                node = node.parent
            return path


        p_path = get_path_to_root(p)
        q_path = get_path_to_root(q)

        p_set = set(p_path)
        for i in range(len(q_path)):
            if q_path[i] in p_set:
                return q_path[i]

        return None
    
    def call_function(self) -> None:
        root = Node(3)
        root.left = Node(5)
        root.left.left = Node(6)
        root.left.right = Node(2)
        root.left.right.left = Node(7)
        root.left.right.right = Node(4)
        root.right = Node(1)
        root.right.left = Node(0)
        root.right.right = Node(8)
        p = root.left
        q = root.right

        self.lowestCommonAncestor(p, q)