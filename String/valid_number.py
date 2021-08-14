
class Solution:
    def isNumber(self, s: str) -> bool:
        # 分五大类: 是不是数字，是不是e，是不是dot，是不是加减号，其它
        # 看见dot 就不能之前有dot，不能之前有e
        # 看见e 之前不能有e，之前不能没有数字, e后面必须有数字
        seen_digit = seen_dot = seen_exponent = False
        for i, ch in enumerate(s):
            if ch.isdigit():
                seen_digit = True
            elif ch in ['+', '-']:
                if i > 0 and s[i - 1] != 'e' and s[i - 1] != 'E':
                    return False
            elif ch in ['e', 'E']:
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True
                seen_digit = False
            elif ch == '.':
                if seen_dot or seen_exponent:
                    return False
                seen_dot = True
            else:
                return False
        
        return seen_digit

    def call_function(self) -> None:
        self.isNumber("--7")
