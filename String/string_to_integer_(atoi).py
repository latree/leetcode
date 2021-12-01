class Solution:
    def myAtoi(self, s: str) -> int:
        def read_digit(s, idx):
            start = idx
            end = idx
            while idx < len(s):
                if s[idx].isdigit():
                    end = idx
                else:
                    break
                idx += 1
            return s[start:end + 1]
                
        
        def convert_to_num(num_str, is_pos):
            res = 0
            times = 0
            for i in range(len(num_str) - 1, -1, -1):
                res += int(num_str[i]) * 10**times
                times += 1
            
            return res * is_pos
        

        is_pos = 1
        res = 0
        s = s.strip()
        
        if not s:
            return 0
        if s[0] == '+':
            s = s[1:]
        elif s[0] == '-':
            is_pos = -1
            s = s[1:]
    
    
        if s and s[0].isdigit():
            num_str = read_digit(s, 0)
            res = convert_to_num(num_str, is_pos)
            if -2**31 <= res <= 2**31 -1:
                return res
            elif res < -2**31:
                return -2**31
            else:
                return 2**31 -1
        else:
            return res
        