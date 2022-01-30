# two pointer problem summary

## Solution summary per question

1. [680. Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/)

    原理
    两头开始移动左右的pointer
    1. 相等就左右pointer 都向中间移动一位
    2. 不相等要么就是skip左边一位，剩下的再判断palindrom，要不然就是skip 右边一位，剩下的要判断是不是palindrom

2. [1570. Dot Product of Two Sparse Vectors](https://leetcode.com/problems/dot-product-of-two-sparse-vectors/)

    原理
    两个pointer 做乘法。然后把所有结果累加起来

3. [408. Valid Word Abbreviation](https://leetcode.com/problems/valid-word-abbreviation/)

    原理
    两个pointer 同时移动。
    1. 相等同时移动到下一位
    2. 如果abbr pointer是数字，那就要先把当前的数字的全部读取出来，然后word pointer移动相应的位数

4. [31. Next Permutation](https://leetcode.com/problems/next-permutation/)

    原理
    1. i， j pointer 从右边开始向左边遍历，找到第一个递减的 i，j
    2. 如果没找到，那么说明当前这个数从左往右一直单调递减，也就是当前最大的permutation，那么return reverse 就可以
    3. **容易错的地方！！** 如果找到了一个递减i，j，那么从j开始再向右遍历，去找到刚好大于nums[i]的nums[j]
        nums[j] > nums[i], nums[i] >= nums[j + 1]
    4. swap i, j
    5. 把 nums[i+1:] reverse 一遍。
    举例 [1, 3, 2]
    先找到 1, 3位置，对应i，j
    然后j 向右找到2
    swap 1，3 也就是 i，j
    reverse 3，1 
    最后变成[2，1，3]

5. [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)

    原理
    就是简单的从左右两边开始向中间遍历
    有两种case 需要 cover:
    1. 非字母（数字，空格，标点）要skip 掉
    2. 大小写要视为相等

6. [88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)

    原理
    这道题需要注意的点是把两个list merge 到第一个list 里面
    in place 去merge，而不是建立一个新的list
    连个pointer是从nums 最右边开始，然后比较大的就放到nums1 的最末尾

7. [986. Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/)

    原理
    也是两个pointer
    需要判断两个区间是不是有交集，有交集就要计算出交集，放到结果里。
    然后move那个落后的区间的pointer

8. [658. Find K Closest Elements](https://leetcode.com/problems/find-k-closest-elements/)

    原理
    因为这道题是sorted array，所以可以用binary search 来解决
    其实这也是一到binary search 的变形题目。不是用binary search 去找一个element 位置，而是去找一个区间的位置。
    因为这个区间是sorted，又知道区间的长度。那么直接找到左边的element也就能确定区间的位置
    只要找到了左边界，然后直接return arr[left:left + k]

9. [1868. Product of Two Run-Length Encoded Arrays](https://leetcode.com/problems/product-of-two-run-length-encoded-arrays/)

    原理
    还是两个pointer 移动。
    移动pointer 的条件就是当前的freq == 0 的时候就可以移动这个pointer了。

10. [253. Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/)

    原理
    这道题用priority queue 做比用two pointer跟间接明了
    1. sort interval
    2. 遍历interval，
        2.1 如果 当前meeting需要的开始的时间，和heap 上的最早结束的时间没有重叠，那么就可以用同一个meeting room。
        cur_interval[0] >= heap[0]
        2.2 如果重叠，那么必须要一个新的meeting room push 到heap里面
    3. return len(heap)

11. [556. Next Greater Element III](https://leetcode.com/problems/next-greater-element-iii/)

    原理
    这道题就是 31. Next Permutation 的变形。把list of integers 的input 改成一个数字的input

12. [16. 3Sum Closest](https://leetcode.com/problems/3sum-closest/)

    原理
    变形题。用三个pointer。
    1. 最外层的循环为pointer i 从头到尾的遍历
    2. 固定i 了以后再定义两个pointer  l， h。 h是end of list，l + 1
    3. 进入nested 循环。while l<h 来寻找 target
    4. 最后return target - diff. 因为要找最接近的。不一定一定有target 存在在list里

13. [825. Friends Of Appropriate Ages](https://leetcode.com/problems/friends-of-appropriate-ages/)

    原理
    主要的是这个公式

    ```python
    request(a, b) * c[a] * (c[b] - (a == b))
    ```

    巧妙的运用到了 True is 1 and False is 0 in python

## Conlution

1. 680, 125 都是左右开始的两个pointer 然后向中间移动
2. 1570， 408， 88，都是pointer从同一边开始移动。88题是变形，从后面向前移动。 作比较以后进行处理
    2.1 131， 556 也是pointer 从一遍开始，要进行好几步的不同方式的移动
    2.2 986， 1868 是两个区间比较或者两个lists 进行计算。最后操作完成根据特殊条件决定move pointer
    2.3 825 也是两个ptrs 从同一边move 来决定

3. 658 是用binary search 做的。而且move pointer的条件比较特殊
4. 253 是用priority queue 做的，其实跟求交集是大同小异
5. 16 是move 3 个pointer。 重点是固定一个pointer 然后根据条件move 剩下的两个pointer
