import math


def smallest_subarray_sum(s, arr):
  
  min_length = math.inf
  window_sum = 0
  window_start = 0
  for window_end in range(0, len(arr)):
      window_sum += arr[window_end]  # add the next element
    # shrink the window as small as possible until the 'window_sum' is smaller than 's'
      while window_sum >= s:
        min_length = min(min_length, window_end - window_start + 1)
        window_sum -= arr[window_start]
        window_start += 1
      
  if min_length == math.inf:
    return 0
  return min_length
