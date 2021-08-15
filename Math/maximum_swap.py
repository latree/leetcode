class Solution:
    def maximumSwap(self, num: int) -> int:
        num_lst = [ch for ch in str(num)]
        idx_map = {}
        for i, item in enumerate(num_lst):
            idx_map[item] = i
        
        sorted_lst = sorted(num_lst.copy())[::-1]

        to_swap = False
        i = 0
        while not to_swap and i < len(num_lst):
            if num_lst[i] != sorted_lst[i]:
                to_swap_idx = idx_map[sorted_lst[i]]
                num_lst[i], num_lst[to_swap_idx] = num_lst[to_swap_idx], num_lst[i]
                to_swap = True
            else:
                i += 1
        return int("".join(num_lst))