#Recursion Yay
def fib(n):
    final = 0
    if n == 0:
        return 0
    if n == 1:
        return 1
    prev_fib = 1
    prev_prev_fib = 0
    start_n = 2
    while start_n != n:
        new_prev_fib = prev_fib + prev_prev_fib
        final += (new_prev_fib)
        prev_prev_fib = prev_fib
        prev_fib = new_prev_fib
        start_n +=1
    
    return prev_fib + prev_prev_fib

def fib_recursive(n):
    if n == 0: return 0
    if n ==1: return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)