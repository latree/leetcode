
from Data_Structure.tree_node import TreeNode

class MaxDepth:
    def maxDepth(self, root: TreeNode) -> int:
#         # solution 1: recursion
#         if not root:
#             return 0
        
#         left = self.maxDepth(root.left) + 1
#         right = self.maxDepth(root.right) + 1
        
#         return max(left, right)
        
        # solution 2: BFS 
        # time: O(n) n is number of node
        # space: O(N) N = 2^(log2(n-1)) which is the maxium num of n nodes at the same layer. n is the total number of nodes.  log2(n-1) is the number of layer. 
        if not root:
            return 0
        
        queue = [root]
        
        depth = 0
        while queue:
            tmp_layer = queue
            if tmp_layer:
                depth += 1
            queue = []
            for node in tmp_layer:
                if node and node.left:
                    queue.append(node.left)
                if node and node.right:
                    queue.append(node.right)
        
        return depth
