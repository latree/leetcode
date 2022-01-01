from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # # 这道题其实最根本的意思是从max(weight) 到 sum(weights) 这个递增的数组里找出一个min weight
        # # 来符合ship within targeted days。
        # # 所以这就符合binary search的条件。从一个递增数组里面找到一个target。
        # def canship(cap, days):
        #     count = 0
        #     cur_cap = 0
        #     for weight in weights:
        #         if cur_cap + weight <= cap:
        #             cur_cap += weight
        #         else:
        #             count += 1
        #             cur_cap = weight
            
        #     if cur_cap != 0:
        #         count += 1
        #     return count <= days
                
        
        # left = max(weights)
        # right = sum(weights)
        
        # while left < right:
        #     mid = left + (right - left) // 2
        #     if canship(mid, days):
        #         right = mid
        #     else:
        #         left = mid + 1
        
        # return right

# 第二遍
        def check_cap(weight):
            days = 0
            temp_w = 0
            for i in range(len(weights)):
                if temp_w + weights[i] > weight:
                    days += 1
                    temp_w = weights[i]
                else:
                    temp_w += weights[i]
            return days + 1 if temp_w > 0 else days

        
        left, right = max(weights), sum(weights)
        
        # ********** important **********************
        # 注意这个等号和最后的return 是right + 1.
        # 如果这里有等号，那么left = mid + 1  and right = mid - 1
        # 那么就会出现一个问题，如果mid 刚好就是最后要的结果，那么check_cap(mid) == days
        # 那么right = mid - 1， 最后return right 就是错的了，因为mid正好就是结果，最后return的是mid - 1

        # 第一遍的写法就没有这样的问题。我现在认为二分法如果出错，还是得带具体的例子进去。至于什么样的例子要带入，还是得总结一下
        while left <= right:
            mid = left + (right - left) // 2
            
            if check_cap(mid) > days:
                left = mid + 1
            else:
                right = mid - 1
            
        return right + 1