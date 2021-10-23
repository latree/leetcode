from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # ************ important *****************
        # 这道题在做第二遍的时候还是有点没弄明白
        # 这道题原理是：
        # 每一次得到cur_idx_sum 以后做一个mod k， 如果之后的cur_idx_sum mode k 得到的结果之前已经得到了说明这两个cur_idx_sum之间
        # 的subarray 得到的sum 是可以被k 整除的。

        # mod_map={0:-1} 初始值必须要有因为如果没有这个初始值那么在nums[:i] 就是k的倍数的时候就会认定为False，因为算法里必须要和之前的
        # sum 相比较。所以必须设立一个初始值这样就会包括num[:i]直接就是k的倍数的情况。
        # ****************** important **********************

        # Time: O(n)
        # Space: O(n) n 应该是mod k 最多可能出现的余数次数
        if k == 0:
            return False
        mod_map = {0:-1}
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            cur_mod = cur_sum % k
            if cur_mod not in mod_map:
                mod_map[cur_mod] = i
            else:
                if i - mod_map[cur_mod] >=2:
                    return True

        return False

    def call_function(self) -> None:
        self.checkSubarraySum([23,2,4,6,6], 7)