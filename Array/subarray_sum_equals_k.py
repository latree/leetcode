from typing import List

class subarraySum:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # # solution 1: store the previous calculation
        # # Time: O(n**2)
        # # Space: O(n)
        # sum_array = []
        # cur_sum = 0
        # for i in range(len(nums)):
        #     cur_sum += nums[i]
        #     sum_array.append(cur_sum)
        
        # res = 0
        # for i in range(len(nums)):
        #     if sum_array[i] == k:
        #         res +=1
        #     for j in range(i + 1, len(nums)):
        #         cur_window_sum  = sum_array[j] - sum_array[i]
        #         if cur_window_sum == k:
        #             res += 1
        # return res
    
        # # solution 2: hashmap
        # # Time: O(n)
        # # Space: O(n)
        # # hash_map key：当前sum的总值。value是这个sum总值出现的次数
        # # 为什么要用sum - k？：如果sum - k 出现在hash_map中就说明之前的sum 和当前的sum相差k，那么
        # # 就是从之前的index 到现在index的sub window 之和就是k。所以就找到了sub array
        # hash_map = {}
        # hash_map[0] = 1
        # cur_sum = 0
        # count = 0
        # for i in range(len(nums)):
        #     cur_sum += nums[i]
        #     cur = cur_sum - k
        #     if cur in hash_map:
        #         count += hash_map.get(cur)
        #     hash_map[cur_sum] = hash_map.get(cur_sum, 0) + 1
        # return count

# 第二遍
        # 这里用到了形成一个累加的array，在不少题目当中累加的array 都是很有用的
        # 尤其是在sum的题型里面。
        sum_map = {}
        cur_sum = 0
        # ******* important *******
        # 必须要有这个sum_map[0] = 1. 比如在第一个找到sum之和是k的时候 cur_sum - k 就是0， 如果没有，就不在这个dict里面。count就会少一个
        sum_map[0] = 1
        count = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            minus_k = cur_sum - k
            if minus_k in sum_map:
                # 为什么count的是 sum_map[minus_k]？
                # 因为是寻找到当前idx的sum减去k以后是不是之前的sum是等于这个值的。
                # 如果存在那么之前那个sum的idx是i，现在的idx是j。就代表i-j的区间
                # sum 是等于k的。
                
                # 另外有可能能出现当前的这个minus_k有可能有好几种情况都等于都是用到minus_k以后的idx
                # 所以每次要加sum_map[cur_sum] 值。这样才能得到总数
                count += sum_map[minus_k]
            sum_map[cur_sum] = sum_map.get(cur_sum, 0) + 1
        
        return count

    def call_function(self) -> None:
        print(self.subarraySum([1, 1, 1], 2))
        