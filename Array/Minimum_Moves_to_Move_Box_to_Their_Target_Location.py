from typing import List
from collections import deque

class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        # 做bfs的时候可以不用deque， 直接用双list 就可以
        # seen |= cur 代表两个set union
        # Time: O(v**2)
        # Spcae: O(v**2)

        M = len(grid)
        N = len(grid[0])
        dire = [(1,0),(0,1),(-1,0),(0,-1)]

        def player_next_move(r, c, box, seen):
            for r_move, c_move in dire:
                nr, nc = r + r_move, c + c_move
                if  0 <= nr < M and 0 <= nc < N and grid[nr][nc] != '#' and (nr,nc) != box and (nr,nc) not in seen:
                    yield r_move, c_move
        
        def can_get(cur_b,cur_p,tar):
            seen,cur = set([cur_p]),set([cur_p])
            while cur:
                tmp = []
                for loc in cur:
                    for x, y in player_next_move(loc[0], loc[1], cur_b, seen):
                        tmp += [(loc[0]+x,loc[1] +y)]
                cur = set(tmp)
                seen |= cur
                if tar in seen:
                    return True
            return False

        def box_next_move(r, c, player_pos, seen):
            for r_move, c_move in dire:
                nr, nc = r + r_move, c + c_move
                pr, pc = r - r_move, c - c_move
                if  0 <= nr < M and 0 <= nc < N and grid[nr][nc] != '#' and can_get((r, c), player_pos, (pr, pc)) and ((nr,nc), (r, c)) not in seen:
                    yield r_move, c_move
			
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'B': box = (i,j)
                if grid[i][j] == 'S': player = (i,j)
                if grid[i][j] == 'T': target = (i,j)
				
        seen,cur,res = set([(box,player)]), set([(box,player)]), 0
        while cur:
            tmp = []
            res += 1
            for b,p in cur:
                for x, y in box_next_move(b[0], b[1], p, seen):
                    tmp += [((b[0]+x,b[1]+y),b)]
            cur = set(tmp)
            seen |= cur
            for x,y in dire:
                if (target,(target[0]+x,target[1]+y)) in seen:
                    return res
        return -1

# # 第二遍心得：
#         # ************** note ******************
#         # 这道题的步骤就是繁琐。算法上没有很难
#         # 关键的点就是在于把具体的小步骤可以用一个一个function写出来
#         # 1. 找到box next move, 需要先找到player 能不能move box 到新的位置， ----- box_next_move function
#         # 2. player 能不能move到新的位置取决于，从现在player的位置到player target 位置有没有
#         # available的path。------- can_get function
#         # 3. 有available的path那么每一步的限制条件是什么  ---- player_next_move function
#         M = len(grid)
#         N = len(grid[0])
#         moves = [(1,0),(0,1),(-1,0),(0,-1)]
        
#         def player_next_move(box, player, seen):
#             for x, y in moves:
#                 nr, nc = player[0] + x, player[1] + y
#                 if 0 <= nr < M and 0 <= nc < N and (nr, nc) not in seen and grid[nr][nc] != '#' and (nr, nc) != box:
#                     yield x, y
        
#         def can_get(cur_b, cur_p, tar):
#             seen = set()
#             queue = deque()
#             queue.append(cur_p)
#             seen.add(cur_p)
#             while queue:
#                 size = len(queue)
#                 for _ in range(size):
#                     cur_node = queue.popleft()
#                     for x, y in player_next_move(cur_b, (cur_node[0], cur_node[1]), seen):
#                         queue.append((cur_node[0]+x,cur_node[1] +y))
#                         seen.add((cur_node[0]+x,cur_node[1] +y))
#                 if tar in seen:
#                     return True
            
#             return False
        
#         def box_next_move(box, player, seen):
#             for x, y in moves:

#                 # ************** note ******************
#                 # this is next box position
#                 nr_b, nc_b = box[0] + x, box[1] + y
                
#                 # ************** note ******************
#                 # This is player position need to be available so that player can push box to box next position
#                 nr_p, nc_p = box[0] - x, box[1] - y
#                 player_pos_should_available = (nr_p, nc_p)
#                 next_box_pos = (nr_b, nc_b)

#                 # ************** note ******************
#                 # 这个条件比较关键
#                 if 0 <= nr_b < M and 0 <= nc_b < N and can_get(box, player, player_pos_should_available) and (next_box_pos, b) not in seen and grid[nr_b][nc_b] != '#':
#                     yield x, y
        
#         for i in range(M):
#             for j in range(N):
#                 if grid[i][j] == "S": player = (i, j)
#                 if grid[i][j] == "B": box = (i, j)
#                 if grid[i][j] == "T": target = (i, j)
        
#         queue = deque()
#         queue.append((box, player))
#         seen=set()
#         seen.add((box, player))
#         res = 0
#         while queue:
#             size = len(queue)
#             res += 1
#             for _ in range(size):
#                 cur_node = queue.popleft()
#                 b, p = cur_node[0], cur_node[1]
#                 for x, y in box_next_move(b, p, seen):
#                     queue.append(((b[0]+x,b[1]+y),b))
#                     seen.add(((b[0]+x,b[1]+y),b))
#             for x,y in moves:
#                 if (target,(target[0]+x,target[1]+y)) in seen:
#                     return res
#         return -1