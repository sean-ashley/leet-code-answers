class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r_counter = 0
        l_counter = 0
        total_count = 0
        
        for i in s:
            if i == 'R':
                r_counter +=1
            else:
                l_counter += 1
            
            if r_counter == l_counter:
                total_count += 1
                r_counter = 0
                l_counter = 0
            
        return total_count
        
