# ************** 记住**************
# 这是一个小的trick需要记住：这个循环是iterate一个matrix 右上半的部分
n = 4
for i in range(n - 2, -1, -1):
    for j in range(i + 1, n, 1):
        print((i, j))