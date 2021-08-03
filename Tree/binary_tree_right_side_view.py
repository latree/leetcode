from Data_Structure.tree_node import TreeNode
from typing import List
from collections import deque

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        # # solution 1： DFS
        # Time: O(n) n is size of treenode
        # Space: O(n) n is size of treenode
        # 这个dfs解法非常巧妙的运用到了先往最右边走再return 再走左边
        # 只要每到新的一层，就先把最左边的node 加进path里
        # if not root:
        #     return []
        
        # right_side = []
        # def helper(node: TreeNode, level: 0):
        #     if level == len(right_side):
        #         right_side.append(node.val)
            
        #     for child in [node.right, node.left]:
        #         if child:
        #             help(child, level + 1)
            
        # help(root, 0)
        # return right_side

        # solution 2: BFS
        # Time: O(n) n is size of treenode
        # Space: O(n) n is size of treenode
        if not root:
            return []
        queue = deque([root])
        res = []
        while queue:
            res.append(queue[-1].val)
            running_size = len(queue)
            i = 0
            while i < running_size:
                node = queue.popleft()
                i += 1
                for child in [node.left, node.right]:
                    if child:
                        queue.append(child)
        
        return res
                    