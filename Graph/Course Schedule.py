from lib2to3.pytree import Node


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build graph
        # 非常典型的toppological sort。 graph 找闭环
        # 用visited[i] == 1 表示已经走过或者走完的Node
        # 用visited[i] == -1 表示正在走的path，node正在当前的path里面
        # 用visited[i] == 0 表示没有走过的node
        graph = {i: []  for i in range(numCourses)}
        visited = {i: 0  for i in range(numCourses)}
        
        for prereq in prerequisites:
            next_course, pre_course = prereq[0], prereq[1]
            graph[next_course].append(pre_course)
        
        
        def dfs(graph, cur_course, visited):
            if visited[cur_course] == -1:
                return False
            
            if visited[cur_course] == 1:
                return True
        
            visited[cur_course] = -1
            
            for next_course in graph[cur_course]:
                if not dfs(graph, next_course, visited):
                    return False
            
            visited[cur_course] = 1
            return True
        

        for node in graph.keys():
            if not dfs(graph, node, visited):
                return False
        
        return True