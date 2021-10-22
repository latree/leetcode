from typing import List

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        # # 有两个细节要注意：
        # # 第一个是: ord_diff += (tmp_diff % 26, ) 这样的表达方式可以实现往tuple 里加东西
        # # 第二个是：要注意审题，对于每一个单独的字符向上加几个diff 而不是作为一个string 整体shift
        # res_dict = {}

        # for item in strings:
        #     ord_diff = ()

        #     for i in range(1, len(item)):
        #         tmp_diff = 26 + ord(item[i]) - ord(item[i - 1])
        #         ord_diff += (tmp_diff % 26, )
                
        #     res_dict[ord_diff] = res_dict.get(ord_diff, []) + [item]

        # return [value for value in res_dict.values()]


# 第二遍：
#         这种方法比较容易好理解
#         每个word都有一个base。先用word里第一个ch 找出与‘a’的diff
#         然后用这个diff 计算这个word的base
#         之后只要group base 一起的就好了
        def convert_to_base(word):
            diff = ord(word[0]) - ord('a')
            
            base = ''
            for i in range(len(word)):
                cur_ch_ord = ord(word[i]) - diff
                if cur_ch_ord < ord('a'):
                    # 唯一的特殊情况就是这个得出的unicode 小于‘a’的unicode，那么我们就要加26 
                    # 比如az 和ba， ba 的a 减1 就是负的了
                    cur_ch_ord += 26
                base += chr(cur_ch_ord)    
            return base
        
        base_map = {}
        
        for i in range(len(strings)):
            word = strings[i]
            cur_base = convert_to_base(word)
            if cur_base not in base_map:
                base_map[cur_base] = []
            base_map[cur_base].append(word)
        
        return [v for v in base_map.values()]
    
    def call_function(self):
        self.groupStrings(["abc","bcd","acef","xyz","az","ba","a","z"])