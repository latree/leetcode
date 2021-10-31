from typing import List

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
#         group = {}
#         for r, row in enumerate(matrix):
#             for c, val in enumerate(row):
#                 if r-c not in group:
#                     group[r-c] = val
#                 else:
#                     if group[r-c] != val:
#                         return False
#         return True

# # [1, 2, 3, 4],
# # [5, 1, 2, 3],
# # [9, 5, 1, 2]


# # 00, 11, 22     1
# # 01, 12, 23     2
# # 02, 13,        3
# # 03             4


# # 10, 21         5
# # 20, 

        # 第二遍：
        # 这个是矩阵的性质。对角线的r，c 的差值是相等的

        group = {}
        
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if r-c not in group:
                    group[r-c] = val
                if r-c in group and val != group[r-c]:
                    return False
        
        return True