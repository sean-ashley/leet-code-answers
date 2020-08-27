class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #combine both lists
        merged_list = nums1 + nums2
        #sort list in logn time
        merged_list.sort()
        #if the list has an even length
        if len(merged_list) % 2 == 0:
            #add the two middle elements and divide by 2 and return 
            return (merged_list[len(merged_list)//2] + merged_list[len(merged_list)//2 - 1]) / 2
        else:
            #return middle element
            return merged_list[len(merged_list)//2]
            
