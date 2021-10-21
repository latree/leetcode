from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # freq = [0] * 26
        # for ch in tasks:
        #     freq[ord(ch) - ord('A')] += 1
        
        # freq.sort()

        # freq_max = freq.pop()
        # idle_time = (freq_max - 1) * n


        # while freq and idle_time:
        #     # 这里是最不好理解的地方，
        #     # 如果input 的是 aabb，那么最frequent的task 就有两个。那么取一个freq_max 和freq.pop()最小值就是必须的
        #     idle_time -= min(freq_max - 1, freq.pop())
        # idle_time = max(0, idle_time)

        # return idle_time + len(tasks)



        # 第二遍：
        # 这道题第二遍做也没做明白
        # 其实一共分两种情况讨论
        # 1. 最频繁的task 的idle 时间不能cover剩余的task
        # a, [b, c,] a, [d, e,] a, [f]
        # idle 的时间完全涵盖了剩下的task
        # 2. 最频繁的task 的idle 时间能cover剩余的task，并且可能有剩余
        # a, [b, c,] a, [b, d] a, [b,()], a, b
        # 这两种情况取最大值就可以了
        
        # 第一种很简单就是len(task)
        # 第二种首先要知道idle 的数量也就是[]的数量，应该是 a 频率再减去1， 也就是freq(a) - 1
        # 然后以a [(),()] 为单位一共重复了freq(a) - 1 次。然后a， [b, c] 的长度是1个a 加上一个1个idle的长度。
        # 那么a, [b, c,] a, [b, ()] a, [(),()] 的长度就是  (freq(a) - 1) * (1 + idle)
        # 最后再加上末尾的 最频繁的task 个数。如果两个task 频率一样就是2
        
        # frequencies of the tasks
        frequencies = [0] * 26
        for t in tasks:
            frequencies[ord(t) - ord('A')] += 1
        
        max_freq = max(frequencies)
        max_n = frequencies.count(max_freq)
        
        return max(len(tasks), (1 + n) * (max_freq - 1) + max_n)
