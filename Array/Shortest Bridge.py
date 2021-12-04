from typing import List
from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # find the first island one 1
        def dfs(grid, queue, i, j, visited, moves):
            # 这道题的思路比较简单，就是找到第一个岛屿的所有的点，然后bfs 到第二个岛屿的点。一旦找到就return steps 因为是bfs所以一定是最短的。
            # 刚开始的时候思路有点没有打开的原因：
            # 认为必须要找到第一个岛屿的边缘
            # 其实不用找到第一个岛屿的边缘。可以把所有第一个岛屿的点都放进bfs的queue里面。这样每扩散一层就是把第一个岛屿里面的所有的点都扩散一层。
            # 在中间的点无所谓，它不可能是连接两个岛屿的shortest bridge。必须是边缘的点
            
            # 可以没有这个stop condition， 因为stop condition 就是不能整个island的边缘。只要next move 不是grid 不是1，那么就不会继续recursion call
            # if not grid[i][j]:
            #     return
            
            for move in moves:
                n_i = i + move[0]
                n_j = j + move[1]
                if 0 <= n_i < len(grid) and 0 <= n_j < len(grid[0]) and (n_i, n_j) not in visited and grid[n_i][n_j] == 1:
                    queue.append([n_i, n_j])
                    visited.add((n_i, n_j))
                    dfs(grid, queue, i + move[0], j + move[1], visited, moves)
                
        moves = [[1, 0],[0, 1],[-1, 0],[0, -1]]        
        first = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    first = [i, j]
                
        queue = deque()
        visited = set()
        queue.append([first[0], first[1]])
        visited.add((first[0], first[1]))
        dfs(grid, queue, first[0], first[1], visited, moves)
        steps = 0
        while queue:
            size = len(queue)
            
            for i in range(size):
                node = queue.popleft()
                
                
                for move in moves:
                    n_i = node[0] + move[0]
                    n_j = node[1] + move[1]
                    if 0 <= n_i < len(grid) and 0 <= n_j < len(grid[0]) and (n_i, n_j) not in visited:
                        if grid[n_i][n_j] == 1:
                            return steps
                        else:
                            queue.append([n_i, n_j])
                            visited.add((n_i, n_j))
                    
            steps += 1
        
        return steps