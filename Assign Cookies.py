class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        #sort both lists and greedy dat mandem
        
        g.sort()
        s.sort()
        
        #manually loop thru lsit with while loop
        
        i = 0
        j = 0
        happy_kids = 0
        
        while i < len(g) and j < len(s):
            
            #if the child can be satisfied, increment happy_kids and move up to the next kid/cookie
            if g[i] <= s[j]:
                happy_kids += 1
                
                i += 1
            j+= 1
            
        
        
        return happy_kids
