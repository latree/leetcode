
# Definition for a Node.
from typing import Deque


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # # ********** note **************
        # # 第二遍心得
        # # 这个created_map 是重点。在第二遍做的时候还是会出错。
        # # 闭环的case其实很容易想到，比较常见。用一个visited 就可以解决问题
        
        # # 但是created_map，
        # # 比如 [[2,4],[1,3],[2,4],[1,3]]
        # # 这里面在 iterate到 node.val = 2 和node.val = 4 的时候都会碰到他们的邻居
        # # node.val = 3。但是这个node_3 还没有被访问，所以就会造成visited不会cover这个case
        # # 那么我们就需要用另个一created_map来记录我们之前所有已经created 过的node。这样
        # # 才会避免重复create的情况

        # if not node:
        #     return None
        # queue = Deque()
        # # 最开始的时候我是有两个queue同时执行来复制所有queue的操作，但其实不需要这个过程。只要iterate queue
        # # 的时候，每一个新created node 都能被记录，在需要的时候能被拿到就可以了
        # # copy_queue = Deque()
        # queue.append(node)
        # res_node = Node(node.val)
        # # copy_queue.append(res_node)
        # # 因为这是一个undirected graph 所以必须要有visite，要不然就会进入无限循环
        # visited = set()
        # # 因为会出现第一个node 在loop邻居的时候就创建了一个node，在下一个node 如果再遇到同一个node
        # # 必须要记录之前created node，要不然就会重复创建node。所以要在每一次create 一个node的时候
        # # 就把新创建的node 加入到这个map里
        # created_map = {}
        # created_map[node] = res_node
        # while queue:
        #     cur_node = queue.popleft()
        #     # cur_copy_node = copy_queue.popleft()
        #     if cur_node in visited:
        #         continue
        #     visited.add(cur_node)
        #     for neighbor in cur_node.neighbors:
        #         if neighbor:
        #             if neighbor not in created_map:
        #                 copy_neighbor = Node(neighbor.val) 
        #                 created_map[neighbor] = copy_neighbor
        #             else:
        #                 copy_neighbor = created_map[neighbor]
        #             # cur_copy_node.neighbors.append(copy_neighbor)
        #             created_map[cur_node].neighbors.append(copy_neighbor)

        #             queue.append(neighbor)
        #             # copy_queue.append(copy_neighbor)
        # return res_node


# 第三遍：
        if not node:
            return
        
        visited = set()
        created_node = {}
        queue = deque()
        
        copy_start = Node(node.val, [])
        queue.append((node, copy_start))
        
#         ********** important ************
#         created_map 还是漏掉了
        created_node[node] = copy_start
        visited
        
        while queue:
            cur_node, cur_copy_node = queue.pop()
            if cur_node in visited:
                continue
            visited.add(cur_node)
            for neighbor in cur_node.neighbors:
                if neighbor not in created_node:
                    copy_neighbor = Node(neighbor.val, [])
                    created_node[neighbor] = copy_neighbor
                # 这个else 也漏掉了。如果neight in created_node. 那么说明copy_neighbor 已经created好了，那么直接用就可以
                else:
                    copy_neighbor = created_node[neighbor]
                cur_copy_node.neighbors.append(copy_neighbor)
                queue.append((neighbor, copy_neighbor))
        
        return copy_start