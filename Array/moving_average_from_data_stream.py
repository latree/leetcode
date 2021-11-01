from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        self.queue = deque()
        self.size = size

    def next(self, val: int) -> float:
        divisor = len(self.queue) + 1
        if len(self.queue) >= self.size:
            self.queue.popleft()
            divisor = self.size
        self.queue.append(val)
        
        return sum(self.queue) / divisor
                    

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)