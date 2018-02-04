##########################################################
#Factorial
##########################################################
fact_memo = {0:1, 1:1}

def genNthFactorialNaive(n): #quickly recurses out
    if (n == 0 or n == 1):
        return 1
    return n*genNthFactorialNaive(n-1)

def genNthFactorialMemo(n): #also recurses out <-- should it - yes because missing dict entries
    if (n < 2):
        return fact_memo[n]
    if n-1 not in fact_memo:
        fact_memo[n] = n*genNthFactorialMemo(n-1)
        return fact_memo[n]
    else:
        return n*fact_memo[n-1]

def genNthFactorialUpDict(n): #linear time --> dynamic programming
    fact_memo = {0:1}
    for k in xrange(1,n+1):
        fact_memo[k] = k*fact_memo[k-1]
        del fact_memo[k-1] #keep dictionary small
    return fact_memo[n]

def genNthFactorialSexy(n): #linear time --> slightly (constant) faster than up dict 
    return reduce(lambda x,y: x*y, xrange(1,n+1))

def genNthFactorial(n): #linear time --> fastest
    last_fact = 1
    for k in xrange(1,n+1):
        new_fact = k*last_fact
        last_fact = new_fact
    return new_fact

"""

import cProfile, pstats, StringIO
pr = cProfile.Profile()
pr.enable()

genNthFactorial(100000)
genNthFibonacci(100000) #fibonacci faster than factorial

pr.disable()
s = StringIO.StringIO()
sortby = 'cumulative'
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print s.getvalue()

"""
