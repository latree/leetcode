from typing import Counter, List, Reversible

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
#         # 这道题的边界非常容易错， 有好几个边界有很tricky
#         def format_range(lower, upper):
#             if lower == upper:
#                 return str(lower)
            
#             return str(lower) + "->" + str(upper)
        
#         res = []
#         # 下面都是以 nums =[0,1,3,50,75], lower = 0, upper = 99 为例子
#         # prev, cur 代表的是数组里的数，所以区间应该是prev + 1, cur - 1
#         # 之所以定义prev = lower - 1是因为在最开始 在后面prev + 1的时候就可以涵盖lower了
#         prev = lower - 1
#         # 这里也很tricky，这里多做了一次循环
#         # 如果没有那个+1 循环那么 答案["2","4->49","51->74","76->99"] 最后一个区间就会丢失 也就是"76->99" 会丢失
#         for i in range(len(nums) + 1):
#             cur = nums[i] if i < len(nums) else upper + 1

#             if prev + 1 <= cur - 1:
#                 res.append(format_range(prev + 1, cur - 1))
#             prev = cur
#         return res

# # [0,1,3,50,75], lower = 0, upper = 99

        # 第二遍：
        # 这个方法比上面的方法好。思路更清晰
        # 原理：
        # 1. 首先遍历nums 然后只要是nums[i] 和nums[i + 1]之差大于1 的那么就会产生一个区间，把这个区间append 到res
        # 2. 之后，如果nums是空，那么[lower, upper]就是missing 区间
        # 3. 如果lower 到nums[0] 有missing那么就append到最前面
        # 4. 如果nums[-1]到upper 有missing 那么就append到最后面
        def format_range(lower, upper):
            if lower == upper:
                return str(lower)
            
            return str(lower) + "->" + str(upper)
        
        res = []
        
        for i in range(len(nums) - 1):
            pre = nums[i] 
            cur = nums[i + 1]
            if pre + 1 != cur:
                res.append(format_range(pre + 1, cur - 1))

        if not nums:
            temp = format_range(lower, upper)
            return [temp]
        
        if lower < nums[0]:
            temp = format_range(lower, nums[0] - 1)
            res = [temp] + res
        
        if nums[-1] < upper:
            temp = format_range(nums[-1] + 1, upper)
            res = res + [temp]
        return res