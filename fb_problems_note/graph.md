# Graph problem summary

## Solution summary per question

1. [133. Clone Graph](https://leetcode.com/problems/clone-graph/)
    复制一个graph
    有两点要特别注意：
    1. 闭环。闭环可以用一个visited set 就可以解决
    2. 避免重复create node 需要用到created_map，
        比如 [[2,4],[1,3],[2,4],[1,3]]
        这里面在 iterate到 node.val = 2 和node.val = 4 的时候都会碰到他们的邻居
        node.val = 3。但是这个node_3 还没有被访问，所以就会造成visited不会cover这个case
        那么我们就需要用另个一created_map来记录我们之前所有已经created 过的node。这样
        才会避免重复create的情况

2. [269. Alien Dictionary](https://leetcode.com/problems/alien-dictionary/)
    根据现有的array of strings 制作一个graph。(可以用{node:set()} 来表示一个graph)
    从每一个graph node 出发 找出一个最长的path，return。 就要用到dfs
    append 所有最长的path 就是结果

3. [2076. Process Restricted Friend Requests](https://leetcode.com/problems/process-restricted-friend-requests/)

    还没有做过，稍后总结

## Conlution

### 图的定义

图（Graph）是一种复杂的非线性表结构。

顶点（vertex）：图中的元素；
边（edge）：图中的顶点与其他任意顶点建立连接的关系；
顶点的度（degree)：跟顶点相连接的边的条数。
入度（In-degree）和出度（Out-degree）：对于有向图，一个顶点的入度是指以其为终点的边数；出度指以该顶点为起点的边数；
图有多种类型，包括有向图、无向图、简单图、多重图、有向图、无向图等

### 图的分类

无向图，有向图，带权图，多重图

#### 有向图和无向图

图的每条边规定一个方向，那么得到的图称为有向图；相反，边没有方向的图称为无向图。

#### 简单图

任意两顶点之间只有一条边（在有向图中为两顶点之间每个方向只有一条边）；
每条边所关联的是两个不同的顶点
带权图（weighted graph）
在带权图中，每条边都有一个权重（weight）[非负实数]。

#### 多重图

图中某两个顶点之间的边数多于一条，又允许顶点通过同一条边和自己关联，则称为多重图