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

8. [173. Binary Search Tree Iterator](https://leetcode.com/problems/binary-search-tree-iterator/)

    原理：
    用stack来模仿recursion call。
    1. 基本原则就是把node.left都append到stack 里面，然后一个一个的pop出来
    2. 每pop一个，就要向右走一步，然后再把剩余的所有left 的node都append 进去。

9. [1382. Balance a Binary Search Tree](https://leetcode.com/problems/balance-a-binary-search-tree/)

    原理：
    就是把一个unbanlance 的tree 先把他用inorder的顺序变成一个list
    然后用recursion 和 二分的概念去重新construct一个新树

    mid = left + (right - left) // 2
    left = recur(nodes[:mid])
    right = recur(modes[mid+1:])
    nodes[mid].left = left
    nodes[mid].right = right

10. [129. Sum Root to Leaf Numbers](https://leetcode.com/problems/sum-root-to-leaf-numbers/)

    原理：
    dfs 美国一层都是cur_sum * 10 + root.val 然后pass到下一层
    最后把所有到leaf的时候的cur_sum 一次一次的加起来。

11. [863. All Nodes Distance K in Binary Tree](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/)

    ***** 这个方法不是非常普遍的适用 ******
    原理：
    这道题不是特别的好想清楚。
    这道题一共分2个case
    case1：从target 下面的substree找到dist ==k的node，也就是if node == target: 这里表述的case。
    case2: case2.a 是target在当前node的分枝中。如果target在左分枝，那么我们就要到**右**分支找到k-left+1 的node，也是距离target是k的node
            case2.b 如果target在右分枝，那么我们就要到**左**分支找到k-right+1 的node，也是距离target是k的node
            case2.c 并且在case2 中还有一种情况就是，node自己本身就是到target 等于k距离的node，那么也要加进去
    需要注意的是这个return 是到parent 的距离。
    遇到target的时候return 1， none的时候return -1。 target在某一个分枝里的时候return left + 1 or right + 1

    **另一个比较简单的思路是把tree 直接转化为一个graph。然后直接用bfs做**

12. [515. Find Largest Value in Each Tree Row](https://leetcode.com/problems/find-largest-value-in-each-tree-row/)

    原理：
    这道题就是用bfs traverse 然后每一行找一个最大值

13. [536. Construct Binary Tree from String](https://leetcode.com/problems/construct-binary-tree-from-string/)

    原理：
    这道题用recursion 做比较好理解。
    第一：pre order create node
    然后分别把左子树的sub-string 和右子树的sub-string pass 进node.left 和node.right recursion call
    recursion的层数就是tree的层数，分差就是tree的分差。
    第二：最关键的是找到左子树和右子树的sub-string ，然后分割substring，分别pass 进recursion call
    1. 第一次遇到'(' 并且当时的open param count == 1 然后left 还没有assign的时候
        这个idx 就是左子树的开始的idx
    2. 同理：1. 第1次遇到'(' 并且当时的open param count == 1 然后left已经assign了
    right没有assign 那就是右子树的开始的idx

14. [270. Closest Binary Search Tree Value](https://leetcode.com/problems/closest-binary-search-tree-value/)

    原理：
    基本的binary tree traverse， 
    大于target root.left
    小于target root.right

15. [958. Check Completeness of a Binary Tree](https://leetcode.com/problems/check-completeness-of-a-binary-tree/)
    
    原理：
    bfs traverse tree
    然后对pre_node和cur_node 进行记录。
    一旦出现 not pre_node and cur_node，那么就是return false

16. [1522. Diameter of N-Ary Tree](https://leetcode.com/problems/diameter-of-n-ary-tree/)
    
    原理：
    这道题就是 leetcode 543的变形。
    原本只需要有left 和right的子树的长度比较，现在变成一个list of 分枝比较

    1. 需要注意的点是每一个node 都会收集list of depths. sort 这个list
        top two item 相加就是当前最大的diameter。用这个和max diameter 作比较
    2. return len(depths) > 2 那么return 最大的depth。 否则return 仅有个depth

17. [865. Smallest Subtree with all the Deepest Nodes](https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/)

    原理:
    在同一个dfs function里面同时track node 和depth。
    左边大就return左边child，右边大就return 右边child
    两遍一样大就return当前的node


conclusion:
938, 236, 270，就是在当前node 做一个分情况的讨论， 根据不同的case traverse 到不同的方向left or right
314, 987, 就是把tree mark 一个row col 的坐标
199， 515，958 bfs 当中每一行有一些不同的操作
173 用stack 来模仿recursion call
1382，536， 是tree recursion call 当中要拆分list 或者string 的形式。每次pass param的时候有个pivot. recur(node.left, s[:pivot]) recur(node.right, s[pivot + 1:])
129 dfs 的最简单的变形
863 tree 转化成一个graph，然后用bfs做
543， 1522 diameter 在每一个node上找出一个max(left+right, cur_max)。 1522 就是一个多个数找最大
865 recursion return了两个值，用来记录当前的node 情况。 