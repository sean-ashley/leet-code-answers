class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_so_far = ""
        i = 0
        try:
            while len(longest_so_far) != len(strs[0]):
                for k in strs:
                    if not k.startswith(longest_so_far + strs[0][i]):
                        return longest_so_far   
                longest_so_far += strs[0][i]
                i += 1


            return longest_so_far
        except IndexError:
            return longest_so_far
        
