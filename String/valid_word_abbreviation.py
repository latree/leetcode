class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # i = j = 0
        # # corner case 需要test好几遍才cover了所有的case.
        # while i < len(word):
        #     if j >= len(abbr):
        #         return False
        #     if word[i] == abbr[j]:
        #         i += 1
        #         j += 1
        #     elif abbr[j].isdigit() and abbr[j] != '0':
        #         idx = j
        #         while j < len(abbr) and abbr[j].isdigit():
        #             j += 1
        #         num = int(abbr[idx:j])
                
        #         if i + num > len(word):
        #             return False
        #         i = i + num
        #     else:
        #         return False
        
        # return i == len(word) and j == len(abbr)


        # 第二遍
        i, j = 0, 0 
        
        while i < len(word) and j < len(abbr):
            if not abbr[j].isdigit():
                if word[i] == abbr[j]:
                    i += 1
                    j += 1
                else:
                    return False
            else:
                # get number
                num = 0
                times_ten = 0
                if abbr[j] == '0':
                    return False
                while j < len(abbr) and abbr[j].isdigit():
                    num = 10 **times_ten * num + int(abbr[j])
                    j += 1
                    times_ten += 1
                i += num

        # ***** important ******
        # 最主要的就是这个i 和j 最后必须是同时到达length of word and length of abbr
        return i == len(word) and j == len(abbr)