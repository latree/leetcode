from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # the key is to find pattern and word mapping/graph
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)
        # key h*t, value: word
        patterns = {}
        for word in wordList:
            for i in range(len(word)):
                curPattern = word[:i] + "*" + word[i + 1:]
                patterns[curPattern] = patterns.get(curPattern, [])
                patterns[curPattern].append(word)
        
        queue = deque()
        queue.append(beginWord)
        steps = 0
        visited = set()
        while queue:
            size = len(queue)
            steps += 1
            for i in range(size):
                curWord = queue.popleft()
                visited.add(curWord)
                if curWord == endWord:
                    return steps
                for j in range(len(curWord)):
                    curPattern = curWord[:j] + "*" + curWord[j + 1:]
                    for nei in patterns[curPattern]:
                        if nei not in visited:
                            queue.append(nei)
        return 0
        
# *it: hit
# h*t: hit, hot
# hi*: hit
# *ot: hot, dot, lot
# ho*: hot
# d*t: dot
# do*: dot, dog
# l*t: lot, 
# lo*: lot, log
# *og: dog, log, cog
# c*g: cog, 
# co*: cog