import collections
from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(dict)
        
        for (from_c, to_c), val in zip(equations, values):
            graph[from_c][to_c] = val
            graph[to_c][from_c] = 1/val
            
        def bfs(src, dst):
            queue = collections.deque()
            queue.append([src, 1])
            visited = set()
            
            while queue:
                c_node, c_rate = queue.popleft()
                visited.add(c_node)
                if c_node == dst:
                    return c_rate
                else:
                    for n_dst, n_rate in graph[c_node].items():
                        if n_dst not in visited:
                            queue.append([n_dst, n_rate * c_rate])
            
            return -1
            
        res = []
        
        for query in queries:
            if not (query[0] in graph and query[1] in graph):
                res.append(-1)
            else:
                res.append(bfs(query[0], query[1]))
        return res
