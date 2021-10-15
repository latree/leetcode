from typing import List

class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:        
        res = []
        i, j = 0, 0 
        while i < len(encoded1) and j < len(encoded2):
            val = encoded1[i][0] * encoded2[j][0]
            freq = min(encoded1[i][1], encoded2[j][1])
            if res and res[-1][0] == val:
                res[-1][1] += freq
            else:
                res.append([val, freq])
            encoded1[i][1] -= freq
            encoded2[j][1] -= freq
            
            if encoded1[i][1] ==0:
                i += 1
            if encoded2[j][1] ==0:
                j += 1
        return res