class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #complete loop k times.
        for i in range(k):
            #remove the last element of the list and assign it to num
            last = nums.pop()
            #insert that number at the start, shifting the whole list forward
            nums.insert(0,last)
                    
                
