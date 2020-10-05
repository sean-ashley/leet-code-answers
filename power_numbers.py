class Solution:
    def maxPower(self, s: str) -> int:
        
        
        max_count = 1
        
        curr_count = 1
        
        
        for i in range(len(s)-1):
            
            if s[i] == s[i+1]:
                curr_count += 1
            
            else:
                curr_count = 1
            
            
            if curr_count > max_count:
                max_count = curr_count
                
            
            
        return max_count
        
        
        
