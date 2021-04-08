class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        from collections import deque
        levels = []
        
        #intialize queue with root
        queue = [root] if root else None
      
        # while we still have a queue
        while queue:

            level = []
            queue_copy = queue.copy()
            for node in queue_copy:
                #append root to level
                level.append(node.val)
                #pop out root from queue
                queue.pop(0)
                #append left and right nodes to queue if they exist
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            levels.append(level)
        
        return levels
