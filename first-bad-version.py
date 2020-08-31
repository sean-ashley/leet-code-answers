# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        right =n
        left = 1
        mid_idx = (right + left) // 2
        while left<=right:
            mid_idx = (right + left) // 2
            if isBadVersion(mid_idx):
                right = mid_idx - 1
            else:
                left = mid_idx +1
        return left
            
