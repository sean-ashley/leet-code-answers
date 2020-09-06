def fibonacci(n):

    # Write your code here.
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
