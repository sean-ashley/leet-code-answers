
class Solution:
    def __init__(self):
        self.memo = {1:1,2:1}
    def fib(self, n: int) -> int:
        #base case
        if n == 0:
            return 0
        if n==1 or n==2:
            return 1
        if n not in self.memo:
            self.memo[n] = self.fib(n-1) + self.fib(n-2)
        
        return self.memo[n-1] + self.memo[n-2]
