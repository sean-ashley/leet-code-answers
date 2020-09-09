class Solution:
    global memo
    memo = {}
    def climbStairs(self, n: int) -> int:
        #dynamic programming it
        if n <= 2:
            return n
        if n not in memo:
            memo[n] = self.climbStairs(n-2) + self.climbStairs(n-1)
        return memo[n]
        
