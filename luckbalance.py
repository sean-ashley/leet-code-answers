# Complete the luckBalance function below.
def luckBalance(k, contests):
    #sort it such that the unimportant contests come first, followed by  the highest value important contests
    contests.sort(key = lambda x: x[1] * (1/x[0]))
    p = 0
    total_luck = 0
    #loop thru contests
    for i in contests:
        #if its not important , lose it automatically
        if i[1] == 0:
            total_luck += i[0]
        else:
            #if weve reached the amount of contests we can lose, subtract the luck
            if p == k:
                total_luck -= i[0]
            #otherwise add it 
            else:

                total_luck += i[0]
                p += 1
    return total_luck
