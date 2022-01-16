from collections import Counter
import math

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # # 最优的解法是组成一个filtered s 只记录char 和char 的idx if char在t里面
        # # 然后loop filtered s  
        # if not s or not t:
        #     return ""
        
        # dict_t = Counter(t)
        # requried = len(dict_t)
        
        # l, r = 0, 0
        # char_formed = 0
        # window_counts = {}
        
        # res = (math.inf, None, None)
        
        # while r < len(s):
        #     char = s[r]
        #     window_counts[char] = window_counts.get(char, 0) + 1
        #     if char in dict_t and window_counts[char] == dict_t[char]:
        #         char_formed += 1
            
        #     while l <= r and char_formed == requried:
        #         char = s[l]
                
        #         if r - l + 1 < res[0]:
        #             res = (r - l + 1, l, r)
        #         window_counts[char] -= 1
        #         if char in dict_t and window_counts[char] < dict_t[char]:
        #             char_formed -= 1
        #         l += 1
        #     r += 1
            
        # return "" if res[0] == math.inf else s[res[1]: res[2] + 1]


        # # 第二遍
        # # rules:
        # # 1. 每到ch in dict_t的时候我们都要update的ch 的counter，如果counter == dict_t[ch]，就说明这个ch 达到了需要的个数
        # #     那么char_formed += 1
        # # 2. 每到char_formed == 本身的t的len时候(也就是required)：
        # #     那么我们就要开始移动最左边的l，看看能不能形成更小的substring 但是cover t的字母
        # # 3. 如果counter < dict_t[ch]
        # #     那么char_formed -= 1
        # # 4. l 向左移动也要减去相应的counter
        # char_formed = 0
        # dict_t = Counter(t)
        # required = len(dict_t)
        # window_counts = {}
        
        # filtered_s = []
        # # (res, l, r)
        # res = (math.inf, 0, 0)
        
        # for i in range(len(s)):
        #     if s[i] in dict_t:
        #         filtered_s.append((s[i], i))
        
        
        # l, r = 0, 0
        # while r < len(filtered_s):
        #     ch, idx = filtered_s[r]
        #     window_counts[ch] = window_counts.get(ch, 0) + 1
        #     if ch in dict_t and window_counts[ch] == dict_t[ch]:
        #         char_formed += 1
            
        #     while l <= r and char_formed == required:
        #         ch, idx = filtered_s[l]
        #         act_l, act_r = filtered_s[l][1], filtered_s[r][1]
                
        #         if act_r - act_l + 1 < res[0]:
        #             res = (act_r - act_l + 1, act_l, act_r)
                
        #         window_counts[ch] -= 1
        #         if ch in dict_t and window_counts[ch] < dict_t[ch]:
        #             char_formed -= 1
        #         l += 1
            
        #     r += 1
        
        # return "" if res[0] == math.inf else s[res[1]: res[2] + 1]


# 第三遍的方法比较好
        # 需要的所有ch 的count
        need = Counter(t)
        # 需要的长度
        missing = len(t)
        
        # start， end 是最后的final window边界
        # i 是sliding window的起始
        i, start, end = 0, 0, 0
        
        # j是sliding window的结束，所以从1 开始，因为i从0 开始
        for j, ch in enumerate(s, 1):
            
            # 如果need[ch] 大于0 表示找到一个在 t里面的字符，所以可以missing 减去1
            if need[ch] > 0:
                missing -= 1
            
            # 只要在sliding window里面，不管这个ch是不是t当中的ch， 都是需要减去1 表示当前的sliding window已经包含了这个ch
            need[ch] -= 1
            
            # sliding window里面包含了t所有的ch的时候，我们就要开始从左边缩减这个sliding window的宽度
            if missing == 0:
                # i< j好理解。这个need[s[i]] < 0 是精髓！！！ 不能是 need[s[i]] <= 0， 因为如果s[i] 是t当中的ch。 正好need[s[i]] == 0
                # 也就是说这个s[i]正好在sliding window的左边界。如果这个时候再进入循环，那么就会把这个s[i]从sliding window中去除，这样sliding window中就少了一个t中的ch
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                
                # 出了while循环代表现在这个sliding window是我能找到的最小的sliding window，然后把这个结果update 给start and end
                if end == 0 or j - i < end - start:
                    start, end = i, j
                
                # update以后，我们新的sliding window的左边起始点要从i + 1 开始。 既然是当前最小的sliding window，那么它的左边界的ch 一定是一个t当中的ch，而且不能被删掉，要不然不会跳出while循环
                # 所以要从i + 1开始的话，必须要update need[s[i]] 和missing 
                need[s[i]] += 1
                missing += 1
                i += 1
        return s[start:end]


# 0 1 2 3 4 5 6 7 8 9 10 11 12
# A D O B E C O D E B A  N  C
# l
# r

# ABC

# char_formed = 2
# requried = 3
# window_counts = {a:1,b:0,c:1}
# dict_t = {a:1, b:1, c:1}

# res = (4, 9, 12)

# filtered_s:[(a,0), (b, 3), (c, 5), (b, 9), (a, 10), (c, 12)]
#                                              l
#                                                      r
