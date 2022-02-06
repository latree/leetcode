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

#         # 第二遍心得
#         # *********** note ***********
#         # 这个生成graph的方式很重要，因为这是给所有出现过的字母都生成了一个set
#         # 比如
#         # ["wrt","wrf","er","ett","rftt"]
#         # w > e
#         # t > f
#         # r > t
#         # e > r
#         # 在生成graph的代码里不会出现graph['f']因为在生成graph遍历的条件没有touch到f这个node
#         # 以及f的邻居。所以在dfs 遍历的过程中遍历到f的话就会报错，因为f不存在于graph中。所以
#         # 生成graph的时候必须要先把所有的字母都建立一个空set
#         graph = {c:set() for w in words for c in w}
        
#         # build graph
#         for i in range(len(words)- 1):
#             w1, w2 = words[i], words[i + 1]
#             min_len = min(len(w1), len(w2))
            
#             if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
#                 return ""
            
#             for j in range(min_len):
#                 if w1[j] != w2[j]:
#                     graph[w1[j]] = graph.get(w1[j],set())
#                     graph[w1[j]].add(w2[j])
                    
#                     # *********** note ***********
#                     # 这里也必须有break因为我们只能对比第一个不相同的字母，之后的没有意义
#                     break
        
#         # *********** note ***********
#         # 这个graph 不能有闭环。如果有闭环就没有字母的顺序的结果了。
#         # 需要这个函数return 一个bool来表示会不会出现闭环。
#         # 这是一个我之前不知道的算法，graph coloring，只有用的graph coloring 才能找出
#         # directional graph 当中的闭环
#         # ch 在visited 里面代表了  代表这我现在正在走的path里，这个node是已经走过的， ch 不在visited 表示没走过这个node
#         # 在visited里面并且状态是True 代表 这个node上面有闭环
#         # 在visited里面并且状态是False 代表这个node 上面没有闭环
#         # 不在visited 里面代表这个node 还从来没有访问过
#         visited = {}
#         res = []
#         def dfs(node: str, path: List[str], graph: dict) -> bool:
#             if node in visited:
#                 return visited[node]
            
#             visited[node] = True
#             for neighbor in graph[node]:
#                 if dfs(neighbor, path, graph):
#                     return True
#             visited[node] = False
#             path.append(node)
                        
#         for k in graph:
#             if dfs(k, res, graph):
#                 return ""
#         res = res[::-1]
        
#         return "".join(res)


# 第三遍
# graph coloring 和闭环的这个traverse还是没有记住。得重点回顾



# # ["wrt","wrf","er","ett","rftt"]
# # w > e
# # t > f
# # r > t
# # e > r