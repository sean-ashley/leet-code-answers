class Solution:
    def romanToInt(self, s: str) -> int:
        #make dict
        
        rome_to_int = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        
        total = 0
        
        
        for i in range(len(s)):
            
            
            #check special cases
            if (s[i] == "I" and (i < len(s) - 1)) and ( (s[i+1] == "V") or s[i+1] == "X"): 
                total += -1
            
            elif (s[i] == "X" and (i < len(s) - 1)) and ( (s[i+1] == "L") or s[i+1] == "C"):
                total += -10
            
            elif (s[i] == "C" and (i < len(s) - 1)) and ( (s[i+1] == "D") or s[i+1] == "M"):
                total += -100
                
            
            #normal case
            else:
                total += rome_to_int[s[i]]
            
        
        
        return total
