from typing import Counter, List

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        # 这道题的边界非常容易错， 有好几个边界有很tricky
        def format_range(lower, upper):
            if lower == upper:
                return str(lower)
            
            return str(lower) + "->" + str(upper)
        
        res = []
        # 下面都是以 nums =[0,1,3,50,75], lower = 0, upper = 99 为例子
        # prev, cur 代表的是数组里的数，所以区间应该是prev + 1, cur - 1
        # 之所以定义prev = lower - 1是因为在最开始 在后面prev + 1的时候就可以涵盖lower了
        prev = lower - 1
        # 这里也很tricky，这里多做了一次循环
        # 如果没有那个+1 循环那么 答案["2","4->49","51->74","76->99"] 最后一个区间就会丢失 也就是"76->99" 会丢失
        for i in range(len(nums) + 1):
            cur = nums[i] if i < len(nums) else upper + 1

            if prev + 1 <= cur - 1:
                res.append(format_range(prev + 1, cur - 1))
            prev = cur
        return res

# [0,1,3,50,75], lower = 0, upper = 99

            
            
        