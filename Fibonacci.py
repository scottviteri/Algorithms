##########################################################
#Fibonacci
##########################################################
import numpy

fib_memo = {0:0, 1:1, 2:1}

def genNthFibonacciNaive(n): #runtime real bad <-- recursion for days
    if (n <= 2):
        if (n == 0):
            return 0
        return 1
    return genNthFibonacciNaive(n-1)+genNthFibonacciNaive(n-2)

def genNthFibonacciMemo(n): #better than genNthFibonacciNaive, eventually recurses out 
    if (n <= 2):
        return fib_memo[n]
    if n-1 not in fib_memo or n-2 not in fib_memo:
        fib_memo[n] = genNthFibonacciMemo(n-1) + genNthFibonacciMemo(n-2)
        return fib_memo[n]
    return fib_memo[n-1]+fib_memo[n-2]

def genNthFibonacciUpDict(n): #linear time
    fib_memo = {0:0, 1:1, 2:1}
    if n not in fib_memo:
        for k in xrange(3,n+1):
            fib_memo[k] = fib_memo[k-1] + fib_memo[k-2]
            del fib_memo[k-2] # keep dictionary small
    return fib_memo[n]

def genNthFibonacciLinear(n): #linear time
    if (n <= 1): 
        if n == 1:
            return 1
        else: 
            return 0
    else:
        second_last_fib = 0
        last_fib = 1
        new_fib = 0 #in case bad input return 0
        for _ in xrange(2,n+1):
            new_fib = last_fib + second_last_fib
            second_last_fib = last_fib
            last_fib = new_fib
        return new_fib

def genNthFibonacciLinearAlt(n): #linear time - tiny bit faster
    if (n <= 1): 
        if n == 1:
            return 1
        else: 
            return 0
    else:
        fib_1 = 1
        fib_0 = 0
        for _ in xrange(2,n+1):
            fib_1, fib_0 = fib_1 + fib_0, fib_1
        return fib_1

def genNthFibonacciClosed(n): #gets off due to precision of floating point
    root_5 = float(5**0.5)
    PHI = (1.0+root_5)/2.0
    phi = (1.0-root_5)/2.0
    return (PHI**n - phi**n)/(root_5)

def genNthFibonacciMatrix(n): #log(n) -- way faster 
    start_matrix = numpy.matrix([[1],[0]])
    T = numpy.matrix([[1,1],[1,0]], dtype=object)
    T_n = numpy.linalg.matrix_power(T,n-1)
    result_matrix = numpy.dot(T_n,start_matrix)
    return int(result_matrix[0,0])

#Fast squaring complexity equivalent to using Djikstra Formulas
#F(2n) = (2*F(n-1) + F(n)) * F(n) 
#F(2n-1) = F(n-1)**2 + F(n)**2

def genNthFibonacci(n): #use 2n formulas until next power is greater than n, then matrix method -- fastest log(n) 
    fib_1, fib_0 = 1, 0
    current_n = 1
    if n == 0: return 0
    while current_n*2 <= n:
        sq_fib_1, sq_fib_0 = fib_1*fib_1, fib_0*fib_0 
        mix_fib = fib_1*fib_0
        fib_1, fib_0 = sq_fib_1 + 2*mix_fib, sq_fib_0 + sq_fib_1
        current_n *= 2
    start_matrix = numpy.matrix([[fib_1],[fib_0]])
    T = numpy.matrix([[1,1],[1,0]], dtype=object)
    T_n = numpy.linalg.matrix_power(T,n - current_n)
    fib_1 = numpy.dot(T_n,start_matrix)[0,0]
    return int(fib_1)

############################################################
#Time
############################################################
"""
import time

t1 = time.time()
genNthFibonacciMatrix(100)
t2 = time.time()
genNthFibonacci(100)
t3 = time.time()

print t2-t1,t3-t2
"""
"""
print [genNthFibonacciLinear(x) for x in range(20)]
print [genNthFibonacciLinearAlt(x) for x in range(20)]
"""
