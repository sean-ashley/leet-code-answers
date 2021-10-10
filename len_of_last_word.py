class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        list_of_words = s.split()
        
        for i in reversed(list_of_words):
            if i is not " ":
                return len(i)
        
        return 0
