import collections

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count_map = collections.Counter(s)
        res = []

        for ch in order:
            res.append(ch * count_map[ch])        
            del count_map[ch]
        
        for ch in count_map:
            res.append(ch * count_map[ch])
        
        return "".join(res)