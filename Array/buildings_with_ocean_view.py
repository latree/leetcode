from typing import List

class findBuildings:
    def findBuildings(self, heights: List[int]) -> List[int]:
        if len(heights) == 1:
            return [0]
        slow, fast = len(heights) - 1, len(heights) - 2 
        building_idx = [slow]
        while fast >=0:
            if heights[fast] > heights[slow]:
                building_idx.append(fast)
                slow = fast
                
            fast -= 1

        return building_idx[::-1]
