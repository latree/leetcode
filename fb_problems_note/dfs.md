# General DFS problem summary

## Solution summary per question

1. [339. Nested List Weight Sum](https://leetcode.com/problems/nested-list-weight-sum/)

    原理
    这是最基础的dfs原来，
    1. 只要遇到list，就要recursion call 然后depth + 1
    2. 如果遇到integer 就直接计算val * depth 加到最后的cur_sum里

2. [827. Making A Large Island](https://leetcode.com/problems/making-a-large-island/)

    原理
    1. 用dfs 去把matrix 里面所有的island都遍历一遍，遍历的时候需要做以下事情
        1.1 给每一个island mark 一个idx 这个idx 就是为了有island_id
        1.2 count 这个island 的面积。
        1.3 记录一个map {idx(island_id): total_size}
    2. 遍历所有 grid[row][col] == 0的点。也就是不是islande 点
        2.1 向四个方向寻找这个点是不是任何island 相邻。如果相邻就要把当前点的面积(1) + area[idx](相邻island的total 面积)
        2.2 update 当前最大的面积。

3. [721. Accounts Merge](https://leetcode.com/problems/accounts-merge/)

    原理
    1. 建立一个email to account idx map. 注意一定是email to account_idx. 如果不是account_idx而是名字，那就分辨不出来重名的情况。 email_to_acct_idx = {email:[idx]}
    2. 对于每一个account(每一个row in accounts) 做dfs 来收集emails
        2.1 如果visited 直接return
        2.2 set visited[idx] = Ture
        2.3 遍历当前account 里的每一个email，用这个email来找出所有有这个email 的account_idx 为邻居，继续做dfs

## Conclution

1. 比较直接的dfs 的操作。nested list and integer
2. 在matrix 里面做dfs 和bfs 是一种比较常见的题型。需要有一些比较固定的形势moves, seen 边界判断
3. 最后其实是一个graph 题目。把graph 转化成了一个list。
