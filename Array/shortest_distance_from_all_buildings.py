from typing import List
from collections import deque 
import math

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        # # 这个是求shortest distance 应该及时反映出来用bfs做会好一些
        # # 从有房子的地方到0 的最短距离，然后把每一个房子到这个0的距离都相加，最后找到最小值
        # moves = [(1, 0),(0, 1),(-1, 0),(0, -1)]
        # m = len(grid)
        # n = len(grid[0])
        # cache = [[(0, 0)for i in range(n)] for i in range(m)]
        # building_pos = []
        
        # def bfs(r, c, cache, grid, num_reached):
        #     queue = deque()
        #     queue.append((r, c))
        #     steps = -1
        #     visited = set()
        #     while queue:
        #         size = len(queue)
        #         steps += 1
        #         for i in range(size):
        #             cur_r, cur_c = queue.popleft()
        #             if (cur_r, cur_c) in visited:
        #                 continue
        #             visited.add((cur_r, cur_c))
                    
        #             if grid[cur_r][cur_c] == num_reached:
        #                 dis, house_reached = cache[cur_r][cur_c]
        #                 dis += steps
        #                 house_reached += 1
        #                 cache[cur_r][cur_c] = (dis, house_reached)
        #                 grid[cur_r][cur_c] = num_reached - 1
        #             for move in moves:
        #                 nr, nc = cur_r + move[0], cur_c + move[1]
        #                 if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited and grid[nr][nc] == num_reached:
        #                     queue.append((nr, nc))  
        
        # # 这个optimization不好想
        # num_reached = 0
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == 1:
        #             building_pos.append((i, j))
        #             bfs(i, j, cache, grid, num_reached)
        #             num_reached -= 1
        
        
        # min_dis = math.inf
        # total_building = len(building_pos)
        # for i in range(m):
        #     for j in range(n):
        #         dis, house_reached = cache[i][j]
        #         if house_reached == total_building:
        #             min_dis = min(min_dis, dis)
        
        # return min_dis if min_dis != math.inf else -1


# 第二遍刷
        # moves = [(1, 0),(0, 1),(-1, 0),(0, -1)]
        # m = len(grid)
        # n = len(grid[0])
        # cache = [[0 for i in range(n)] for i in range(m)]
        # building_pos = []
        
        # def bfs(r, c, cache, grid, num_reached):
        #     queue = deque()
        #     queue.append((r, c))
        #     seen = set()
        #     seen.add((r, c))
            
        #     dist = -1
        #     while queue:
        #         size = len(queue)
        #         dist += 1
        #         for i in range(size):
        #             cur_r, cur_c = queue.popleft()
        #             if grid[cur_r][cur_c] == num_reached + 1:
        #                 grid[cur_r][cur_c] -= 1
        #                 cache[cur_r][cur_c] += dist
        #             for move in moves:
        #                 nr, nc = cur_r + move[0], cur_c + move[1]
        #                 if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in seen and grid[nr][nc] == num_reached + 1:
        #                     queue.append((nr, nc))
        #                     seen.add((nr, nc))
        
        # # ***************** note *************************
        # # 直接用 num_reached 这个var 来mark 每一个空位被几个房子reach 到了，
        # # 每被一个房子reach 到就减一
        # # 这样可以缩减我们做bfs的范畴，因为这个空位的值如果不等于当前已经iterate的房子的数量
        # # 那么说明之前有房子没法到达这个空位，那么我们就直接跳过这个空位就可以了
        # num_reached = 0
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == 1:
        #             num_reached -= 1
        #             bfs(i, j, cache, grid, num_reached)
        
        # res = math.inf
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == num_reached:
        #             res = min(res, cache[i][j])
        # return res if res != math.inf else -1
        
        
#         # building to 0 solution
#         moves = [(1, 0),(0, 1),(-1, 0),(0, -1)]
#         m = len(grid)
#         n = len(grid[0])
#         cache = [[(0, 0)for i in range(n)] for i in range(m)]
#         building_pos = []
        
#         def bfs(r, c, cache, grid):
#             queue = deque()
#             queue.append((r, c))
#             seen = set()
#             seen.add((r, c))
            
#             dist = -1
#             while queue:
#                 size = len(queue)
#                 dist += 1
#                 for i in range(size):
#                     cur_r, cur_c = queue.popleft()
#                     if grid[cur_r][cur_c] != 1:
#                         cur_dist, cur_buildings = cache[cur_r][cur_c]
#                         cache[cur_r][cur_c] = (cur_dist + dist, cur_buildings + 1)
#                     for move in moves:
#                         nr, nc = cur_r + move[0], cur_c + move[1]
#                         if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in seen and grid[nr][nc] == 0:
#                             queue.append((nr, nc))
#                             seen.add((nr, nc))
        
#         num_building = 0
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == 1:
#                     # building_pos.append((i, j))
#                     num_building += 1
#                     bfs(i, j, cache, grid)
        
#         res = math.inf
#         for i in range(m):
#             for j in range(n):
#                 distance, num_reached = cache[i][j]
#                 if num_reached == num_building:
#                     res = min(res, distance)
#         return res if res != math.inf else -1


# 第三遍：
        moves = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        m = len(grid)
        n = len(grid[0])
        
        cache = [[(0, 0) for _ in range(n)] for _ in range(m)]
        
        def bfs(cache, grid, r, c):
            queue = deque()
            queue.append((r, c))
            seen = set()
            
            # need to discuss
            dist = -1
            
            while queue:
                size = len(queue)
                dist += 1
                for i in range(size):
                    c_r, c_c = queue.popleft()
                    
                    # *********** important ***************
                    # seen 的node必须要写在这里，在bfs 的run 的时候
                    if (c_r, c_c) in seen:
                        continue
                    seen.add((c_r, c_c))
                    if grid[c_r][c_c] != 1:
                        cur_dist, cur_num_building = cache[c_r][c_c]
                        cache[c_r][c_c] = (dist + cur_dist, cur_num_building + 1)
                        
                        
                    for move in moves:
                        n_r = c_r + move[0]
                        n_c = c_c + move[1]
                        if 0 <= n_r < m and 0 <= n_c < n and (n_r, n_c) not in seen and grid[n_r][n_c] == 0:
                            queue.append((n_r, n_c))
        
        num_buildings = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    num_buildings += 1 
                    bfs(cache, grid, i, j)
        
        res = math.inf
        for i in range(m):
            for j in range(n):
                cur_dist, cur_b_num = cache[i][j]
                if cur_b_num == num_buildings:
                    res = min(cur_dist, res)
        
        return res if res != math.inf else -1