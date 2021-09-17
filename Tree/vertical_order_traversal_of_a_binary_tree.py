from Data_Structure.tree_node import TreeNode
from typing import Optional, List
from collections import deque, heapq

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # k: columne value, v: list of node value
        col_map = {}
        queue = deque()
        # queue element type: (TreeNode, row, col)
        queue.append((root, 0, 0))
        
        while queue:
            size = len(queue)
            # 在每一层的每个col 的list设置成priority queue 那么要比单纯的list 最后再sort一遍要快很多
            # k: columne value, v: priority queue node value
            cur_col_map = {}
            for i in range(size):
                c_n, r, c = queue.popleft()
                cur_col_map[c] = cur_col_map.get(c, [])
                heapq.heappush(cur_col_map[c], c_n.val)
                
                if c_n.left:
                    queue.append((c_n.left, r + 1, c - 1))
                if c_n.right:
                    queue.append((c_n.right, r + 1, c + 1))
            
            for k, v in cur_col_map.items():
                col_map[k] = col_map.get(k, [])
                
                while cur_col_map[k]:
                    value = heapq.heappop(cur_col_map[k])
                    col_map[k].append(value)
            
        keys = list(col_map.keys())
        keys.sort()
        res = []
        for key in keys:
            res.append(col_map[key])
        
        return res