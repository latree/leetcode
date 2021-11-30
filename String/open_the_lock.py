from collections import deque
from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def plus_one(cur_num, idx):
            if cur_num[idx] == '9':
                cur_num = cur_num[:idx] + '1' + cur_num[idx + 1:]
            else:
                cur_num = cur_num[:idx] + str(int(cur_num[idx]) + 1) + cur_num[idx + 1:]
            return cur_num
            
        def minus_one(cur_num, idx):
            if cur_num[idx] == '0':
                cur_num = cur_num[:idx] + '9' + cur_num[idx + 1:]
            else:
                cur_num = cur_num[:idx] + str(int(cur_num[idx]) - 1) + cur_num[idx + 1:]
            return cur_num
    
        # 这个小细节需要注意一下。while loop 里面有
        #     if cur_num in dead:
        #         continue
        # 最开始的时候我把dead 和visited 合并成一个set，但是如果合并下面的while loop就会出问题。因为在开始visited 就加了’0000‘
        # 这样直接cut 掉后面所有的分枝。
        # 如果非要合并dead 和visited，那么后面的while loop 就要做相应的改变

        visited = set()
        dead = set(deadends)

        queue = deque()
        queue.append('0000')
        visited.add('0000')
        turns = 0
        while queue:
            size = len(queue)
            for i in range(size):
                cur_num = queue.popleft()
                if cur_num == target:
                    return turns
                if cur_num in dead:
                    continue
                for j in range(4):
                    up = plus_one(cur_num, j)
                    down = minus_one(cur_num, j)
                    if up not in visited:
                        queue.append(up)
                        visited.add(up)
                    if down not in visited:
                        queue.append(down)                    
                        visited.add(down)

            turns += 1
        
        return -1