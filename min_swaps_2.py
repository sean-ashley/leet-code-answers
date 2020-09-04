def minimumSwaps(arr):
    #create dict mapping vals to idx
    nums = {}
    #initialize num swaps at 0
    num_swaps = 0
    for i in range(len(arr)):
        nums[arr[i]] = i
    #loop thru list
    for i in range(len(arr)):
        #if the value isnt in the right position
        if arr[i] != i+1:
            #store this value for later when we update the dict
            curr = arr[i]
            num_swaps+=1
            #swap the val at the cur idx with the correct val, and the incorrect val
            #with the idx of the correct val.
            arr[i],arr[nums[i+1]] = i+1, arr[i]
            #update dict so it accuratly maps
            nums[curr] = nums[i+1]
            nums[i+1] = i
    return num_swaps
