from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # i  = 1 
        # N = len(flowerbed)
        # # 使用一个temp是为了让后面check每一个idx 的时候每个case的一致性。这样就不用为了idx out
        # # of range 而烦扰了。
        # temp = [0] + flowerbed + [0]
        # # 这里应该是N + 1， 因为我在开始和结束的时候都加了一个0， 总共加了2个0，从i = 1开始的话，如果到最后的时候i + 2 就会超出idx（如果是i<N 的情况）
        # # temp = [0, 1,0,0,0,1,0,0, 0]
        # # 2
        # # i=5 就是这种情况 i+=2 以后是i-7 依旧是flowerbed 里的最后一个元素，但是如果是i<N那么就直接跳出循环了
        # while i < N + 1:
        #     if not temp[i]:
        #         if not temp[i - 1] and not temp[i + 1]:
        #             temp[i] = 1
        #             n -= 1
        #             i += 2
        #         elif not temp[i - 1]:
        #             i += 2
        #         elif not temp[i + 1]:
        #             i += 1
        #         else:
        #             i += 2
        #     else:
        #         i += 2
        # return n <= 0
    


    # 第二遍：
        # 使用一个temp是为了让后面check每一个idx 的时候每个case的一致性。这样就不用为了idx out
        # of range 而烦扰了。
        # temp = [0] + flowerbed + [0]
        # 这里应该是N + 1， 因为我在开始和结束的时候都加了一个0， 总共加了2个0，从i = 1开始的话，如果到最后的时候i + 2 就会超出idx（如果是i<N 的情况）
        # temp = [0, 1,0,0,0,1,0,0, 0]
        # 2
        # i=5 就是这种情况 i+=2 以后是i-7 依旧是flowerbed 里的最后一个元素，但是如果是i<N那么就直接跳出循环了
        
        # 具体分析的四种情况：
        # [0,0,0]
        # [0,0,1]
        # [1,0,0]
        # [1,0,1]

        i = 1
        N = len(flowerbed)
        
        temp = [0] + flowerbed + [0]
        
        while i < N + 1:
            # 当前位置是空
            if not temp[i]:
                # [0,0,0]
                if not temp[i - 1] and not temp[i + 1]:
                    n -= 1
                    temp[i] == 1
                    i += 2
                # [0,0,1]
                elif not temp[i - 1] and temp[i + 1]:
                    i += 2
                # [1,0,0]
                elif temp[i - 1] and not temp[i + 1]:
                    i += 1
                # [1,0,1]
                else:
                    i += 2
            else:
                i += 2
        
        return n <= 0