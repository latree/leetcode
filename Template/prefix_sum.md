# Prefix_sum problem summary

## Solution summary per question

1. [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)

    特点：两个prefix_product
    因为题目要求要求出去自己以外的production。那么就必须要有两个prefix_product
    一个是从左往右的prefix_product
    一个是从右往左的prefix_product
    这样在计算除去自己以外的production 就是 left[i - 1] + right[i + 1]

2. [304. Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/)

    特点：matrix的prefix_sum。
    target matrix sum = 右下角row，col 的prefix_sum - 右上角 prefix_sum - 左下角prefix_sum + 左上角prefix_sum
    这个画图会非常清晰。
    target matrix sum 的左上和右下的坐标分别是(row1, col1), (row2, col2)
    那么target matrix sum = prefix[row2][col2] - prefix[row2][col1] - prefix[row1][col2] - prefix[row1][col2]

3. [548. Split Array with Equal Sum](https://leetcode.com/problems/split-array-with-equal-sum/)

    特点：找三个指针，一个prefix_sum
    原理
    固定j的值，然后从左侧iterate i来找到符合prefix_sum[i - 1] == prefix_sum[j - 1] - prefix_sum[i]的情况，prefix_sum并加到set 里
    从右侧iterate k来找到符合 prefix_sum[n - 1] - prefix_sum[k] == prefix_sum[k - 1] - prefix_sum[j] 的情况。
    因为所有值都相等，所以如果prefix_sum 的值在left_set里面那么就找到了valid solution了
