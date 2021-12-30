from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
# #         原理：
# #         1.每一个对角线的r，c之和是相等的。
# #         2.zigzag 的模式，就是单数相反，双数为正
        
# #         implement：
# #         1. 建立一个map
# #         diagonal = {i+j: [mat[i][j], ....]}
# #         2. 然后iterate 每一个map的entry， k为单数相反，k为整数直接append
        
#         diagonal = {}
#         res = []
#         for i in range(len(mat)):
#             for j in range(len(mat[0])):
#                 if i + j not in diagonal:
#                     diagonal[i + j] = [mat[i][j]]
#                 else:
#                     diagonal[i + j].append(mat[i][j])
        
#         for k, v in diagonal.items():
#             if k % 2 == 0:
#                 v = v[::-1]
#             for i in v:
#                 res.append(i)
        
#         return res


# 第二遍
        # 如果是同一个对角线里的元素， 那么i+j 相等
        # 最后只要根据i+j 是单数还是双数做一个反转就可以了
        m = len(mat)
        n = len(mat[0])
        dia = {}
        for i in range(m):
            for j in range(n):
                if i + j not in dia:
                    dia[i + j] = [mat[i][j]]
                else:
                    dia[i + j].append(mat[i][j])
        
        res = []
        for k, v in dia.items():
            if k % 2 != 0:
                res += v
            else:
                res += v[::-1]
        
        return res