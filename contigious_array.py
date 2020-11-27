class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        from collections import defaultdict

        maxlen = 0

        indices = {0: -1}

        count = 0

        for i in range(len(nums)):

            count = (count + 1) if nums[i] == 1 else (count - 1)

            if count in indices:
                maxlen = max(maxlen, i-indices[count])
            else:
                indices[count] = i

        return maxlen
