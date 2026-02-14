class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        num = ""
        
        for ch in s:
            if ch.isdigit() or (ch in "+-" and num == ""):
                num += ch
            else:
                break
        
        if num in ["", "+", "-"]:
            return 0
        #return int(num)
        return max(min(int(num), 2**31 - 1), -2**31)