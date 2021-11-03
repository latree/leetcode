
class Solution:
    def isNumber(self, s: str) -> bool:
        # # 分五大类: 是不是数字，是不是e，是不是dot，是不是加减号，其它
        # # 看见dot 就不能之前有dot，不能之前有e
        # # 看见e 之前不能有e，之前不能没有数字, e后面必须有数字
        # seen_digit = seen_dot = seen_exponent = False
        # for i, ch in enumerate(s):
        #     if ch.isdigit():
        #         seen_digit = True
        #     elif ch in ['+', '-']:
        #         if i > 0 and s[i - 1] != 'e' and s[i - 1] != 'E':
        #             return False
        #     elif ch in ['e', 'E']:
        #         if seen_exponent or not seen_digit:
        #             return False
        #         seen_exponent = True
        #         seen_digit = False
        #     elif ch == '.':
        #         if seen_dot or seen_exponent:
        #             return False
        #         seen_dot = True
        #     else:
        #         return False
        
        # return seen_digit

    # 第二遍：
        # 分五大类: 是不是数字，是不是e，是不是dot，是不是加减号，其它
        has_dot = has_digit = has_expo = False
        
        for i, ch in enumerate(s):
            # 有dot时候 之前有了dot 或者之前有了e那么就不是valid
            if ch == '.':
                if has_dot or has_expo:
                    return False
                has_dot = True
            # 看到加号，那么加号之前的字符只要不是e 那就是错的
            elif ch in ["+", "-"]:
                if i > 0 and s[i - 1] != "E" and s[i-1] != "e":
                    return False
            # 看到e 有点复杂。
            # 看到e必须保证之前没有e 否则错的
            # 看到e的时候，e前面必须要存在数字 否则错的
            # 看到e的时候，e之前的数字都可以忽略，可以重新按照是不是valid数字来检测
            elif ch in ["E", "e"]:
                if not has_digit or has_expo:
                    return False
                has_expo = True
                has_digit = False
            
            elif ch.isdigit():
                has_digit = True
            else:
                return False
        
        # 如果整个循环没有数字那么是错的
        return has_digit
    def call_function(self) -> None:
        self.isNumber("--7")
