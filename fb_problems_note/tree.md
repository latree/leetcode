# Tree problem summary

## Solution summary per question

1. [938. Range Sum of BST](https://leetcode.com/problems/range-sum-of-bst/)

    原理，
    1. traverse tree，只要数值在[low, high]区间就要全部左右遍历
    2. node.val 小于 low 就要往node.right 遍历
    3. node.val 大于high 就要往node.left 遍历

2. [314. Binary Tree Vertical Order Traversal](https://leetcode.com/problems/binary-tree-vertical-order-traversal/)

    这道题跟314 非常相似。唯一的区别就是在同一个row col 的nodes 314是从左往右排列
    987是按大小排列
    原理：
    1. traverse 整个数，contruct 一个idx_map的dict {(row, col):[int]}. 因为在同一个坐标上可能会出现multiple的数值
    2. 最后根据这个idx_map来contruct 最后的list of list

    大体原理不难，但是会在sort construct 最后的结果的时候稍微有些麻烦。
    1. 结果要按照col 来sort
    2. 如果同样的col，那么要按照row 来sort。 如果同样的row 和col 最后要按照从左往右排列。也就是traverse 先left 后right的顺序。

3. [1650. Lowest Common Ancestor of a Binary Tree III](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/)

    原理：
    p1 -> p2 -> p3 -> c1 -> c2 -> q1 -> c1
    q1 -> c1 -> c2 -> p1 -> p2 -> p3 -> c1
    两个人跑步，如果a，b跑到头互换path， 总会在c1遇到。

4. [236. Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)

    原理：
    这个就是bottom up的时候要分情况讨论，对于每一个小三角的node， left， right 
    可能出现的情况
    就是答案当中的几种情况。这里不一一详细说明，因为代码比较简单，直接看一下答案

5. [987. Vertical Order Traversal of a Binary Tree](https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/)

    这道题跟314 非常相似。唯一的区别就是在同一个row col 的nodes 314是从左往右排列
    987是按大小排列
    原理：
    1. traverse 整个数，contruct 一个idx_map的dict {(row, col):[int]}. 因为在同一个坐标上可能会出现multiple的数值
    2. 最后根据这个idx_map来contruct 最后的list of list

    大体原理不难，但是会在sort construct 最后的结果的时候稍微有些麻烦。
    1. 结果要按照col 来sort
    2. 如果同样的col，那么要按照row 来sort。 如果同样的row 和col 最后要按照从大到小sort
    为了完整这样的sort，我们还要记录下 两个set()，一个是row idx set， 一个是col idx set

6. [199. Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/)

    原理：
    bfs 遍历整个树。然后append每一层最后一个node


7. [543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)

    原理：
    在每一个node上都做一个比较
    当前的最大值 max(res[0], left + right)
    return max(right, left) + 1

8.[173. Binary Search Tree Iterator](https://leetcode.com/problems/binary-search-tree-iterator/)

    原理：
    