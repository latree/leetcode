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
        
        # solution 2:
        order_map = {}
        for i, char in enumerate(order):
            order_map[char] = i

        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                if j >= len(words[i + 1]):
                    return False
                
                if words[i][j] != words[i + 1][j]:
                    if order_map[words[i][j]] > order_map[words[i + 1][j]]:
                        return False
                    break
        return True

    def call_function(self) -> None:
        self.isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz")



# Example 1:

# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
# Example 2:

# Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false
# Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
# Example 3:

# Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
# Output: false
# Explanation: The first three characters "app" match, and the second string is shorter (in size.) 
# According to lexicographical rules "apple" > "app", because 'l' > '∅', 
# where '∅' is defined as the blank character which is less than any other character (More info).