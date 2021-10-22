from typing import List

class AlienSorted:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # # solution 1:
        # # Time: O(m*n) n is length of words, m is max length of one element in words O(n**2)
        # # Space: O(1)
        # order_map = {}
        # for i, char in enumerate(order):
        #     order_map[char] = i

        # for i in range(1, len(words)):
        #     first_word = words[i - 1]
        #     second_word = words[i]
        #     min_len = min(len(first_word), len(second_word))
            
        #     # find first unequal char
        #     to_compare_idx = -1
        #     for i in range(min_len):
        #         if second_word[i] != first_word[i]:
        #             to_compare_idx = i
        #             break
            
        #     if to_compare_idx >= 0:
        #         if order_map[first_word[to_compare_idx]] >  order_map[second_word[to_compare_idx]]:
        #             return False
        #     else:
        #         if len(second_word) < len(first_word):
        #             return False
        # return True
        
        # # solution 2:
        # order_map = {}
        # for i, char in enumerate(order):
        #     order_map[char] = i

        # for i in range(len(words) - 1):
        #     for j in range(len(words[i])):
        #         if j >= len(words[i + 1]):
        #             return False
                
        #         if words[i][j] != words[i + 1][j]:
        #             if order_map[words[i][j]] > order_map[words[i + 1][j]]:
        #                 return False
        #             break
        # return True



# 第二遍：
        order_map = {}
        for idx, ch in enumerate(order):
            order_map[ch] = idx
        
        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                # 这个条件到了当前的这个j的时候，也就是说
                # 第一个词的长度比第二个词的长度要长。并且之前的字母都相等。
                # 那么这个时候直接return False
                if j >= len(words[i + 1]):
                    return False
                if words[i][j] != words[i + 1][j]:
                    if order_map[words[i][j]] > order_map[words[i + 1][j]]:
                        return False
                    # 这个条件比较容易漏掉。
                    # 如果当前的两个词的字母不相等，并且符合所给的顺序，那么我们就不用管之后的字母的顺序了
                    break
        return True

    def call_function(self) -> None:
        self.isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz")
