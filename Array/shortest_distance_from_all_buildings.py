from typing import List
from collections import deque 
import math

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        # 这个是求shortest distance 应该及时反映出来用bfs做会好一些
        # 从有房子的地方到0 的最短距离，然后把每一个房子到这个0的距离都相加，最后找到最小值
        moves = [(1, 0),(0, 1),(-1, 0),(0, -1)]
        m = len(grid)
        n = len(grid[0])
        cache = [[(0, 0)for i in range(n)] for i in range(m)]
        building_pos = []
        
        def bfs(r, c, cache, grid, num_reached):
            queue = deque()
            queue.append((r, c))
            steps = -1
            visited = set()
            while queue:
                size = len(queue)
                steps += 1
                for i in range(size):
                    cur_r, cur_c = queue.popleft()
                    if (cur_r, cur_c) in visited:
                        continue
                    visited.add((cur_r, cur_c))
                    
                    if grid[cur_r][cur_c] == num_reached:
                        dis, house_reached = cache[cur_r][cur_c]
                        dis += steps
                        house_reached += 1
                        cache[cur_r][cur_c] = (dis, house_reached)
                        grid[cur_r][cur_c] = num_reached - 1
                    for move in moves:
                        nr, nc = cur_r + move[0], cur_c + move[1]
                        if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited and grid[nr][nc] == num_reached:
                            queue.append((nr, nc))  
        
        # 这个optimization不好想
        num_reached = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    building_pos.append((i, j))
                    bfs(i, j, cache, grid, num_reached)
                    num_reached -= 1
        
        
        min_dis = math.inf
        total_building = len(building_pos)
        for i in range(m):
            for j in range(n):
                dis, house_reached = cache[i][j]
                if house_reached == total_building:
                    min_dis = min(min_dis, dis)
        
        return min_dis if min_dis != math.inf else -1