class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #create a hash table to store numbers
        hash_table = set()
        #loop thru lsit
        for i in nums:
            if i in hash_table:
                return True
            hash_table.add(i)
        return False
