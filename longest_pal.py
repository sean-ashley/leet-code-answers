class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        #general idea, start at "middle" character and move outwards from it. treat ever element
        #as a possibl middle character, if we find a palindrome longer then a previous one, record it
        length = len(s)
        res = ""
        reslen = 0
        for i in range(len(s)):
            
            
            #for odd number
            l,r = i,i
            
            
            while l >= 0 and r < length and s[l] == s[r]:
                if (r - l + 1) > reslen:
                    res = s[l:r + 1]
                    reslen = r - l + 1
                
                l -= 1
                r += 1
            
            #for even number
            l,r = i, i+1
            while l >= 0 and r < length and s[l] == s[r]:
                if (r - l + 1) > reslen:
                    res = s[l:r + 1]
                    reslen = r - l + 1

                l -= 1
                r += 1
        
        return res
                
