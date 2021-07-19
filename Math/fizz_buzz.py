from typing import List

class fizzBuzz:
    def fizzBuzz(self, n: int) -> List[str]:
        # # solution 1
        # answer = []
        # for i in range(1, n + 1):
        #     if i % 3 == 0  and i % 5 == 0:
        #         answer.append("FizzBuzz")
        #     elif i % 3 == 0:
        #         answer.append("Fizz")
        #     elif i % 5 == 0:
        #         answer.append("Buzz")
        #     else:
        #         answer.append(str(i))
        # return answer

        # # solution 2:
        # answer = []
        # for i in range(1, n + 1):
        #     tmp_str = ""
        #     if i % 3 == 0:
        #         tmp_str += "Fizz"
        #     if i % 5 == 0:
        #         tmp_str += "Buzz"
        #     if not tmp_str:
        #         tmp_str += str(i)
        #     answer.append(tmp_str)
        # return answer

        # solution 3: hash
        key_dict = {3: "Fizz", 5: "Buzz"}
        answer = []
        for i in range(1, n + 1):
            tmp_str = ""
            for key in key_dict.keys():
                if i % key == 0:
                    tmp_str += key_dict[key]
            
            if not tmp_str:
                tmp_str += str(i)
            answer.append(tmp_str)
        return answer