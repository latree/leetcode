
class num1Bits:
    def hammingWeight(self, n: int) -> int:
        # # solution 1: 每一位做一次 &。 
        # bits = 0
        # mask = 1

        # for i in range(32):
        #     if (n & mask) != 0:
        #         bits += 1
            
        #     mask <<= 1
        # return bits

        # solution 2:
        