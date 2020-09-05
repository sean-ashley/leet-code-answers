def maximumToys(prices, k):
    num_toys = 0
    prices.sort()
    
    for i in prices:
        if k - i>= 0:
            k-= i
            num_toys+= 1
    return num_toys
