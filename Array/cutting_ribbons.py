from typing import List

class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        # 拿l = 0, r = 1举例，第一个iteration，mid=left=0 if valide, 那么left必须等于mid+1如果不等于mid + 1 进入下个循环的时候，mid还是=left=0.那就出不了循环了。
        # 同理右边也是一样的
        left, right = 1, max(ribbons)
        candidate = 0
        while left <= right:
            mid = left + (right - left) // 2
            
            if self.valide(mid, ribbons, k):
                candidate = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return candidate
                
    
    
    def valide(self, length, ribbons, k) -> bool:
        count = 0
        
        for ribbon in ribbons:
            count += ribbon // length
        
        return count >= k
    