# Complete the makeAnagram function below.
def makeAnagram(a, b):
    from collections import Counter
    #initialize number of moves
    num_moves = 0
    #initialize counters
    a_count = Counter(a)

    b_count = Counter(b)
    #while there are more of a letter in a then b, remove it and add a move
    for i in a:
        while  a_count[i] > b_count[i]:
            num_moves += 1
            a_count[i] -= 1
    #do the same for b
    for i in b:
        while  b_count[i] > a_count[i]:
            num_moves += 1
            b_count[i] -= 1
    return num_moves
