class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        
#         right is the number of the right most lighted bulb.

#         Iterate the input light A,
#         update right = max(right, A[i]).

#         Now we have lighted up i + 1 bulbs,
#         if right == i + 1,
#         it means that all the previous bulbs (to the left) are turned on too.
#         Then we increment res
        
        right = res = 0
        for i, a in enumerate(flips, 1):
            right = max(right, a)
            if right == i:
                res += 1
            
        return res