class Solution:
    def reverse(self, x: int) -> int:
        xrev=int(str(abs(x))[::-1])
        if xrev <-2**31 or xrev>(2**31)-1:
            return 0
        
        if x < 0:
            return xrev*(-1)

        return xrev
        