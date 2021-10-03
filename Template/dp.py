# *****首先，动态规划问题的一般形式就是求最值。
# 动态规划其实是运筹学的一种最优化方法，只不过在计算机问题上应用比较多，比如说让你求最长递增子序列呀，最小编辑距离呀等等。

# *****既然是要求最值，核心问题是什么呢？求解动态规划的核心问题是穷举。因为要求最值，肯定要把所有可行的答案穷举出来，然后在其中找最值呗。

# 先，动态规划的穷举有点特别，因为这类问题存在「重叠子问题」
# 而且，动态规划问题一定会具备「最优子结构」，才能通过子问题的最值得到原问题的最值。
# **只有列出正确的「状态转移方程」，才能正确地穷举。

# *****以上提到的重叠子问题、最优子结构、状态转移方程就是动态规划三要素。


# 初始化 base case
dp[0][0][...] = base
# 进行状态转移
for 状态1 in 状态1的所有取值：
    for 状态2 in 状态2的所有取值：
        for ...
            dp[状态1][状态2][...] = 求最值(选择1，选择2...)

# *****明确 base case -> 明确「状态」-> 明确「选择」 -> 定义 dp 数组/函数的含义。


# 但反过来，最优子结构性质作为动态规划问题的必要条件，一定是让你求最值的，
# ******以后碰到那种恶心人的最值题，思路往动态规划想就对了，这就是套路。


# 遍历方向的选择
# 1、遍历的过程中，所需的状态必须是已经计算出来的。
# 2、遍历的终点必须是存储结果的那个位置。


# 目前发现的压缩dp的维度有两道题
# 1216, 935
# 1216 是非常典型的压缩方式。详细请看那题的解法和 状态压缩：labuladong的算法小抄---对动态规划进行降维打击 https://labuladong.gitee.io/algo/3/24/65/
# 935是压缩三维到二维，三维用两个二维代替