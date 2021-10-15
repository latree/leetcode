from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
#         # ****** 这道题花了我非常多的时间
#         # 先说这个解法的思路：
#         # 就是先用二分法找到离x 最近的数
#         # 然后设置两个指针分别从里到外扩散 知道k个都closet都找到。
#         # 思路跟简单，但是在implement的时候边界非常容易出错
#         # 下面的comments 会说到哪里总是出错
#         left, right = 0 , len(arr) - 1
        
#         j = 0
#         res = []
#         while left < right:
#             mid = left + (right - left) // 2
#             if arr[mid] == x:
#                 j = mid
#                 break
#             # 如果x 在mid 左边我们需要查看x是不是在mid 和mid-1 的中间。如果正好在他们中间那么我们可以直接
#             # return找到的就是最小的值。刚开始的时候思路不请，在大于小于的符合上弄错。
#             if x < arr[mid]:
#                 if mid > 0 and x > arr[mid - 1]:
#                     j = mid if abs(arr[mid] - x) <= abs(arr[mid - 1] - x) else mid - 1
#                     break
#                 # 这里之所以是right == mid 而不是mid - 1， 下面是left = mid 原因是如果mid==0
#                 # 那么mid-1 就是right=-1，那么在line 36 出现的j=right 就会有out of idx 问题
#                 # right = mid：
#                 # 比如这个case：
#                 # [1,2,3,4,5]
#                 # k:4
#                 # x:-1
#                 right = mid
#             # 同理如果x 在mid 右边我们需要查看x是不是在mid 和mid+1 的中间。如果正好在他们中间那么我们可以直接
#             # return找到的就是最小的值。刚开始的时候思路不请，在大于小于的符合上弄错。
#             else:
#                 if mid < len(arr) - 1 and arr[mid + 1] > x:
#                     j = mid if abs(arr[mid] - x) <= abs(arr[mid + 1] - x) else mid + 1
#                     break
#                 # 如果x 在最右边的那个数还要往右，那么right 会一直不动，然后left 挪到len(arr)- 1
#                 # 即使left+1也没关系，因为下面的代码不会再用到left了
#                 left = mid + 1
        
        
#         if j == 0:
#             j = right
#             i = right - 1
#         else:
#             i = j - 1
#         left_over = k
#         while left_over > 0 and 0 <= i < len(arr) and 0 <= j < len(arr):
#             if abs(arr[i]-x) <= abs(arr[j]-x):
#                 res.append(arr[i])
#                 i -= 1
#             else:
#                 res.append(arr[j])
#                 j += 1
#             left_over -= 1
        
#         while j < len(arr) and left_over > 0:
#             res.append(arr[j])
#             j += 1
#             left_over -= 1
            
#         while i >= 0 and left_over > 0:
#             res.append(arr[i])
#             i -= 1
#             left_over -= 1
            
#         return sorted(res)

        
#         *****目标是找k个数，那么arr已经是sorted，那么我们其实就在arr里找一个k 的window就是答案
#         注意，只要我们找到左边界，那么答案就是arr[left:left + k]
#         左边界的最大值只有可能是len(arr) - k 要不然就不够k个element了，所以right = len(arr) - k
        
        left, right = 0, len(arr) - k
        while left < right:
            mid = left + (right - left) // 2
            # 如果，x 靠近mid 那么答案就不可能是mid + k 以后的element。因为如果x靠近mid，那么左边界
            # 必须从mid-y开始。y是变量。 那mid-y一定比mid 小，所以mid+k已经之后的elemnet都不会reach到。所以我们要avoid这些element 所以要move right to mid
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        
        return arr[left:left + k]