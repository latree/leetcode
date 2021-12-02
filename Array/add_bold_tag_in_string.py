from typing import List
                                                                                                        
class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        # 1. 这道题其实就是先找出所有match的word 的（起始，结束）位置然后保存 到location里面
        # 2. 根据location里面所有matching word 的idx 的（起始，结束）位置看看有没有重合的，有重合的就combine，直到没有重合的位置
        # 3. 没有重合的就直接加上bold tag。
        location = []
        for word in words:
            start = s.find(word)
            
            while start != -1:
                location.append([start, start + len(word)])
                start = s.find(word, start + 1)
        if not location:
            return s
        
        location.sort()
        
        begin, end = location[0][0], location[0][1]
        res = s[0:begin]
        for i in range(1, len(location)):
            if location[i][0] <= end:
                end = max(location[i][1], end)
            else:
                res += "<b>" + s[begin:end] + "</b>"
                res += s[end:location[i][0]]
                begin = location[i][0]
                end = location[i][1]
        
        res += "<b>" + s[begin:end] + "</b>" + s[end:]
        return res