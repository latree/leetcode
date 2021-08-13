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