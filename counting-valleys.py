# Complete the countingValleys function below.
def countingValleys(n, s):
    level = 0
    vals =0 
    for i in s:
        if level == -1 and i == 'U':
            vals += 1
        if i == 'U':
            level += 1
        else:
            level -= 1
    
    return vals
