from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:    
        # stack = []
        # pre_time = 0
        # res = [0] * n
        # for log in logs:
        #     func, type, timestamp = log.split(":")
        #     func, timestamp = int(func), int(timestamp)
            
        #     if type == 'start':
        #         if stack:
        #             res[stack[-1]] += timestamp - pre_time
        #         stack.append(func)
        #         pre_time = timestamp
        #     else:
        #         # 这两部很关键 pre_time = timestamp + 1是我没有想到的。
        #         # 你可以想象成每一个时间都是有准确节点的。
        #         # 在5结束的时候其实就是相当于在6开始的时候结束，所以要在previous time的基础上加1
        #         res[stack.pop()] += timestamp - pre_time + 1
        #         pre_time = timestamp + 1
            
        # return res
    

# # 第二遍
#         # stop of stack is the current fuction id
#         # pre_time 记录了当前stack上的最近的timestamp 时间。每新读一个log的时间都需要pre_time来计算当前stack上的function 跑了多久了
#         stack = []
#         res = [0] * n
#         pre_time = 0
#         for i in range(len(logs)):
#             cur_log = logs[i].split(":")
#             f_id, state, timestamp = int(cur_log[0]), cur_log[1], int(cur_log[2])
#             # 这里比较容易混淆。不管当前的log 和top of stack是不是同一个function。都不重要。
#             # 重要的是如果state是start 那么我们就要结算一下当前的top of stack的function run 了多久。
#             # 如果state是end 那么正好是当前的这个top of stack的function从开始run到结束了。那也要结算一些这个function run了多久，然后把这个function pop 出stack
#             if state == "start":
#                 if stack:
#                     res[stack[-1]] += timestamp - pre_time
#                 stack.append(f_id)
#                 pre_time = timestamp
#             else:
#                 res[stack[-1]] += timestamp - pre_time + 1
#                 stack.pop()
#                 pre_time = timestamp + 1
        
#         return res

# 第三遍：
        # 这道题总体的思路就是
        # 1. 每一次遇到 state是start时候要push func_id， 每次是end 时候pop func_id （这里跟括号题目其实是一样的）
        # 2. 处理time 计算的时候要注意。 因为start 和end time 的定义导致了下面这个小细节
        #     a. 有stack 存在并且是start state的时候说明新的func， 那么time 计算就直接当前time 减去pre_time
        #     b. end state 计算的时候需要 time - pre_time + 1, 而且pre_time 也要 time + 1
        res = [0] * n
        stack = []
        pre_time = 0
        for i in range(len(logs)):
            log = logs[i].split(":")
            func_id, state, time = int(log[0]), log[1], int(log[2])
            
            if state == 'start':
                if stack:
                    res[stack[-1]] += time - pre_time
                stack.append(func_id)
                pre_time = time
            else:
                res[stack[-1]] += time - pre_time + 1
                stack.pop()
                pre_time = time + 1
                    
        return res

    def call_function(self):
        self.exclusiveTime(2, ["0:start:0","1:start:2","1:end:5","0:end:6"])