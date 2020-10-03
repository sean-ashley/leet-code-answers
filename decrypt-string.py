class Solution:
    def freqAlphabets(self, s: str) -> str:
        import string
        
        str_list = list(string.ascii_lowercase)
        decoder = {}
        for i in range(1,27):
            decoder[str(i)] = str_list[i-1]
            
        hash_count = s.count('#')
        i = 0
        
        decoded_str = ''
        while i < len(s):
            if hash_count != 0 :
                
                if s[i+2] == '#':
                    decoded_str += decoder[s[i:i+2]]
                    i += 3
                    hash_count -= 1
                
                else:
                    decoded_str += decoder[s[i]]
                    i+=1
            else:
                decoded_str += decoder[s[i]]
                i+=1
                
        return decoded_str
                
                                                           
        
        
