class WordDictionary:
    # first question using trie data structure
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node['$'] = True

    def search(self, word: str) -> bool:
        def dfs(word, node) -> bool:    
            for i, ch in enumerate(word):
                if ch not in node:
                    if ch == '.':
                        for x in node:
                            if x != '$' and dfs(word[i + 1:], node[x]):
                                return True
                    return False
                else:
                    node = node[ch]
            return '$' in node

        return dfs(word, self.trie)
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

    # # 第二遍心得：
    # def __init__(self):
    #     self.trie = {}

    # def addWord(self, word: str) -> None:
    #     cur_node = self.trie
    #     for ch in word:
    #         if ch not in cur_node:
    #             cur_node[ch] = {}
    #         cur_node = cur_node[ch]
    
    # ************* note ******************
    #     # 必须有这个结尾的符号，要不然在trie里面可能在这一层还有其他的字母。
    #     # 只凭idx==len(word)不能作为判断这个词在不在trie里的依据，因为不知道词的底部
    #     cur_node['$'] = True

    # def search(self, word: str) -> bool:
    #     def dfs(word, idx, trie):
    #         if idx == len(word):
    
    # ************* note ******************
    #             # 必须有这个结尾的符号，要不然在trie里面可能在这一层还有其他的字母。
    #             # 只凭idx==len(word)不能作为判断这个词在不在trie里的依据，因为不知道词的底部
    #             return True if '$' in trie else False

    #         if word[idx] != '.' and word[idx] not in trie:
    #             return False
            
    #         res = True
    #         if word[idx] == '.':
    
    # ************* note ******************
    #             # 在遇到 '.' 的情况比较特殊，我们要iterate所有接下来的字母，
    #             # 并且不能iterate 到'$'因为当前的word还没有结束。
    #             # 在这之后的任何情况return True 都是我们需要的结果。所以必须要
    #             # 有一个temp 的dot_res去搜集所有case的结果，再和 res 做与逻辑
    #             # res = res and dot_res
    #             dot_res = False
    #             for k in trie.keys():
    #                 if k != '$':
    #                     dot_res = dot_res or dfs(word, idx + 1, trie[k])
    #             res = res and dot_res
    #         else:
    #             res = res and dfs(word, idx + 1, trie[word[idx]])
            
    #         return res

    #     return dfs(word, 0, self.trie)