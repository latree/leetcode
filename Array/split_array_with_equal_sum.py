from typing import List

class Solution:
    def splitArray(self, nums: List[int]) -> bool:
        # 原理
        # 固定j的值，然后从左侧iterate i来找到符合prefix_sum[i - 1] == prefix_sum[j - 1] - prefix_sum[i]的情况，prefix_sum并加到set 里
        # 从右侧iterate k来找到符合 prefix_sum[n - 1] - prefix_sum[k] == prefix_sum[k - 1] - prefix_sum[j] 的情况。
        # 因为所有值都相等，所以如果prefix_sum 的值在left_set里面那么就找到了valid solution了
        prefix_sum = []
        pre_sum = 0
        n = len(nums)
        for i in range(n):
            pre_sum += nums[i]
            prefix_sum.append(pre_sum)
        
        # 注意j的起始和结束。因为i + 1 < j and i > 0 那么j最小能等于3. 同理。因为j + 1 < k < n - 1那么j 最大就能等于n - 4
        for j in range(3, n - 3):
            left_set = set()
            
            # i的边界也是同理，因为 i > 0 所以i从1 开始。因为i + 1 < j那么i最大等于j - 2
            for i in range(1, j - 1):
                if prefix_sum[i - 1] == prefix_sum[j - 1] - prefix_sum[i]:
                    left_set.add(prefix_sum[i - 1])
            # k的边界也是同理，因为j + 1 < k < n - 1那么k起始是j + 2， 最大等于n - 2
            for k in range(j + 2, n - 1):
                if prefix_sum[n - 1] - prefix_sum[k] == prefix_sum[k - 1] - prefix_sum[j] and prefix_sum[k - 1] - prefix_sum[j] in left_set:
                    return True
        
        return False
                    