from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for ch in tasks:
            freq[ord(ch) - ord('A')] += 1
        
        freq.sort()

        freq_max = freq.pop()
        idle_time = (freq_max - 1) * n


        while freq and idle_time:
            # 这里是最不好理解的地方，
            # 如果input 的是 aabb，那么最frequent的task 就有两个。那么取一个freq_max 和freq.pop()最小值就是必须的
            idle_time -= min(freq_max - 1, freq.pop())
        idle_time = max(0, idle_time)

        return idle_time + len(tasks)
