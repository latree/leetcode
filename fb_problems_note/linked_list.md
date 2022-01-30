# linked list problem summary

## Solution summary per question

1. [426. Convert Binary Search Tree to Sorted Doubly Linked List](https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/)

    原理
    这是比较费解的linked list 题目
    inorder traverse 就是按照1，2，3，4 的顺序遍历整个tree
    用两个global 变量保存当前的first， last 在目前的这个doublely linked list 里面就可以
    1. 当遍历到第一个node。设置first， last node 为当前这个第一个node
    2. 之后每次把当前的node append 到last 之后，然后连接pointer
    3. 出了recursion 之后，再把收尾连接就可以了。

2. [138. Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/)

    原理
    需要有一个visited map 来记录已经create 过的node。 
    create 一个新的function get_cloned_node去check 是不是这个node 已经在created map里面了，如果有，直接return， 如果没有再create一个新的然后放入created map里
    1. 每一次在遍历的心的node 时候要call 这个get_cloned function 三遍
        1.1 第一遍看看当前这个node clone 了没有
        1.2 node.next clone了没有
        1.2 node.random clone 了没有
    2. 最后吧next 和 random的node连接
    3. 进入下一个node

3. [146. LRU Cache](https://leetcode.com/problems/lru-cache/)

    原理
    LRU cache 是一道经典的题目。
    需要一个doublely linked list 和一个hashmap 来记录{key: Node(val)}

    在python 里面可以用ordered dict 来实现会更简单明了一些
    1. init 里面有capacity 和 OrderedDict
    2. get key not in OderdedDict return -1
        2.1 OderdedDict.move_to_end(key)
        2.2 return OderdedDict[key]
    3. OrderedDict[key] = value
        3.1 move_to_end(key)
        3.2 if size > capacity OrderedDict.popitem(last=False)

4. [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)

    原理
    只需要一个priority queue. 
    1. 最开始的时候把每一个list 的第一个node放进queue
    2. while queue
        2.1 每一次pop出最小的append 到res list 里面
        2.2 把pop 出来的node.next append回queue 里面

    知道queue is empty

5. [708. Insert into a Sorted Circular Linked List](https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/)

    原理
    用两个pre， cur pointer 遍历
    三个case
    1. head 为空， 那么直接create 一个新node 然后首尾连接
    2. 进入while pre.next != head 循环
        2.1 case 1 <- Node(2) <- 3 （if prev.val <= node.val <= curr.val:）
        2.2 Case2: 3 -> 1, 3 -> Node(4) -> 1, 3 -> Node(0) -> 1
            if prev.val > curr.val and (node.val > prev.val or node.val < curr.val)
    3. 最后把node insert 进去

6. [114. Flatten Binary Tree to Linked List](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/)
    原理
    想象一下，在当前的node， return 回来的是left_tail 和right_tail
    我把这道题想复杂了，这就是单纯的flatten tree
    没有左子树大小的问题。
    只需要把左子树的最后一个node 连到右子树的第一个node，然后
    把整个左子树再移到右边
    因为在preorder 的位置，如果是leaf node 直接return，那么left_tail 和right_tail 肯定是leaf node

    1. 如果有left_tail
        2.1 left_tail.right = node.right
        2.2 node.right = node.left
        2.3 node.left = None
    2. 如果没有left_tail return right_tail if right_tail else left tail

## Conlution

1. linked 基本题目都很简单。难的还是linked list 和tree 的结合题目
2. 114， 426 就是tree 和linked list 结合题目。要把tree 转换成linked list
3. 23 priority queue 的应用
4. 708 linked list insert node 变形。insert 进入circular linked list
5. 138 有点像graph 的clone graph。 需要有map 才可以
6. LRU cache 是orderedDict，或者是doublely linked list和hashmap的组合。
