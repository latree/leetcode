from typing import List

class findBuildings:
    def findBuildings(self, heights: List[int]) -> List[int]:
        # if len(heights) == 1:
        #     return [0]
        # slow, fast = len(heights) - 1, len(heights) - 2 
        # building_idx = [slow]
        # while fast >=0:
        #     if heights[fast] > heights[slow]:
        #         building_idx.append(fast)
        #         slow = fast
                
        #     fast -= 1

        # return building_idx[::-1]


        # 第二遍
        # 这个其实就是用到monotonic stack 的概念。只往stack append 比当前最大值还要再大的值
        max_height = 0
        res = []
        for i in range(len(heights) -  1, -1, -1):
            if heights[i] > max_height:
                res.append(i)
                max_height = heights[i]
            
        return res[::-1]