# Hashtable problem summary

## Solution summary per question

1. [953. Verifying an Alien Dictionary](https://leetcode.com/problems/verifying-an-alien-dictionary/)

    创建一个dictionary 的order_map。这个order_map是存储的{ch:idx}。
    原理：
    用双指针遍历list里的两个词的每一个字母如果前一个词的当前字母和后一个词的当前字母不等，那么必须前一个词的字母要大于后一个词的当前字母的idx

2. [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)

    这里用到了一个prefix_sum的概念。在不少题目当中累加的array 都是很有用的，尤其是在sum的题型里面。
    这道题是形成一个sum_map也就是{prefix_sum:counter} 这个prefix_sum就是到当前idx的sum。counter是这个prefix_sum 在这个array里出现的次数。
    原理：
    遍历array，如果prefix_sum - k 在这个sum_map里，那么就意味着曾经出现的prefix_sum 到当前的prefix_sum 这段区间的subarray 的和是k。那么就是
    我们要找的subarray。counter能够帮助我们记录我们能找到几个这样的array

3. [249. Group Shifted Strings](https://leetcode.com/problems/group-shifted-strings/)

    原理：如果一个string a通过shift能够变成另外一个string b说明a 和b 的有一个共同的base string。
    只要我们通过固定的公式把每一个词的base string 存储进一个hashtable里面

    ```python
    base_map = {base:[string]}
    ```

    那么在遍历每一个词的时候，先把这个词转化成base string， 看看base_map中有没有这个base string，有就group，没有就建立一个新的entry

4. [523. Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/)

    原理:需要有一个prefix_sum。用一个mod_map

    ```python
    mod_map = {mod_val:idx}
    ```

    这个mod_map就是用来存储当前idx的prefix_sum做了mod以后的余数是不是在mod_map里曾经出现过。如果出现过就说明曾经出现的prefix_sum 到当前的prefix_sum 这段区间的subarray 的和是 k的倍数

5. [398. Random Pick Index](https://leetcode.com/problems/random-pick-index/)

    原理：建立一个idx_map

    ```python
    idx_map = {ch:[idx]}
    ```

    这个idx_map 用来存储每一个字母已经出现的idx的一个list
    通过这个list我们就能平等的随机得到这个字母的其中一个idx

6. [791. Custom Sort String](https://leetcode.com/problems/custom-sort-string/)

    原理：建立一个count_map。

    ```python
    # ch is in stirng s 
    count_map = {ch:count}
    ```

    count_map就是对string s的每一个字母的计数。先把order string里面的字母遍历一遍，加进res。同时删除已经加入res的ch
    最后再遍历一遍count_map里剩余的ch加进res。

7. [380. Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/)

    建立一个list和一个idx_map

    ```python
    # ch is in stirng s 
    array = [val1, val2]
    idx_map = {va1:idx1, val2:idx2}
    ```

    有了这两个var 就可以进行insert 和deletion都是O(1)的操作了。
    delete：每一次把需要delete元素swap到array 最末端然后pop，在delete val在idx_map的entry， 最后update swap之后的idx_map val的idx
    insert：append 的array末尾，然后加入一个新的entry 在idx_map里面。如果已经有个val在idx_map里面，直接return False

8. [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)

    建立一个target的count_dict。建立一个空的用来表示当前的这个substring的count_dict情况.count_dict就是每一个字母出现的次数
    再建立一个char_formed 和required。char_formed来记录当前的substring 有没有包含所有要的target的ch的个数。required是应该有的所有target里ch的个数。

    通过双指针来记录和检查是不是找到符合的substring
    在当前的substring里面没有足够的所有在target里的ch的个数的时候挪动右边的指针
    如果在当前的substring里满足target，那么开始挪动做指针，直到char_formed < required 停止。然后update 最小res的值

9. [266. Palindrome Permutation](https://leetcode.com/problems/palindrome-permutation/)

    建立一个char_map

    ```python
    # ch is in stirng s
    count_map = {ch:count}
    ```

    ch是stirng s里的字母，count就是出现的次数。如果这个string是palindrome，那么count_map里能够出现单数的ch的count的个数必须小于等于1

10. [348. Design Tic-Tac-Toe](https://leetcode.com/problems/design-tic-tac-toe/)

    原理
    直观的方法就是用一个matrix 记录所有的步骤，然后去每一个row，col diag and anti-diag 去check
    但是最简单的方式是把row，col diag and anti-diag 去check 用一个数值来计算。
    player a 下了一步棋就是 + 1
    player b 下了一步棋就是 - 1
    最后只需要看row，col diag and anti-diag 这四个值有没有任何一个到达 n 或者-n

11. [616. Add Bold Tag in String](https://leetcode.com/problems/add-bold-tag-in-string/)

    原理
    1. 这道题其实就是先找出所有match的word 的（起始，结束）位置然后保存 到location里面
        需要注意的是这里找word 是允许重叠的。所以在用while loop 重复找 start = s.find(word, start + 1)
    2. 根据location里面所有matching word 的idx 的（起始，结束）位置看看有没有重合的，有重合的就combine，直到没有重合的位置
    3. 没有重合的就直接加上bold tag。

12. [939. Minimum Area Rectangle](https://leetcode.com/problems/minimum-area-rectangle/)

## Conlution

560， 523 用到了prefix_sum，并且用prefix_sum 进行的转化来形成一个hash map去解决问题。
953, 398, 380 都是用ch:idx 的hash table 来解决问题。
791, 76, 266 都是用ch:count的hash table 来解决问题。
249 是用base:[string1, string2]
348 是直接用一个数值来判断
616 是区间找交集。
