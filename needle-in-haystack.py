class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #if the needles not in the haystack, return -1
        if needle not in haystack:
            return -1
        #if the needles the empty string, return 0
        elif needle == '':
            return 0
        else:
            #loop thru the characters in the haystack
            for i in range(len(haystack)):
                #find the index where the needle is equal to the haystack (note will not index out of list since we know the needle is in  there, so we dont have to worry about catching the error.)
                if needle == haystack[i:i+len(needle)]:
                    return i
        
