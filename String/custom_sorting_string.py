import collections

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # count_map = collections.Counter(s)
        # res = []

        # for ch in order:
        #     res.append(ch * count_map[ch])        
        #     del count_map[ch]
        
        # for ch in count_map:
        #     res.append(ch * count_map[ch])
        
        # return "".join(res)
    
    # 第二遍：
            # ******* important *******
        # collections.Counter() 需要记一下
        count_map = collections.Counter(s)
        res = []
        for ch in order:
            # ch * int 也是一个需要记住的地方
            res.append(ch * count_map[ch])
            # 每一次要del 这样才能知道哪些是不在order里的ch
            del count_map[ch]
        
        for ch in count_map:
            res.append(ch * count_map[ch])
        
        return "".join(res)