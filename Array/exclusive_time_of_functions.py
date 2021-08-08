from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:    
        stack = []
        pre_time = 0
        res = [0] * n
        for log in logs:
            func, type, timestamp = log.split(":")
            func, timestamp = int(func), int(timestamp)
            
            if type == 'start':
                if stack:
                    res[stack[-1]] += timestamp - pre_time
                stack.append(func)
                pre_time = timestamp
            else:
                # 这两部很关键 pre_time = timestamp + 1是我没有想到的。
                # 你可以想象成每一个时间都是有准确节点的。
                # 在5结束的时候其实就是相当于在6开始的时候结束，所以要在previous time的基础上加1
                res[stack.pop()] += timestamp - pre_time + 1
                pre_time = timestamp + 1
            
        return res
    
    def call_function(self):
        self.exclusiveTime(2, ["0:start:0","1:start:2","1:end:5","0:end:6"])