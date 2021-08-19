class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j = 0
        # corner case 需要test好几遍才cover了所有的case.
        while i < len(word):
            if j >= len(abbr):
                return False
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j].isdigit() and abbr[j] != '0':
                idx = j
                while j < len(abbr) and abbr[j].isdigit():
                    j += 1
                num = int(abbr[idx:j])
                
                if i + num > len(word):
                    return False
                i = i + num
            else:
                return False
        
        return i == len(word) and j == len(abbr)
