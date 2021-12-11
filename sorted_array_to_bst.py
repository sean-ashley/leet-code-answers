class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        #base case
        if len(nums) == 0:
            return
        
        mid_index = len(nums) // 2
        print(mid_index)
        root = TreeNode(nums[mid_index])
        
        root.left = self.sortedArrayToBST(nums[:mid_index])
        root.right = self.sortedArrayToBST(nums[mid_index + 1:])
        
        return root
