from audioop import reverse


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 在207 course schedule 的基础上加一个path。用postorder的方式return 这个path 就是
        # topological sort return 的res

        # 根据graph的定义不同那么return 的path 是正序还是倒序是不同的
        # 如果graph[to].append(from), 那么path 就不用reverse
        # 如果graph[from].append(to)， 那么path 就需要reverse
        graph = {i: []  for i in range(numCourses)}
        visited = {i: 0  for i in range(numCourses)}
        
        for prereq in prerequisites:
            next_course, pre_course = prereq[0], prereq[1]
            graph[next_course].append(pre_course)
        
        
        def dfs(graph, cur_course, visited, path):
            if visited[cur_course] == -1:
                return False
            
            if visited[cur_course] == 1:
                return True
        
            visited[cur_course] = -1
            
            for next_course in graph[cur_course]:
                if not dfs(graph, next_course, visited, path):
                    return False
            
            path.append(cur_course)    
            visited[cur_course] = 1
            return True
        
        
        path = []
        for node in graph.keys():
            if not dfs(graph, node, visited, path):
                return []
        
        return path