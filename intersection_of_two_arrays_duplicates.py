class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        from collections import Counter

        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        results = []

        for i in nums1:
            if (i in nums2) and (counter1[i]) and (counter2[i]):
                smaller_num = min(counter1[i], counter2[i])
                for k in range(smaller_num):
                    results.append(i)
                    counter1[i] = 0

        return results
