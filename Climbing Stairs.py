class Solution:
    def climbStairs(self, n: int,memo = {}) -> int:
        
        #base cases
        if n == 1:
            return 1
        elif n==2:
            return 2
    
        #if n isnt in our dictionairy, add it
        if n not in memo.keys():
            #recursive call
            memo[n] = self.climbStairs(n - 1,memo) + self.climbStairs(n-2,memo)

        
        #return the value in the memo
        
        return memo[n]
            
