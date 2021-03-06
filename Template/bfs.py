# Return the length of the shortest path between root and target node.
# ***** BFS is the best method to solve minimum steps to reach in graph questions




from typing import Deque

# template one: general template for traversal
def BFS(root: Node, target: Node) -> int:
    # store all nodes which are waiting to be processed
    queue = Deque() 
    # number of steps neeeded from root to current node
    step = 0
    # initialize
    queue.append(root)
    # BFS
    while queue:
        step += 1
        # iterate the nodes which are already in the queue
        size = len(queue)
        for i in range(size):
            cur = queue.popleft()
            if cur is target:
                return step
            for neighbor in cur.neighbors:
                queue.append(neighbor)
        
    # there is no path from root to target
    return -1


# template two: have the visted to avoid cycle graph if infinite loop
# Return the length of the shortest path between root and target node.
def BFS(root: Node, target: Node) -> int:
    # store all nodes which are waiting to be processed
    queue = Deque() 
    # number of steps neeeded from root to current node
    step = 0

    # store all the nodes that we've visited
    visited = set()
    # initialize
    queue.append(root)
    # add root to visited
    visited.add(root)

    # BFS
    while queue:
        step += 1
        size = len(queue)
        for i in range(size):
            cur = queue.popleft()
            if cur is target:
                return step
            for neighbor in cur.neighbors:
                if cur not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
                            
    # there is no path from root to target
    return -1



# // 计算从起点 start 到终点 target 的最近距离
# int BFS(Node start, Node target) {
#     Queue<Node> q; // 核心数据结构
#     Set<Node> visited; // 避免走回头路
    
#     q.offer(start); // 将起点加入队列
#     visited.add(start);
#     int step = 0; // 记录扩散的步数

#     while (q not empty) {
#         int sz = q.size();
#         /* 将当前队列中的所有节点向四周扩散 */
#         for (int i = 0; i < sz; i++) {
#             Node cur = q.poll();
#             /* 划重点：这里判断是否到达终点 */
#             if (cur is target)
#                 return step;
#             /* 将 cur 的相邻节点加入队列 */
#             for (Node x : cur.adj())
#                 if (x not in visited) {
#                     q.offer(x);
#                     visited.add(x);
#                 }
#         }
#         /* 划重点：更新步数在这里 */
#         step++;
#     }
# }