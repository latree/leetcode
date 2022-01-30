from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
# #         这里稍微有个变形。
# #         1. 这里为什么用binary search？因为一旦判断了mid 和mid+1的大小我们就能缩小一半的搜索区域，即使array不是一个sorted array。
# #         这也是从侧面印证了，并不是不是sorted array就不能使用binary search。主要还是在看能不能找到一个条件后就可以缩小左半部或者右半部的搜索区域。如果符合就是可以用binary search
# #         2. 如果mid 小于mid+1 那么必然在右侧有一个peak。反之在左侧也会有一个peak
        
#         l, r = 0, len(nums) - 1
#         while l <= r:
#             mid = l + (r - l) // 2
#             if mid < len(nums) - 1:
#                 if nums[mid] > nums[mid + 1]:
#                     r = mid - 1
#                 elif nums[mid] < nums[mid + 1]:
#                     l = mid + 1
#                 elif nums[mid] == nums[mid + 1]:
#                     l = mid + 1
#             else:
#                 # 这里比较好理解，如果mid+1不存在，那么说明mid已经在最右侧了。所以mid 是最大值
#                 return mid
#         # 3. 这里我已经用了闭环的搜索范围，那么为什么最后return的是left 而不是right呢？
#         # 因为如果while循环结束那么一定意味着现在left 和right是一个left > right的关系。
#         # 其次，如果想一下：                 
#         # if nums[mid] > nums[mid + 1]:
#         #     r = mid - 1
#         # 如果mid 就是那个峰值。那么r直接等于mid-1，那么就会刚好错过这个峰值。所以不应该是r，而是l
#         return l

        # 第二遍
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = l + (r - l) // 2
            if mid < len(nums) - 1:
                if nums[mid] <= nums[mid + 1]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                return mid
        
        return l