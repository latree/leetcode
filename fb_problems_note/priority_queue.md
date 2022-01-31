# Priority Queue problem summary

## Solution summary per question

1. [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)

    原理
    priority queue 性质
    记住用法list(heapq.nlargest(k, heap))

2. [973. K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/)

    原理
    唯一的变形是需要用dist 来排序。所以在append 进去priority queue 的时候要append 进去三个元素
    (distance, x, y)

3. [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)

    原理

    变形是需要用count 来排序。所以在append 进去priority queue 的时候要append 进两个元素
    (count, key)

## Conclution

1. 唯一的变形就是在于排序的变量可能需要一个简单的计算。
2. 当然priority queue 可以和别的题目combine 起来。 比如和bfs， dfs， linked list， array 的题目搭配来考