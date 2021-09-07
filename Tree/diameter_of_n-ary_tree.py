# Definition for a Node.
import heapq

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def __init__(self):
        self.res = 0
        
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        def helper(root: 'Node') -> int:
            if not root:
                return 0

            depths = []
            max_depth = 0
            for child in root.children:
                if child:
                    cur_depth = helper(child) + 1
                    depths.append(cur_depth)

            res = 0
            cur_max_path = 0
            if depths:
                if len(depths) >= 2:
                    top_two_depths = heapq.nlargest(2, depths)
                    cur_max_path = top_two_depths[0] + top_two_depths[1]
                    res = top_two_depths[0]
                else:
                    cur_max_path = depths[0]
                    res = depths[0]
    
            self.res = max(cur_max_path, self.res)
            return res
        helper(root)
        return self.res
    