from typing import List

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        # 有两个细节要注意：
        # 第一个是: ord_diff += (tmp_diff % 26, ) 这样的表达方式可以实现往tuple 里加东西
        # 第二个是：要注意审题，对于每一个单独的字符向上加几个diff 而不是作为一个string 整体shift
        res_dict = {}

        for item in strings:
            ord_diff = ()

            for i in range(1, len(item)):
                tmp_diff = 26 + ord(item[i]) - ord(item[i - 1])
                ord_diff += (tmp_diff % 26, )
                
            res_dict[ord_diff] = res_dict.get(ord_diff, []) + [item]

        return [value for value in res_dict.values()]

    
    def call_function(self):
        self.groupStrings(["abc","bcd","acef","xyz","az","ba","a","z"])