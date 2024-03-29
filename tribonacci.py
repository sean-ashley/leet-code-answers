class Solution:
    def __init__(self):
        self.memo = {}
    def tribonacci(self, n: int) -> int:
        #base cases
        if n==0:
            return 0
        elif n==1:
            return 1
        elif n==2:
            return 1
        
        if n not in self.memo:
            self.memo[n] = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
        
        
        return self.memo[n]
