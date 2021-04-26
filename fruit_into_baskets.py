
class Solution:
                        
    def totalFruit(self, tree: List[int]) -> int:
        
        max_val = 0
        
        fruits = {}
        curr_total = 0
        for i,fruit in enumerate(tree):
            
            #update last known location of fruit
            fruits[fruit] = i
            #see if we ccan add to our basket count
            if len(fruits) < 2 or (len(fruits) == 2 and (fruit in fruits)):
                
                curr_total += 1
            
            
            #if we overflow our basket
            else:
                #see if we got a best
                max_val = max(max_val,curr_total)
                
                #this gives the right most index the first fruit appeared in, essentially giving us the number of the second fruit before we have to reset
                #this allows us to include that number in the next curr_total
                mindex = min(fruits.values())
                curr_total = i - mindex
                
                #reset the dict
                
                fruits = {fruit : i, tree[i-1] : i-1}
            
            
            #return the max
            
        return max(curr_total,max_val)
                
