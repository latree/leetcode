from Data_Structure.tree_node import TreeNode
from typing import Optional, List
from collections import deque, heapq

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # # k: columne value, v: list of node value
        # col_map = {}
        # queue = deque()
        # # queue element type: (TreeNode, row, col)
        # queue.append((root, 0, 0))
        
        # while queue:
        #     size = len(queue)
        #     # 在每一层的每个col 的list设置成priority queue 那么要比单纯的list 最后再sort一遍要快很多
        #     # k: columne value, v: priority queue node value
        #     cur_col_map = {}
        #     for i in range(size):
        #         c_n, r, c = queue.popleft()
        #         cur_col_map[c] = cur_col_map.get(c, [])
        #         heapq.heappush(cur_col_map[c], c_n.val)
                
        #         if c_n.left:
        #             queue.append((c_n.left, r + 1, c - 1))
        #         if c_n.right:
        #             queue.append((c_n.right, r + 1, c + 1))
            
        #     for k, v in cur_col_map.items():
        #         col_map[k] = col_map.get(k, [])
                
        #         while cur_col_map[k]:
        #             value = heapq.heappop(cur_col_map[k])
        #             col_map[k].append(value)
            
        # keys = list(col_map.keys())
        # keys.sort()
        # res = []
        # for key in keys:
        #     res.append(col_map[key])
        
        # return res

    # 第二遍：
    #     1. 用dfs mark 所有的坐标
    #     2. 计算一个col的offset， 因为col 坐标是从一个负数开始的
    #     3. iterate row， col的range。 如果坐标在idx_map里面而且长度大于1 那么就要sort一下，然后再加到res里面
        def dfs(r, c, node, idx_map, row_set, col_set):
            if not node:
                return
            
            if (r, c) in idx_map:
                idx_map[(r, c)].append(node.val)
            else:
                idx_map[(r, c)] = [node.val]
            
            row_set.add(r)
            col_set.add(c)
            
            dfs(r + 1, c - 1, node.left, idx_map, row_set, col_set)
            dfs(r + 1, c + 1, node.right, idx_map, row_set, col_set)
        
        idx_map = {}
        
        row_set = set()
        col_set = set()
        dfs(0, 0, root, idx_map, row_set, col_set)

        col_offset = 0 - min(col_set)
        
        res = [[] for _ in range(len(col_set))]
        for i in range(len(col_set)):
            for j in range(len(row_set)):
                c_i = i - col_offset
                if (j, c_i) in idx_map:
                    if len(idx_map[(j, c_i)]) > 1: 
                        idx_map[(j, c_i)].sort()
                    res[i] += idx_map[(j, c_i)]
        
        return res