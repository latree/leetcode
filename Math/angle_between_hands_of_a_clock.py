class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # 灵活运用mod 是一个小的技巧
        converted_hour = hour % 12

        hour_part = converted_hour * 60 + minutes / 60 * 60
        min_part = minutes / 60 * 720
        res = abs(hour_part - min_part) / 720 * 360
        
        # return 也可以写成 min(res, 360 - res)
        # 因为就只有两种可能性
        return 360 - res if res > 180 else res