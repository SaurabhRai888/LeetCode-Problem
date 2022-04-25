class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n=len(p)
        result=[]
        s_p="".join(sorted(p))
        for i in range(0,len(s)-n+1):
            s_s="".join(sorted(s[i:i+n]))
            if s_s==s_p:
                result.append(i)
        return result
        