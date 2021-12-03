from typing import List
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # 这道题没有那么复杂。
        # 最好理解的方式是：
        # 有一个新的meeting要开始，那么就看当前已经在meeting的所有room最早的结束时间和
        # 新meeting的开始时间。如果正在进行的meeting的最早结束时间小于新meeting的开始时间
        # 那么就可以空（heappop）出一个meeting room， 然后新的meeting可以用那个room（heappush）。反之，直接用一个新的meeting room（heappush）
        
        if not intervals:
            return 0
        
        # heap
        free_rooms = []
        intervals.sort(key=lambda x: x[0])
        heapq.heappush(free_rooms, intervals[0][1])
        
        
        for interval in intervals[1:]:
            if free_rooms[0] <= interval[0]:
                heapq.heappop(free_rooms)
            
            heapq.heappush(free_rooms, interval[1])
        
        return len(free_rooms)
