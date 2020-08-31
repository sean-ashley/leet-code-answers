# Complete the hourglassSum function below.
def hourglassSum(arr):
    hash_table = set()
    #loop thru 4 times as that is all u need (anymore and u get an index)
    for i in range(4):
        for k in range(4):
            #for each row, calculate the hourglass then shift to the right by 1
            hash_table.add(sum(arr[i][k:3+k]+[arr[i+1][1+k]]+arr[i+2][k:3+k]))
    return max(hash_table)
        
