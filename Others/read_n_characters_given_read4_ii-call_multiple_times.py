from typing import List
from collections import deque
# # The read4 API is already defined for you.
# # def read4(buf4: List[str]) -> int:

class Solution:
    # def __init__(self):
    #     self.buff_size = 4
    #     self.buffer = [None for i in range(self.buff_size)]
    #     self.char_left_over = 0
    #     self.left_over_ptr = 0
        
    # def read(self, buf: List[str], n: int) -> int:
    #     char_reads = 0
    #     cur_read = 0
    #     if self.char_left_over:
    #         to_read = min(n, self.char_left_over)
    #         buf[0:to_read] = self.buffer[-self.char_left_over - self.left_over_ptr:]
    #         char_reads += to_read
    #         self.char_left_over -= to_read
            
            
    #     while char_reads < n:
    #         cur_read = read4(self.buffer)
    #         if not cur_read:
    #             break
            
    #         buf[char_reads:char_reads + cur_read] = self.buffer[:cur_read]

    #         char_reads += cur_read
        
    #     res = min(char_reads, n)
        
    #     if not self.char_left_over:
    #         self.char_left_over = char_reads - n if char_reads > n else 0
    #         self.left_over_ptr = self.buff_size - cur_read if cur_read < 4 else 0
        
    #     return res


# 第二遍
    def __init__(self):
        self.buffer = deque()
    
    def read(self, buf: List[str], n: int) -> int:        
        # 这道题没有那么复杂
        # 原理就是每次从read4里面读完以后把所有值都append 到buffer 里面
        # 然后每一次只复制给buf的次数是len(self.buffer), n - idx。两个的最小值
        # 这样就能巧妙的保证里每一次先用掉buffer里面的所有值，然后不够再进入下一个循环，够了
        # 就直接退出循环
        idx = 0
        while True:
            buf4 = [""]*4

            l = read4(buf4)
            self.buffer.extend(buf4)
            # 这两步很精髓
            cur_size = min(len(self.buffer), n - idx)
            for _ in range(cur_size):
                buf[idx] = self.buffer.popleft()
                idx += 1
            
            if cur_size == 0:
                break
        return idx