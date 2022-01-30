# linked list problem summary

## Solution summary per question

1. [528. Random Pick with Weight](https://leetcode.com/problems/random-pick-with-weight/)

    原理
    建立一个权重数组。也就是prefix_sum 数组。
    随机产生一个1 到total的随机数。
    找到这个随机数落到这个权重数组的哪里。这样就能保证这个权重的随机概率了。
    模板
    left <= right
    condition
        left = mid + 1
    condition
        right = mid - 1

2. [162. Find Peak Element](https://leetcode.com/problems/find-peak-element/)

    原理
    这道题就很好的解释了，不止只有单调递增或者递减的数组才能用bianry search。
    二分法的方法使得满足一定的条件我们就可以剔除一半的搜索范围。只要满足这个条件就可以用bianry search
    left <= right
    condition
        left = mid + 1
    condition
        right = mid - 1

3. [1011. Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/)

    原理
    特别需要注意的点：
    left, right  = max(weights), sum(weights)
    因为我们至少要保证当天的weights 可以一天load 完成。
    left <= right
    condition
        left = mid + 1
    condition
        right = mid - 1

    condition 需要自己定义成一个function

4. [1891. Cutting Ribbons](https://leetcode.com/problems/cutting-ribbons/)

    原理
    特别需要注意的点：
    left, right  = 1, max(ribbons)
    因为没有办法cut 出比max(ribbon)，因为不能拼接。
    left <= right
    condition
        left = mid + 1
    condition
        right = mid - 1

    condition 需要自己定义成一个function

5. [1539. Kth Missing Positive Number](https://leetcode.com/problems/kth-missing-positive-number/)

    原理
    这道题的变形是在于 condition上的一个小变化
    找kth missing 是可以根据公式计算出来的。 arr[mid] - mid - 1
    left <= right
    condition
        left = mid + 1
    condition
        right = mid - 1

6. [658. Find K Closest Elements](https://leetcode.com/problems/find-k-closest-elements/)

    原理

    因为这道题是sorted array，所以可以用binary search 来解决
    其实这也是一到binary search 的变形题目。不是用binary search 去找一个element 位置，而是去找一个区间的位置。
    因为这个区间是sorted，又知道区间的长度。那么直接找到左边的element也就能确定区间的位置
    left <= right
    condition
        left = mid + 1
    condition
        right = mid - 1

7. [1428. Leftmost Column with at Least a One](https://leetcode.com/problems/leftmost-column-with-at-least-a-one/)

    原理
    选取col 的left， right 来做binary search。
    每一次选一个mid col。 然后看看哪个row上这个col 是1，如果找到了，那么就right= mid - 1
    left <= right
    condition
        left = mid + 1
    condition
        right = mid - 1

## Conclution

1. 所有的FB bianry search 题目都可以套用一个模板。
    left <= right
    condition
        left = mid + 1
    condition
        right = mid - 1

2. 528 是把原始数组转化成一个prefix_sum 来进行二分
3. 162， 1428 是对二分法的适用范围进行了深刻的理解
4. 1011， 1891， 1539，658 都是对，condition 进行了特殊的变形。需要define 一个function。左右边界的定义也是一个变形
