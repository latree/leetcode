class Solution:
    def maximumSwap(self, num: int) -> int:
        # num_lst = [ch for ch in str(num)]
        # idx_map = {}
        # for i, item in enumerate(num_lst):
        #     idx_map[item] = i
        
        # sorted_lst = sorted(num_lst.copy())[::-1]

        # to_swap = False
        # i = 0
        # while not to_swap and i < len(num_lst):
        #     if num_lst[i] != sorted_lst[i]:
        #         to_swap_idx = idx_map[sorted_lst[i]]
        #         num_lst[i], num_lst[to_swap_idx] = num_lst[to_swap_idx], num_lst[i]
        #         to_swap = True
        #     else:
        #         i += 1
        # return int("".join(num_lst))



        # 第二遍：
        # 这里方法非常巧妙。
        # 1. 从后往前的遍历很巧妙。 从后往前的遍历解决了找最大值，并且记录swap 的idx的问题
        # 2. 从后往前的遍历还保证了每一次需要swap的idx 都是最左侧（最高位的位置）需要swap的数字的高位。
        # 原理：
        # 1. 只要发现一个新的最大值，就去update 最大值和最大值的idx
        # 2. 只要发现当前的值小于最大值，那么就是potential 需要swap的对象，那么就要记录当前的最大值的idx 和当前值的idx 作为potential swap的idx对象
        nums = [int(i) for i in str(num)]
        c_max = -1
        max_idx = 0
        
        last_max_idx, last_min_idx = 0, 0
        
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > c_max:
                c_max = nums[i]
                max_idx = i
            elif nums[i] < c_max:
                last_min_idx = i
                last_max_idx = max_idx
            
        
        nums[last_min_idx], nums[last_max_idx] =  nums[last_max_idx], nums[last_min_idx]
        res = []
        for i in nums:
            res.append(str(i))
        return int("".join(res))