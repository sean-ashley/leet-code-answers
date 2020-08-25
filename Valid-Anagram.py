class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        #get counter of letters in first word
        counter1 = Counter(s)
        #get counter of letters in second word
        counter2 = Counter(t)
        #return whether or not the counters are the same.
        return counter1 == counter2
            
        
