class Solution:
    def firstUniqChar(self, s: str) -> int:
        #import defaultdict class
        from collections import defaultdict
        #create dict object that defaults to 0
        hash_map = defaultdict(int)
        #loop thru string
        for i in s:
            #add 1 each time u see a character in the string
            hash_map[i] += 1
            
        for i in range(len(s)):
            #find the item that isnt a duplicate and return it
            if hash_map[s[i]] == 1:
                return i
        #if there no non duplicate there return -1
        return -1
        
