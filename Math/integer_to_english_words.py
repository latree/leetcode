class Solution:
    def numberToWords(self, num: int) -> str:
        def one(num):
            switcher = {
                1: 'One',
                2: 'Two',
                3: 'Three',
                4: 'Four',
                5: 'Five',
                6: 'Six',
                7: 'Seven',
                8: 'Eight', 
                9: 'Nine'
            }
            return switcher.get(num)
        
        def two_less_20(num):
            switcher = {
                10: 'Ten',
                11: 'Eleven', 
                12: 'Twelve',
                13: 'Thirteen',
                14: 'Fourteen', 
                15: 'Fifteen', 
                16: 'Sixteen', 
                17: 'Seventeen', 
                18: 'Eighteen', 
                19: 'Nineteen'
            }
            return switcher.get(num)
        
        def ten(num):
            switcher = {
                2: 'Twenty',
                3: 'Thirty', 
                4: 'Forty', 
                5: 'Fifty',
                6: 'Sixty', 
                7: 'Seventy',
                8: 'Eighty',
                9: 'Ninety'
            }
            return switcher.get(num)
        
        def two(num):
            if not num:
                return ''
            elif num < 10:
                return one(num)
            elif num < 20:
                return two_less_20(num)
            else:
                tens = num // 10
                ones = num % 10
                return ten(tens) + ' ' + one(ones) if ones else ten(tens)
        
        def three(num):
            if not num:
                return ''
            hundred = num // 100
            rest = num % 100
            if hundred and rest:
                return one(hundred) + ' ' + 'Hundred' + ' ' + two(rest)
            if not hundred and rest:
                return two(rest)
            if hundred and not rest:
                return one(hundred) + ' ' + 'Hundred'
        
        if not num:
            return 'Zero'
        
        billion = num // 1000000000
        million = num % 1000000000 // 1000000
        thousand = num % 1000000000 % 1000000 // 1000
        rest = num % 1000000000 % 1000000 % 1000
        
        res = ''
        if billion:
            res += three(billion) + ' ' + 'Billion'
        if million:
            res += ' ' if res else ''
            res += three(million) + ' ' + 'Million'
        if thousand:
            res += ' ' if res else ''
            res += three(thousand) + ' ' + 'Thousand'
        if rest:
            # there is a space after thoudsand word, for example 12345
            # should be 'Twelve Thousand{space} Three Hundred Forty Five'
            res += ' ' if res else ''
            res += three(rest)
        return res
            