def minimumAbsoluteDifference(arr):
    min_number = float('inf')
    arr.sort()
    for i in range(len(arr)-1):
        if abs(arr[i] - arr[i+1]) < min_number:
            min_number =  abs(arr[i] - arr[i+1])
    return min_number
