# Math problem summary

## Solution summary per question

1. [415. Add Strings](https://leetcode.com/problems/add-strings/)

    这道题的原理就是基本的加法运算的方式
    刚开始开顾虑num1 如果加完了怎么办?
    应该是 while p1 >= 0 or p2 >= 0:   还是 while p1 >= 0 and p2 >= 0:?
    如果在那一位上没有数字，那么直接用0 补充就可以了。所以应该用or

2. [670. Maximum Swap](https://leetcode.com/problems/maximum-swap/)

    这里方法非常巧妙。
    1. 从后往前的遍历很巧妙。 从后往前的遍历解决了找最大值，并且记录swap 的idx的问题
    2. 从后往前的遍历还保证了每一次需要swap的idx 都是最左侧（最高位的位置）需要swap的数字的高位。

    原理：
    1. 只要发现一个新的最大值，就去update 最大值和最大值的idx
    2. 只要发现当前的值小于最大值，那么就是potential 需要swap的对象，那么就要记录当前的最大值的idx 和当前值的idx 作为potential swap的idx对象

3. [67. Add Binary](https://leetcode.com/problems/add-binary/)

    和leetcode 415题可以用同一种模板解题

    ```python
        p1, p2 = len(a) - 1, len(b) - 1
        
        res = []
        carry = 0
        while p1 >= 0 or p2 >= 0:
            d1 = ord(a[p1]) - ord('0') if p1 >= 0 else 0
            d2 = ord(b[p2]) - ord('0') if p2 >= 0 else 0
            
            value = (d1 + d2 + carry) % 2
            carry = (d1 + d2 + carry) // 2
            res.append(str(value))
            p1 -= 1
            p2 -= 1
        if carry:
            res.append(str(carry))
        
        res = res[::-1]
        return "".join(res)
    ```

4. [29. Divide Two Integers](https://leetcode.com/problems/divide-two-integers/)

    这道题用到指数递增的方法，每次乘以2 来寻找到最大的除数的结果
    iterate 去除以除数的方法比较慢
    原理：
    1. 如果当前除数乘以2 小于被除数，那么当前除数就要乘以2 再去循环尝试是不是大于被除数。这样可以成指数倍增加寻找到除以除数后最大的结果
    2. 一个小的trick是每一次乘以2其实可以用bit operation来代替就是 a << 1

5. [1344. Angle Between Hands of a Clock](https://leetcode.com/problems/angle-between-hands-of-a-clock/)

    这个就是公式
    小时的度数就是，小时的整度数 + 在那一个小时里面分钟的度数

    ```python
    hour_degree = hour_degree_unit * hour + minutes / mins_in_hour * hour_degree_unit
    ```

    分钟的度数比较直接，就是当前分钟减去一个小时的分钟数再乘以360度

    ```python
    minutes_degree = minutes / mins_in_hour * total_degree
    ```

6. [50. Pow(x, n)](https://leetcode.com/problems/powx-n/)

    和leetcode 29 一样用到了指数递增的方法
    2^10 = 2^5 + 2^5

7. [273. Integer to English Words](https://leetcode.com/problems/integer-to-english-words/)

    这道题主要是一个归类的问题
    原理：
    1. 十以内的数有一个名字
    2. 小于20 大于等于十都有独特的名字
    3. 大于等于20 的所有几十有独特的名字
    4. 处理两位数的时候有四个case
    5. 处理三位数的时候需要用到两位数，而且有四个case
    6. 三位数以上都是可重复复的。

8. [282. Expression Add Operators](https://leetcode.com/problems/expression-add-operators/)

    这道题是比较直接的dfs。
    画出recursion tree 就能看出：
    1. 每一个node 是当前cur_res的值（状态）
    2. 每一个node 会有四个分差，就是下一个cur_res要加入的char 是数字，+, -, * 这四个情况
    3. 砍掉的分枝就是cur_res最后一位是0 的情况，0 不能是leading 0

9. [319. Bulb Switcher](https://leetcode.com/problems/bulb-switcher/)

    举例出前9个round 是什么情况就不难发现2个灯是round 4， 3个灯是round 9
    即使平方根

## Conlution

1. leetcode 29， 50 是次幂递增递减的方式来大幅缩减循环的次数
2. **leetcode 67，415 都是加减乘除的运算模板，这个模板很重要**
