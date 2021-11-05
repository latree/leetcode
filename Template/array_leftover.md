# Array leftover problem summary

## Solution summary per question

1. [65. Valid Number](https://leetcode.com/problems/valid-number/)
    这道题就是要费情况讨论：
    分五大类: 是不是数字，是不是e，是不是dot，是不是加减号，其它
    1. 有dot时候 之前有了dot 或者之前有了e那么就不是valid
    2. 看到e 有点复杂。
      a. 看到e必须保证之前没有e 否则错的
      b. 看到e的时候，e前面必须要存在数字 否则错的
      c.看到e的时候，e之前的数字都可以忽略，可以重新按照是不是valid数字来检测

    3. 符号+ - 之前不能有e
    4. 数字就是数字，set flag

2. [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/)
    原理：
    把原有的array 根据左边界sort 一遍
    然后遍历，如果res最后一个的右边界小于当前的左边界直接append
    else 就要把两个merge。也就是直接更新res[-1]右边界就可以了

3. [766. Toeplitz Matrix](https://leetcode.com/problems/toeplitz-matrix/)
    原理：
    **如果r1, c1 和r1, c2在同一个左上到右下的对角线上，那么：r1 - c1 = r2 - c2**

4. [498. Diagonal Traverse](https://leetcode.com/problems/diagonal-traverse/)
    原理：
    **如果r1, c1 和r1, c2在同一个右上到左下的对角线上，那么：r1 + c1 = r2 + c2**
    另外这道题额外有个操作就是需要zigzag，那么每隔一行做一个reverse就可以了

5. [605. Can Place Flowers](https://leetcode.com/problems/can-place-flowers/)
    原理：
    分类讨论：
    在一个[0,0,0]里面当前的遍历元素是中间idx的元素
    在中间的数为0的时候
    分为以下几种类别
    [0, 0, 0]
    [0, 0, 1]
    [1, 0, 0]
    [1, 0, 1]
    中间的数不为0 就直接跳两个idx

6. [158. Read N Characters Given read4 II - Call Multiple Times](https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/)

    这道题其实不难，就是题意有点不容易懂，和function给的定义有点模糊
    原理：
    原理就是每次从read4里面读完以后把所有值都append 到buffer 里面
    然后每一次只复制给buf的次数是len(self.buffer), n - idx。两个的最小值
    这样就能巧妙的保证里每一次先用掉buffer里面的所有值，然后不够再进入下一个循环，够了
    就直接退出循环

7. [346. Moving Average from Data Stream](https://leetcode.com/problems/moving-average-from-data-stream/)
    原理：
    就用一个deque每次check以下过没过标准的size

8. [163. Missing Ranges](https://leetcode.com/problems/missing-ranges/)

    原理：
    1. 首先遍历nums 然后只要是nums[i] 和nums[i + 1]之差大于1 的那么就会产生一个区间，把这个区间append 到res
    2. 之后，如果nums是空，那么[lower, upper]就是missing 区间
    3. 如果lower 到nums[0] 有missing那么就append到最前面
    4. 如果nums[-1]到upper 有missing 那么就append到最后面

9. [393. UTF-8 Validation](https://leetcode.com/problems/utf-8-validation/)
    又是一道分类讨论的题目。
    原理：
    1. 用mask 1000000, 01000000 来做与还看看第一位和第二位是1 还是0 
    2. 先来count n_bytes有几个，然后每过一个num 那么就n_bytes - 1。 最后看看count的n_bytes 和num的数量符不符合。不符合就是false
    3. n_bytes > 4 肯定是错误的，n_bytes==1 说明左边第一位是1 那么也是false
    4. 剩余的bytes 的前两位不是10 那就是false。

## Conlution

1. **leetcode 65, 605, 393 是一类题，用到了分类的和设定flag的情况。这一类题是我比较薄弱的地方**
2. leetcode 766,498是一个类题，都是考到了matrix的对角线性质
3. leetcode 56, 163虽然都是找区间，但是写法上没有太多相似的地方
4. leetcode 158, 346都是有点sliding window的变种，比较简单，就不做过多阐述了。
