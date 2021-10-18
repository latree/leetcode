from typing import List

class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
#         # 拿l = 0, r = 1举例，第一个iteration，mid=left=0 if valide, 那么left必须等于mid+1如果不等于mid + 1 进入下个循环的时候，mid还是=left=0.那就出不了循环了。
#         # 同理右边也是一样的
#         left, right = 1, max(ribbons)
#         candidate = 0
#         while left <= right:
#             mid = left + (right - left) // 2
            
#             if self.valide(mid, ribbons, k):
#                 candidate = mid
#                 left = mid + 1
#             else:
#                 right = mid - 1
        
#         return candidate
                
    
    
#     def valide(self, length, ribbons, k) -> bool:
#         count = 0
        
#         for ribbon in ribbons:
#             count += ribbon // length
        
#         return count >= k




# 第二遍
        # 这道题其实是在找右边界。因为如果 cut_count(ribbons, mid) == k 刚好有符合这个条件的mid
        # 不一定是最大的要找length。所以就转化成了找右边界的问题。
        def cut_count(ribbons, mid):
            count = 0
            for ribbon in ribbons:
                count += ribbon // mid
            return count
        
        left, right = 1, max(ribbons)
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if cut_count(ribbons, mid) == k:
                left = mid + 1
            
            elif cut_count(ribbons, mid) > k:
                left = mid + 1
            elif cut_count(ribbons, mid) < k:
                right = mid - 1
        # 如果没找到直接return 0
        if right <= 0:
            return 0
        return right