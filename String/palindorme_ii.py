class palindromeII:
    def validPalindrome(self, s: str) -> bool:
        # Time: O(2n)
        # Space: O(3n)
        front, end = 0 , len(s) - 1
        error_tolarence = 0
        while front <= end:
            if s[front] != s[end]:
                one, two = s[front: end], s[front + 1: end + 1]
                return one == one[::-1] or two == two[::-1]
            else:
                front +=1 
                end -=1
        return True