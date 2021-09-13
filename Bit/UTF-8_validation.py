from typing import List

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        mask1 = 1 << 7
        mask2 = 1 << 6
        n_bytes = 0
        
        for num in data:
            mask = 1 << 7
            
            if n_bytes ==0:
                # So, we have taken a mask = 1 << 7 which is basically 10000000. We will make use of this mask and logically and it with the number to see if the bit at a particular position is set of not. We do this iteratively to check how many bits are set starting from the most significant bit (Remember, the integer might be too large but we should only process the 8 least significant bits of data.)
                while num & mask:
                    n_bytes += 1
                    mask = mask >> 1
                
                if n_bytes == 0:
                    continue
                if n_bytes == 1 or n_bytes > 4:
                    return False
                
            else:
                # The below code will simple use the mask1 to check if the most significant bit is set to 1 and the second most significant bit is set to 0. if this is not a case, then we return False.
                if not (num & mask1 and not (num & mask2)):
                    return False
            
            n_bytes -= 1
        return n_bytes == 0
                