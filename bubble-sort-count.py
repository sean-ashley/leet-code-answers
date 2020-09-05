# Complete the countSwaps function below.
def countSwaps(a):
    numswaps = 0
    for i in range(len(a)):
        for k in range(len(a)-i-1):
            if a[k] > a[k+1]:
               a[k],a[k+1]  = a[k+1],a[k]
               numswaps +=1
    print("Array is sorted in {0} swaps.\nFirst Element: {1}\nLast Element: {2}".format(numswaps,a[0],a[-1]))
