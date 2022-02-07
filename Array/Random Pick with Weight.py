class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sums = []
        cur_sum = 0 
        for weight in w:
            cur_sum += weight
            self.prefix_sums.append(cur_sum)
        self.total = cur_sum

    def pickIndex(self) -> int:
        target = self.total * random.random()
        left, right = 0, len(self.prefix_sums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            
            # 这里还开始的时候写错了。如果target 大于当前权重的边界值的时候
            # 我们应该果断忽略掉当前合格权重的左侧。因为这个target不可能掉在
            # 左侧那些权重值里
            if self.prefix_sums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()