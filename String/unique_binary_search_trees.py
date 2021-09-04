class Solution:
    def __init__(self):
        self.memo = {}
        
    def numTrees(self, n: int) -> int:
        def count(low, high) -> int:
            if low > high:
                return 1
            
            if (low, high) in self.memo:
                return self.memo.get((low, high))
            
            res = 0
            # 右边界必须是i+1因为i也可以分割到左子树是low 到high，右子树是空的情况
            for i in range(low, high + 1):
                left = count(low, i - 1)
                right = count(i + 1, high)
                
                res += left * right
            self.memo[(low, high)] = res
            return res
        
        
        return count(1, n)
        