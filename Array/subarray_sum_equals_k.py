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
    
        # solution 2: hashmap
        # Time: O(n)
        # Space: O(n)
        # hash_map key：当前sum的总值。value是这个sum总值出现的次数
        # 为什么要用sum - k？：如果sum - k 出现在hash_map中就说明之前的sum 和当前的sum相差k，那么
        # 就是从之前的index 到现在index的sub window 之和就是k。所以就找到了sub array
        hash_map = {}
        hash_map[0] = 1
        cur_sum = 0
        count = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            cur = cur_sum - k
            if cur in hash_map:
                count += hash_map.get(cur)
            hash_map[cur_sum] = hash_map.get(cur_sum, 0) + 1
        return count


    def call_function(self) -> None:
        print(self.subarraySum([1, 1, 1], 2))