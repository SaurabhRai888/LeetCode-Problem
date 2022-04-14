class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i=1
        while True:
            s=i*i
            if s==num:
                return True
            elif s>num:
                return False
            i+=1
        