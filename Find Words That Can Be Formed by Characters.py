
class Solution:

    
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        #get count of chars 
        
        count_chars = Counter(chars)
        
        #instantiate total count
        total_count = 0
        for word in words:
            count2 = Counter(word)
            
            add = True
            for char in word:
                #if there are more words in this character then we can use, we cant add it
                if count2[char] > count_chars[char]:
                    add = False
                    break
            
            if add:
                total_count += len(word)
            
        return total_count
        
