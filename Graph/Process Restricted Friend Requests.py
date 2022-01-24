class DSU:
    def __init__(self, n):
        self.parents = list(range(n))
        # 为了在找union的时候节省时间
        # 这个size 是用来记录每一个parents 有多少个node 是这个parent 的union 下面的
        self.size = [1] * n

    
    def find(self, node):
        while node != self.parents[node]:
            node = self.parents[node]
        return node
    
    def union(self, x, y):
        p, q = self.find(x), self.find(y)

        if p == q:
            return
        
        # 为了在找union的时候节省时间
        # 如果p 的手下比q的手下少，那么p 应该join q， parent 就变成q，而且要q的手下数量要加上p的手下数量
        # 反之亦然
        # 这样做的好处就是在于在查找两个node 是不是一个union 的时候会省去一些时间，因为是小团体加入大团体
        # 两个node 出现在大团体的概率要比出现在小团体的概率高，如果是大团体加入小团体，让小团体的node 成为parent，那么在两个node 都是在大团体手下的时候，需要有extra的步骤 去find parent。
        if self.size[p] < self.size[q]:
            self.parents[p] = q
            self.size[q] += self.size[p]
        else:
            self.parents[q] = p
            self.size[p] += self.size[q]
        
        
class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        dsu = DSU(n)
        res = []
        
        for req_a, req_b in requests:
            req_a_prnt, req_b_prnt = dsu.find(req_a), dsu.find(req_b)
            
            can_be_friend = True
            
            for rstct_a, rstct_b in restrictions:
                rstct_a_prnt, rstct_b_prnt = dsu.find(rstct_a), dsu.find(rstct_b)
                if set([rstct_a_prnt, rstct_b_prnt]) == set([req_a_prnt, req_b_prnt]):
                    can_be_friend = False
                    break
            
            res.append(can_be_friend)
            if can_be_friend:
                dsu.union(req_a, req_b)
        
        return res