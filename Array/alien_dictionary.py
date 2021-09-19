from typing import List

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = {c:set() for w in words for c in w}
        
        # build the graph
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
        
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
                    
        # Use dfs to get result            
                            
        # ***** this is important definition, without this definition beblow case cannot get 
        # correct result
        # False means visited, True means visited and in path
        visited = {}
        res = []
        
        # we have to use postorder dfs because for example:
        #     a -> b -> c
        #     a -> c
        # only postorder will give us the "cba" result. we only need to reverse it
        # the preorder dfs will give us the acb result which is a not valid result
        def dfs(c):
            if c in visited:
                return visited[c]
            
            visited[c] = True
            for nei in adj[c]:
                if dfs(nei):
                    return True
            visited[c] = False
            res.append(c)
        
        
        for c in adj:
            if dfs(c):
                return ""
        res.reverse()
        return "".join(res)
            