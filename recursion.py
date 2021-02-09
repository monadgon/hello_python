def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

print(fib(4)) # result is 5


def fibonacciSeqquence(x):
    return fibonacciSeqquence(x-1) + fibonacciSeqquence(x-2) if x >= 2 else 1 

print(fibonacciSeqquence(4))