class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # # 灵活运用mod 是一个小的技巧
        # converted_hour = hour % 12

        # hour_part = converted_hour * 60 + minutes / 60 * 60
        # min_part = minutes / 60 * 720
        # res = abs(hour_part - min_part) / 720 * 360
        
        # # return 也可以写成 min(res, 360 - res)
        # # 因为就只有两种可能性
        # return 360 - res if res > 180 else res


        # # 第二遍
        # hour_degree_unit = 360 / 12
        # mins_in_hour = 60
        
        # total_degree = 360
        # half_degree = 360 / 2
        
        # # 这个就是公式
        # # 小时的度数就是，小时的整度数 + 在那一个小时里面分钟的度数
        # hour_degree = hour_degree_unit * hour + minutes / mins_in_hour * hour_degree_unit
        
        # # 分钟的度数比较直接，就是当前分钟减去一个小时的分钟数再乘以360度
        # minutes_degree = minutes / mins_in_hour * total_degree
        
        # res = minutes_degree - hour_degree
        
        # return abs(res) if abs(res) < half_degree else total_degree - abs(res)


        # 第三遍：
        min_angle = minutes / 60 * 360
        hour_angle = (60 / 12 * (minutes / 60) + hour * 60 / 12) / 60 * 360
        
        angle = hour_angle - min_angle if hour_angle > min_angle else min_angle - hour_angle
        abs_angle = angle if angle < 180 else 360 - angle
        
        return abs(abs_angle)