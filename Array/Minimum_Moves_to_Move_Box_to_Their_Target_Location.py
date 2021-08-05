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