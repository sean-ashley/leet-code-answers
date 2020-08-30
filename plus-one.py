class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        
        number = ''
        
        
        
        for i in digits:
            number+= str(i)
        num_plus_one = str(int(number) + 1)
            
        
        return [int(i) for i in num_plus_one]
