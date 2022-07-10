def max_sub_array_of_size_k(k, arr):
  # TODO: Write your code here

  #set values to 0
  max_, curr_total, start = 0,0,0
  #loop thru array
  for i in range(len(arr)):
    #take running sum
    curr_total += arr[i]
    #when we reach the size of the contiguos array
    if i >= k-1:
      #take a max
      max_ = max(curr_total,max_)
      #subtract out the start of the array
      curr_total -= arr[start]
      #move the start 1 up
      start += 1

  return max_
