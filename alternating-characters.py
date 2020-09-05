# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    #init num_moves at 0
    num_moves = 0
    #loop from 1 to len(s) to avoid index error a i-1 check
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            num_moves+=1
    
    return num_moves
