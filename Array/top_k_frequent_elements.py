from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count_map = {}
        # for num in nums:
        #     count = count_map.get(num, [num, 0])[1] + 1
        #     count_map[num] = [num, count]
        
        # res = heapq.nlargest(k, count_map.values(), key=lambda e:e[1])
        # return [item[0] for item in res]
        
# 第二遍
        count = {}
    
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        heap_list = []
        
        for num, freq in count.items():
            heapq.heappush(heap_list, (freq, num))
        
        res = list(heapq.nlargest(k, heap_list))
        return [ele[1] for ele in res]