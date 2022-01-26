# Stack problem summary

## Solution summary per question

1. [1249. Minimum Remove to Make Valid Parentheses](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/)

    用两个list来充当stack 去记录括号的配对情况
    原理：
    open 括号的stack来记录open括号的情况：如果有open的时候再出现close我们就要pop
    另一个stack记录close的情况：只有在没有open 括号的时候需要append

2. [1762. Buildings With an Ocean View](https://leetcode.com/problems/buildings-with-an-ocean-view/)

    这道题用到了monotonic stack 概念。也就是单调递增stack。
    因为题目是向右的ocien view。那么我们只需要保持一个从右到左的单调递增stack
    只要当前的idx height 比top of stack 高那么append到res里，并且同时append 到 stack 里

3. [921. Minimum Add to Make Parentheses Valid](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/)

    这道题本身没有用到stack。但是用了了stack的概念
    相对于第一题（leetcode1249）这道题就用了两个var来表示open括号的stack和close括号的stack。
    原理也是和第一个一样：
    遇到open括号的时候open 加一
    遇到close括号的时候close 要先判断有没有open，有就open -1 没有就是close + 1

4. [227. Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/)

    原理：
    关键的地方是cur_ops是记录的前一个的运算符，不是当下的运算符
    每个循环末尾要reset cur_num 和把当前的operation 传递到cur_ops里
    如果碰到数字，那么先得到完整的数字
    **碰到运算符号的时候是我们要进行运算或者是stack operation的时候**
    如果碰到符号，那么就分4种情况讨论
    1. 加号就直接append
    2. 减号append负的数字，因为这里的cur_ops是前一个的符号，而不是当前符号
    3. 乘号就先把top of stack 做乘法然后push回去
    4. 除法跟乘法一样，只不过有一个小的corner case 我在下面的注释解释了

5. [636. Exclusive Time of Functions](https://leetcode.com/problems/exclusive-time-of-functions/)

    top of stack 是current fucntion id
    pre_time记录了当前时间的前一个时间，这个时间是用来记录和计算一个function运行一个小时间段的开始(start time)的。然后每一次iterate 到的时间就是
    这个小时间段的结束(end time)
    原理：
    用stack来记录和存储当前以及还没完成的function的数据。
    如果一个function从头到尾都完成了，那么我们用开始和结束时间记录出运行时间然后pop出stack
    如果一个function开始了，current log是另一个时间，那么就会计算之前那个function的运行时间，save，然后再把当前的function的运行status push stack里最后update pre_time.

6. [1047. Remove All Adjacent Duplicates In String](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/)

    原理：
    用stack来记录前一个ch。如果当前的ch 和top of stack 一样，那么pop出去
    其它情况就一直append进stack就可以了

7. [71. Simplify Path](https://leetcode.com/problems/simplify-path/)

    原理：
    遇到"." 或者空，那么就do nothing
    遇到".."，我们需要pop
    其它的情况append 到stack里就可以了。

8. [1209. Remove All Adjacent Duplicates in String II](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/)

    ```python
    stack = [(ch, count)]
    ```

    原理：
    用stack 记录当前的ch 和已经出现的次数。
    注意，每一次重复出现都要push 一个新的ch 进stack，而不是update 字符的个数
    1. 空stack 直接append
    2. 没有遇到和当前top of stack 重复的字母直接append
    3. 遇到重复度要看重复的次数是不是已经达到了k个，如果达到要pop k个，没达到就继续append

9. [1944. Number of Visible People in a Queue](https://leetcode.com/problems/number-of-visible-people-in-a-queue/)

10. [739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)
    
    原理：
    单调递增stack。只有在top of stack 小于当前的value 的时候我们需要pop 出来。
    然后进行res更新。

11. [224. Basic Calculator](https://leetcode.com/problems/basic-calculator/)


## Conlution

1249， 921是两道括号的题目。用到的stack基本概念解题。open和close各一个stack
1047， 1209 是remove adjacent。第一个用最简单的stack。第二题push 到stack里的内容时候需要多加一个count
227， 636 两道题目是需要有另外辅助的var 来记录之前一次的state，从而在加一次遇到的时候需要用到前一次的state 来进行操作。
1762 monotonic是一个常用的数据结构
