def fib(x):
    if x < 2:
        return x
    else:
        return fib(x-1) + fib(x-2)

print("result:", fib(6))

## 위의 로직을 한 줄로 표현하면 다음과 같습니다.
#def fibonacciSeqquence(x):
#    return fibonacciSeqquence(x-1) + fibonacciSeqquence(x-2) if x >= 2 else x 

#print(fibonacciSeqquence(4))

# Fibonacci Problem
# Sample Input: 6  -> Sample Output: 0 1 1 2 3 5
def fibPrint(x):
    rtn = 0
    if x < 2:
        rtn =  x
    else:
        rtn = fibPrint(x-1) + fibPrint(x-2)

    return rtn

print("result:", fibPrint(6))


def fibonacci(num):
    a, b = 0, 1
    for i in range(num):
        a, b = b, a+b
    return a
print("result:", fibonacci(6) )

#출처: https://excelsior-cjh.tistory.com/31 [EXCELSIOR]