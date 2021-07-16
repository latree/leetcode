from typing import List
import random

class MinStack:
    # # solution 1: two stack
    # def __init__(self):
    #     """
    #     initialize your data structure here.
    #     """
    #     self.main_stack = []
    #     self.min_stack = []

    # def push(self, val: int) -> None:
    #     self.main_stack.append(val)
    #     if not self.min_stack or val <= self.min_stack[-1]:
    #         self.min_stack.append(val)

    # def pop(self) -> None:
    #     if self.main_stack[-1] == self.min_stack[-1]:
    #         self.min_stack.pop(-1)
    #     self.main_stack.pop(-1)
        
    # def top(self) -> int:
    #     return self.main_stack[-1]

    # def getMin(self) -> int:
    #     return self.min_stack[-1]

    # solution 2: two stack with improvement
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.main_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.main_stack.append(val)
        if not self.min_stack or val < self.min_stack[-1][0]:
            self.min_stack.append([val, 1])
        elif val == self.min_stack[-1][0]:
            self.min_stack[-1][1] += 1
            
    def pop(self) -> None:
        if self.main_stack[-1] == self.min_stack[-1][0]:
            self.min_stack[-1][1] -= 1
        if self.min_stack[-1][1] == 0:
            self.min_stack.pop()
        self.main_stack.pop()
        
    def top(self) -> int:
        return self.main_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1][0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()