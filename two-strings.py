# Complete the twoStrings function below.
def twoStrings(s1, s2):
    for i in s1:
        if i in s2:
            return 'YES'
    return 'NO'
