class Solution:
    def romanToInt(self, s: str) -> int:
        r=0
        d={'M':1000,'CM':900,'D':500,'CD':400,'C':100,'XC':90,'L':50,'XL':40,'X':10,'LX':9,'V':5,'IV':4,'I':1}

        for i in range(len(s)):
            if (i+l<len(s) and d[s[i]]<d[s[i+1]])
               r=r-d[s[i]]
            else:
                r=r+d[s[i]]
        return r

        
sol=Solution()
print(sol.roman("MCMXCIV"))
            
        
    