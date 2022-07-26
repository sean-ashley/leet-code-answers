from collections import deque

def longest_substring_with_k_distinct(str1, k):
  curr_chars = deque()
  max_ = 0
  start_window = 0
  i= 0

  while i < len(str1):

    #add the first letter to curr_chars
    curr_chars.append(str1[i])

    #if curr_chars is over k, we reduce the sliding window
    while len(set(curr_chars)) > k:
      #remove the first letter in the deque
      curr_chars.popleft()
      # move up the start of sliding window
      start_window += 1
    
    #take our nex max 
    max_ = max(max_, i - start_window + 1)
    #move up end of sliding window
    i += 1

  return max_
