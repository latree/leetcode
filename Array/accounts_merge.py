from typing import List

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # 先创建一个email map account 的graph
        # 然后从每个account 的每一个email 去做dfs 一旦一个email map 两个以上accouts
        # dfs 就是为了找到一个闭环然后mark 成visited
        # 这样在loop到闭环里的account 的时候就可以直接跳过
        visited_accoutns = [False] * len(accounts)
        res = []
        email_accounts_map = {}
        
        # build email account map
        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                email_accounts_map[account[j]] = email_accounts_map.get(account[j], []) + [i]
        
        def dfs(idx, emails):
            if visited_accoutns[idx]:
                return
            
            visited_accoutns[idx] = True
            for j in range(1, len(accounts[idx])):
                email = accounts[idx][j]
                emails.add(email)
                for neighbor in email_accounts_map[email]:
                    dfs(neighbor, emails)

        for i, account in enumerate(accounts):
            if visited_accoutns[i]:
                continue
            
            name, emails = account[0], set()
            dfs(i, emails)
            res.append([name] + sorted(emails))
        return res


    def call_function(self) -> None:
        self.accountsMerge([["John","johnsmith@mail.com","john_newyork@mail.com"],
                            ["John","johnsmith@mail.com","john00@mail.com"],
                            ["Mary","mary@mail.com"],
                            ["John","johnnybravo@mail.com"]]
        )