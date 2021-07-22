class hammingDistance:
    def hammingDistance(self, x: int, y: int) -> int:
        # # solution 1: build in bit counting function
        # return bin(x ^ y).count('1')

        # # solution 2: count xor by self
        # xor = x ^ y
        # distance = 0
        # while xor:
        #     if xor & 1:
        #         distance += 1
        #     xor >>= 1
        # return distance

        # solution 3 Brian Kernighan's Algorithm
        xor = x ^ y
        distance = 0
        while xor:
            distance += 1
            xor &= xor - 1
        return distance
