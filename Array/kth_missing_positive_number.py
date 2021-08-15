from typing import List

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        counter  = 0
        i = 1
        j = 0
        while counter < k:
            if j < len(arr) and i == arr[j]:
                j += 1    
            else:
                counter += 1
                if counter == k:
                    return i
            i += 1

        return i - 1