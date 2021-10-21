from typing import List
import math
import heapq

class kClosest:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # solution 1:
        # points_map = {}
        # heap_list = []
        # for point in points: 
        #     cur_distance = math.sqrt(point[0] ** 2 + point[1] ** 2)
        #     if cur_distance not in points_map:
        #         points_map[cur_distance] = [point]
        #     else:
        #         points_map[cur_distance].append(point)
        #     heapq.heappush(heap_list, cur_distance)
        
        # heapq.heapify(heap_list)
        # res = []
        # while len(res) < k:
        #     distance = heapq.heappop(heap_list)
        #     res += points_map[distance]
        # return res

        # # solution 2:
        # heap = []
        # for x, y in points:
        #     distance = -(x**2 + y**2)
        #     if len(heap) == k:
        #         heapq.heappushpop(heap, (distance, x, y))
        #     else:
        #         heapq.heappush(heap, (distance, x, y))
        
        # return [[x,y] for (distance, x, y) in heap]



        # 第二遍
        m = len(points)
        heap_list = []
        res = []
        for i in range(m):
            r, c = points[i]
            dist = r**2 + c**2
            heapq.heappush(heap_list, (dist, r, c))
        
        temp = list(heapq.nsmallest(k, heap_list))
        for i in range(len(temp)):
            res.append([temp[i][1], temp[i][2]])
        return res