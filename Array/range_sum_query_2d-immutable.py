from typing import List

class NumMatrix:
    # # 大格子减小格子
    # def __init__(self, matrix: List[List[int]]):
    #     if not matrix or not matrix[0]:
    #         return
    #     N = len(matrix) + 1
    #     M = len(matrix[0]) + 1
    #     self.dp = [ [ 0 for i in range(M) ] for j in range(N) ]
        
    #     for r in range(len(matrix)):
    #         for c in range(len(matrix[0])):
    #             self.dp[r + 1][c + 1] = matrix[r][c] + self.dp[r + 1][c] + self.dp[r][c + 1] - self.dp[r][c]
        
    # def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
    #     return self.dp[row2 + 1][col2 + 1] - self.dp[row1][col2 + 1] - self.dp[row2 + 1][col1] + self.dp[row1][col1]


# # 第二遍
#     def __init__(self, matrix: List[List[int]]):
#         if not matrix or not matrix[0]:
#             return
#         N = len(matrix) + 1
#         M = len(matrix[0]) + 1
#         self.prefix_sum = [[0 for _ in range(M)] for _ in range(N)]
        
#         for i in range(N - 1):
#             for j in range(M - 1):
#                 # 这里有一出会让人非常容易混淆。就是为什么加的是matrix[i][j]而不是matrix[i + 1][j + 1]是因为prefix_sum多加了一个row 和一个col。所以
#                 # 这里的matrix[i][j] 其实就是相当于prefix_sum[i + 1][j + 1]
#                 self.prefix_sum[i + 1][j + 1] = matrix[i][j] + self.prefix_sum[i][j + 1] + self.prefix_sum[i + 1][j] - self.prefix_sum[i][j]
        
        
#     def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
#         return self.prefix_sum[row2 + 1][col2 + 1] - self.prefix_sum[row1][col2 + 1] - self.prefix_sum[row2 + 1][col1] + self.prefix_sum[row1][col1]


# 第三遍：
    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return 
        row = len(matrix) + 1 
        col = len(matrix[0]) + 1
        self.prefix_sum = [[0 for _ in range(col)] for _ in range(row)]
        
        for i in range(row - 1):
            for j in range(col - 1):
                self.prefix_sum[i + 1][j + 1] = matrix[i][j] + self.prefix_sum[i][j + 1] + self.prefix_sum[i + 1][j] - self.prefix_sum[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        # *******  important  ****************
        # 做的时候弄混了一个概念。把(r, c) 概念混淆成了网格的**棱** 的坐标，这是错的！！（r，c）代表的是一个matrix 数字的坐标。！！！
        # 所以我错误的写成了 return self.prefix_sum[row2 + 1][col2 + 1] - self.prefix_sum[row1 + 1][col2 + 1] - self.prefix_sum[row2 + 1][col1 + 1] + self.prefix_sum[row1 + 1][col1 + 1]    
        return self.prefix_sum[row2 + 1][col2 + 1] - self.prefix_sum[row1][col2 + 1] - self.prefix_sum[row2 + 1][col1] + self.prefix_sum[row1][col1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)