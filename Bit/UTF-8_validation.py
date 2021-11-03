from typing import List

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        # mask1 = 1 << 7
        # mask2 = 1 << 6
        # n_bytes = 0
        
        # for num in data:
        #     mask = 1 << 7
            
        #     if n_bytes ==0:
        #         # So, we have taken a mask = 1 << 7 which is basically 10000000. We will make use of this mask and logically 
        #         # and it with the number to see if the bit at a particular position is set or not. 
        #         # We do this iteratively to check how many bits are set starting from the most significant bit 
        #         # (Remember, the integer might be too large but we should only process the 8 least significant bits of data.)
        #         while num & mask:
        #             n_bytes += 1
        #             mask = mask >> 1
                
        #         if n_bytes == 0:
        #             continue
        #         if n_bytes == 1i or n_bytes > 4:
        #             return False
                
        #     else:
        #         # The below code will simple use the mask1 to check if the most significant bit is set to 1 
        #         # and the second most significant bit is set to 0. if this is not a case, then we return False.
        #         if not (num & mask1 and not (num & mask2)):
        #             return False
            
        #     n_bytes -= 1
        # return n_bytes == 0

        # 原理：
        # 1. 用mask 1000000, 01000000 来做与还看看第一位和第二位是1 还是0 
        # 2. 先来count n_bytes有几个，然后每过一个num 那么就n_bytes - 1。 最后看看count的n_bytes 和num的数量符不符合。不符合就是false
        # 3. n_bytes > 4 肯定是错误的，n_bytes==1 说明左边第一位是1 那么也是false
        # 4. 剩余的bytes 的前两位不是10 那就是false。
        mask1 = 1 << 7
        mask2 = 1 << 6
        n_bytes = 0

        for num in data:
            mask = 1 << 7
            
            if n_bytes == 0:    
                while num & mask:
                    n_bytes += 1
                    mask = mask >> 1

                if n_bytes == 0:
                    continue
                if n_bytes == 1 or n_bytes > 4:
                    return False
            else:
                if not (num & mask1 and not(num & mask2)):
                    return False
        
            n_bytes -= 1
        
        return n_bytes == 0