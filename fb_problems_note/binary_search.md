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

## Conlution

1. 
