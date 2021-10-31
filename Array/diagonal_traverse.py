from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
#         原理：
#         1.每一个对角线的r，c之和是相等的。
#         2.zigzag 的模式，就是单数相反，双数为正
        
#         implement：
#         1. 建立一个map
#         diagonal = {i+j: [mat[i][j], ....]}
#         2. 然后iterate 每一个map的entry， k为单数相反，k为整数直接append
        
        diagonal = {}
        res = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i + j not in diagonal:
                    diagonal[i + j] = [mat[i][j]]
                else:
                    diagonal[i + j].append(mat[i][j])
        
        for k, v in diagonal.items():
            if k % 2 == 0:
                v = v[::-1]
            for i in v:
                res.append(i)
        
        return res
