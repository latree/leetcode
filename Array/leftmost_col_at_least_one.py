from Data_Structure import binary_matrix
from Data_Structure.binary_matrix import BinaryMatrix
from typing import List
import math

class leftMostColumnWithOne:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        # def bin_search(matrix: BinaryMatrix, row: int, col: int) -> int:
        #     left, right = 0,  col - 1
        #     while left < right:
        #         mid = (left + right) // 2
        #         if matrix.get(row, mid) == 0:
        #             left = mid + 1
        #         else:
        #             right = mid
            
        #     return left if matrix.get(row, left) == 1 else math.inf

        # [row, col] = binaryMatrix.dimensions()
        # min_idx = math.inf
        # for i in range(row):
        #     left_most_idx = bin_search(binaryMatrix, i, col)
        #     min_idx = min(min_idx, left_most_idx)

        # return min_idx if min_idx != math.inf else -1





# [
# [0,0,0,1],
# [0,0,1,1],
# [0,1,1,1]
# ]

# 第二次刷：心得很值得一看
#         # Solution 1: improvement based on brute force solution
#         # 这个是brute force 第一层improvement的solution
#         # brute force 就是iterate 每一行每一列然后找到第一个1的位置，从而找到最靠左的col值
#         # 这个improve solution就是对于每一行在找1的时候不是单纯的iterate，而是用二分法找到最靠左的1。
#         # 从而减少很多iteration
        
#         rows, cols = binaryMatrix.dimensions()
#         res = math.inf
        
#         for i in range(rows):
#             left, right = 0, cols - 1
#             while left < right:
#                 mid = left + (right - left) // 2
#                 if binaryMatrix.get(i, mid) == 0:
#                     left = mid + 1
#                 else:
#                     right = mid
            
#             if binaryMatrix.get(i, left) == 1:
#                 res = min(res, left)

#         return res if res != math.inf else -1


        # # solution 2: another improvement based on solution 1
        # # 这个解法是在solution 1 上的一个improvement。
        # # solution 1 是对每一个row都做一次binary search。每一次的起始点和终止点都是row 的0 到len(row) - 1
        # # 其实有很多重复的操作是可以“剪枝”的。
        # # 1. 如果之前已经找到了一个res 的left most col。对于接下来的row需要做以下的“剪枝”处理
        # #     1.a 另外如果当前的res ==0 那么也可以直接return，因为没有比col == 0 再靠左的答案了
        # #     1.b 可以check 当前row的 res-1 的col是不是0，如果是0 可以直接skip，因为当前row 不可能比之前得到的res的row有更靠左的答案
        # #     1.c 如果这行没有被skip，那么我们二分法的右起点也可以设置为res，而不是len(row) - 1
        
        # rows, cols = binaryMatrix.dimensions()
        # res = math.inf
        
        # for i in range(rows):
        #     if res != math.inf:
        #         if res > 0:
        #             if binaryMatrix.get(i, res - 1) == 0:
        #                 continue
        #         else:
        #             return res
        #     left = 0
        #     right = cols - 1 if res == math.inf else res
        #     while left < right:
        #         mid = left + (right - left) // 2
        #         if binaryMatrix.get(i, mid) == 0:
        #             left = mid + 1
        #         else:
        #             right = mid

        #     if binaryMatrix.get(i, left) == 1:
        #         res = min(res, left)

        # return res if res != math.inf else -1


        m, n = binaryMatrix.dimensions()
        i, j = 0, n - 1
        
        def row_search(col):
            left, right = 0, m - 1
            while left <= right:
                val = binaryMatrix.get(left, col)
                if val == 1:
                    return True
                left += 1
            return False
            
            
        
        while i <= j:
            mid = i + (j - i) // 2
            
            if row_search(mid):
                j = mid - 1
            else:
                i = mid + 1
        
        return -1 if i == n else i 


    def call_function(self) -> None:
        return self.leftMostColumnWithOne(BinaryMatrix(3,4))