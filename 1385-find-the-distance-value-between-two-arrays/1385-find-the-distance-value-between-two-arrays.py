class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        c = 0
        for i in arr1:
            for j in arr2:
                if(d >= abs(j-i)):
                    break
            else:
                c += 1
        return c