class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        total = 0
        
        curr = n
        if n == 1 or n == 0:
            return n
        for i in range(1,n+1):
            

            if curr - i >= 0:
                total += 1
                curr -= i
            else:
                return total
