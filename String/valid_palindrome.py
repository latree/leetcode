class Solution:
    def isPalindrome(self, s: str) -> bool:
        # i, j = 0, len(s) - 1

        # while i < j:
        #     if s[i] == ' ' or not s[i].isalnum():
        #         i += 1
        #         continue
        #     elif s[j] == ' ' or not s[j].isalnum():
        #         j -= 1
        #         continue
        #     else:
        #         if s[i].lower() != s[j].lower():
        #             return False
        #     i += 1
        #     j -= 1
        # return True 

# 第二遍
        i, j = 0, len(s) - 1
        while i <= j:
            if not s[i].isalnum():
                i += 1
                # continue 会miss 掉
                continue
            if not s[j].isalnum():
                j = 1
                # continue 会miss 掉
                continue
            if s[i].lower() != s[j].lower():
                return False
            
            i += 1
            j -= 1
            
        return True 
        


# s = "A man, a plan, a canal: Panama"