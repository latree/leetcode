from typing import BinaryIO, List

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
#         counter  = 0
#         i = 1
#         j = 0
#         while counter < k:
#             if j < len(arr) and i == arr[j]:
#                 j += 1    
#             else:
#                 counter += 1
#                 if counter == k:
#                     return i
#             i += 1

#         return i - 1


    # # 第二遍心得
    # # 上面的方法是brute force， 下面的方法是用Binary search
    # def findKthPositive(self, arr: List[int], k: int) -> int:
    #     # 这道题不是标准的套公式，有很多地方不一样
    #     # 1. while left< =right,不是while left < right
    #     #     这样在left 和right相等的时候会再一次进入循环
    #     # 2. 判断条件以后，公式是left = mid + 1 和 right = mid
    #     #     但是这题是left = mid + 1 和 right = mid - 1
    #     #     这样在两个相等的时候才不会错过 最左边的idx 符合这个条件（arr[mid] - (mid + 1) < k）的idx。 
    #     # 请以这个例子为例来印证上述两个观点。
    #     # k = 5
    #     # 1 2 3 4 5
    #     # 2 3 4 7 11
    #     left, right = 0, len(arr) - 1
    #     while left <= right:
    #         mid = left + (right - left) // 2
            
    #         if arr[mid] - (mid + 1) < k:
    #             left = mid + 1
    #         else:
    #             right = mid - 1
                
    #     left_over = k - (arr[right] - right - 1)
    #     return arr[right] + left_over


# 第三遍
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            
            if arr[mid] - mid - 1 < k:
                left = mid + 1
            
            else:
                right = mid - 1
        
        # 这道题直接用idx 来return 会更直观一些。我的第一个方法想复杂了
        return left + k