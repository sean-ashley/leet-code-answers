# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        #create a queue
        from collections import deque
        queue = deque([root])    
        avgs = []
        while queue:
            # take the length of the current level
            n = len(queue)
            # go thru the level
            sum_ = 0
            #loop thru n times, this assurs we will be taking down the left-right of each node in the level, hence giving us the next level
            for i in range(n):
                root = queue.pop()
                sum_ +=  root.val
                # go thru the level, attach the new level and take the average
                if root.left:
                    queue.appendleft(root.left)
                if root.right:
                    queue.appendleft(root.right)
            avgs.append(sum_ / n)
        
        return avgs
