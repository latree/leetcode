class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
#         size = len(s)
#         dp = [[0 for j in range(size)] for i in range(size)]
#         def helper(s: str, left: int, right: int) -> int:
#             if left == right:
#                 return 0
#             if left == right - 1:
#                 return 0 if s[left] == s[right] else 1
            
#             if dp[left][right]:
#                 return dp[left][right]
            
#             # case 1: char equal
#             if s[left] == s[right]:
#                 dp[left][right] = helper(s, left + 1, right - 1)
#                 return dp[left][right]
#             # case 2: char not equal: then there are two sub cases:
#             # 1. only move left ptr
#             # 2. only move right ptr
#             dp[left][right] = 1 + min(helper(s, left + 1, right), helper(s, left, right - 1))
#             return dp[left][right]
            
#         return helper(s, 0, size - 1) <= k

        # 转化方程
        # dp[left][right] 到目前为止最小需要remove char的个数使 s成为一个palindrome
#         if s[left] == s[right]:
#             dp[left][right] = dp[left + 1][right - 1]
#         else:
#             dp[left][right] = 1 + min(dp[left + 1][right], dp[left][right - 1])
            
#         return dp[0][n-1] <= k
#         n = len(s)
#         dp = [[0 for j in range(n)] for i in range(n)]
        
#         # i is left, j is right
#         # ************** 记住**************
#         # 这是一个小的trick需要记住：这个循环是iterate一个matrix 右上半的部分
#         for i in range(n - 2, -1, -1):
#             for j in range(i + 1, n, 1):
#                 if s[i] == s[j]:
#                     dp[i][j] = dp[i + 1][j - 1]
#                 else:
#                     dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j - 1])
            
#         return dp[0][n-1] <= k
        
        # solution 3: 压缩二维dp成一维dp
        # 关于压缩dp的维度请看文章 
        # labuladong 的算法小抄 > 第二章、手把手刷动态规划 > 动态规划基本技巧 > 状态压缩：对动态规划进行降维打击
        # https://labuladong.gitee.io/algo/3/24/65/
#         思维过程：
#         第一步：
#         ['x',  1,   1,   1], 
#         ['x', 'x',  1,   1], 
#         ['x', 'x', 'x',  1], 
#         ['x', 'x', 'x', 'x']
#         根据dp的推导公式：dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j - 1]) 和
#         dp[i][j] = dp[i + 1][j - 1]。
#         就不难看出dp[i][j] 只跟之前的三个一运算过的var 有联系，也就是说
#         dp[i + 1][j]， dp[i][j - 1] 和 dp[i + 1][j - 1]， 其实我们每一个循环推导dp[i][j]的过程中
#         只需要记录下来这三个var 的数值作为之后可以运用就好了。这样就能把二维dp 压缩成一维dp
#         ['x',  1,   1,   1], 
#         ['x', 'x',  S,   T], 
#         ['x', 'x',  S,   S], 
#         ['x', 'x', 'x', 'x']
#         dp[i + 1][j] 和 dp[i][j - 1] 就是上图中的 三个S，T就是dp[i][j]
        
#         第二步:
#         无脑去掉i这个这个维度。那么dp[j] = 1 + min(dp[j], [j - 1]) 和 dp[j] = dp[j - 1]。
#         上述代码的一维 dp 数组只能表示二维 dp 数组的一行 dp[i][..]，那我怎么才能得到
#         那我怎么才能得到 dp[i+1][j-1], dp[i][j-1], dp[i+1][j] 这几个必要的的值，进行状态转移呢？
#         更新 dp[j]，那么我们要来思考两个问题：
#         1、在对 dp[j] 赋新值之前，dp[j] 对应着二维 dp 数组中的什么位置？

#         2、dp[j-1] 对应着二维 dp 数组中的什么位置？

#         对于问题 1，在对 dp[j] 赋新值之前，dp[j] 的值就是外层 for 循环上一次迭代算出来的值，也就是对应二维 dp 数组中 dp[i+1][j] 的位置。

#         对于问题 2，dp[j-1] 的值就是内层 for 循环上一次迭代算出来的值，也就是对应二维 dp 数组中 dp[i][j-1] 的位置。
        
#         因为 for 循环遍历 i 和 j 的顺序为从左向右，从下向上，所以可以发现，在更新一维 dp 数组的时候，dp[i+1][j-1] 会被 dp[i][j-1] 覆盖掉，图中标出了这四个位置被遍历到的次序：用str 的数字表示
#         ['x',   1,     1,     1], 
#         ['x',  'x',   '3',   '4'], 
#         ['x',  'x',   '1',   '2'], 
#         ['x',  'x',   'x',   'x']
        
#         那么如果我们想得到 dp[i+1][j-1]，就必须在它被覆盖之前用一个临时变量 temp 把它存起来，并把这个变量的值保留到计算 dp[i][j] 的时候。
#         别小看这段代码，这是一维 dp 最精妙的地方，会者不难，难者不会。为了清晰起见，我用具体的数值来拆解这个逻辑：

# 假设现在 i = 5, j = 7 且 s[5] == s[7]，那么现在会进入下面这个逻辑对吧：

# if (s[5] == s[7])
#     // dp[5][7] = dp[i+1][j-1] + 2;
#     dp[7] = pre + 2;
# **************精髓****************
# 我问你这个 pre 变量是什么？是内层 for 循环上一次迭代的 temp 值。
# 那我再问你内层 for 循环上一次迭代的 temp 值是什么？是 dp[j-1] 也就是 dp[6]，但这是外层 for 循环上一次迭代对应的 dp[6]，也就是二维 dp 数组中的 dp[i+1][6] = dp[6][6]。
# **************精髓****************
# 也就是说，pre 变量就是 dp[i+1][j-1] = dp[6][6]，也就是我们想要的结果。
        
        n = len(s)
        dp = [0 for j in range(n)]
        
        # i is left, j is right
        # ************** 记住**************
        # 这是一个小的trick需要记住：这个循环是iterate一个matrix 右上半的部分
        for i in range(n - 2, -1, -1):
            
            # prev is holding the dp[i + 1][j - 1]
            prev = 0
            for j in range(i + 1, n, 1):
                # Store the value of dp[i+1][j] temporarily.
                temp = dp[j]
                if s[i] == s[j]:
                    dp[j] = prev
                else:
                    # dp[j] will contain the value for dp[i+1][j]
                    # dp[j-1] will contain the value for dp[i][j-1]
                    dp[j] = 1 + min(dp[j], dp[j - 1])
                
                # Copy the value of dp[i+1][j] to `prev`
                # For the next iteration when j=j+1
                # `prev` will hold the value dp[i+1][j-1];
                prev= temp
            
        return dp[n-1] <= k
