class reverseBits:
    def reverseBits(self, n: int) -> int:
        # # solution 1: for each bit from right right to left reverse it
        # ret, power = 0, 31
        # while n:
        #     ret += (n & 1) << power
        #     n >>= 1
        #     power -= 1
        
        # return ret

        # # solution 2: reverse bit per byte
        # def reverseByte(byte, cache):
        #     if byte not in cache:
        #         cache[byte] = (byte * 0x0202020202 & 0x010884422010) % 1023
        #     return cache[byte]
        # ret, power = 0, 24
        # cache = {}
        # while n:
        #     ret += reverseByte(n & 0xff, cache) << power
        #     n >>= 8
        #     power -= 8
        # return ret
        
        # solution 3 divide and conquer 
        n = (n >> 16) | (n << 16)
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
        return n