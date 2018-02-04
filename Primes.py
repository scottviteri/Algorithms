import math
import Newton

#still want fast prime factorization -- quadratic method

def findNthPrimeNaive(n): #Real bad -- findFactors of each number and count up
    number = 1
    prime_count = 0
    while prime_count < n:
        number += 1
        if len(findFactorsNaive1(number))==2:
            prime_count += 1
    return number

def findFactorsNaive1(x): #Naive algorithm -- O(n^(1/2)), maybe can do better with prime factorization  
    divis=[]
    lst=xrange(1,int(math.sqrt(x))+1)
    for factor in lst:
        if x%factor==0:
            comp=x/factor
            divis.append(factor)
            divis.append(comp)
    return divis

def findNonTrivFactors(x):
    divis=[]
    lst=xrange(2,int(math.sqrt(x))+1)
    for factor in lst:
        if x%factor==0:
            comp=x/factor
            divis.append(factor)
            divis.append(comp)
    return divis


def findFactorsNaive2(n): #slightly slower than findFactors1 but is pretty   
    return set(reduce(list.__add__, 
                      ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

#has nth root
def isSquare(n): #only for positive integer n
    x = n // 2
    seen = set([x])
    while n != x**2: #iterate and find the square root
        x = (x+(n//x)) // 2
        if x in seen:  
            return False #has converged on wrong answer
        seen.add(x)
    return True # n == x**2

#difficult asymptotic complexity to calculate
#procedure - check like normal to log(n), afterwards repeated use difference of squares
#analyze convergence rate
#b**2 - a**2 = (a+1)**2 - a**2 = 2a + 1 <-- odd number generator
def findFactors(n):
    prime_list = findPrimesUnderN(int(math.log(n)))
    #need terminating condition for recursion
    factor_list = []
    for p in prime_list:
        while n % p == 0:
            n /= p
            factor_list.append(p)
    #now have a number to factor that may be divided by larger primes
    #will be odd, so can generate with consecutive squares
    a = (n-1)/2 #n = b**2 - a**2 = (b+a)(b-a) --> trivial factorization -- need better 
    
#eventually want to use generaly number field sieve, as it is really super efficient but complicated
#lso want non-deterministic checker    
def isPrime(x): #O(n^(1/2)) from findFactorsNaive1
    return len(findFactorsNaive1(x)) == 2

#############################################################
#findPrimesUnderN
#############################################################

"""
Notes:
The Euler Sieve gets rid of the numbers that are confirmed composites, in order to do fewer checks. However, the big intermediate operations needed to do this make it much slower than the Sieve of Eratosthenes. Use the latter (O(n*loglog(n))).
"""

def findPrimesUnderNEuler(n): #Euler Sieve - remove composite from sieve checking
    full_lst = xrange(3,n,2) #iterating through integers
    full_set = set(full_lst) #convert to set - O(n)
    full_set.add(2)
    composite_set = set([]) #initialize empty set - O(1)
    for i in full_lst: #O(n) * average inside loop
        if(i not in composite_set): #check set inclusion - O(1)
            composite_set.update(findMults(i,full_set,n)) #add all mults to composite set 
            full_set -= composite_set #remove all update composites
    return full_set #return set of primes - O(1)

def findMults(divisor, full_set, max_val):
    composite_lst = [] 
    for multiple in xrange(divisor**2, max_val, divisor): #increment by divisor to get multiples, but don't get rid of original divisor (the base is prime)
        if multiple in full_set: #check if multiple has not been crossed out yet
            composite_lst.append(multiple) 
    return composite_lst

#with i**2 optimization
def findPrimesUnderN(n): #Sieve of Eratosthenes -- O(n*log(log(n)))
    A = [None]*2 + [True]*n #initialize list, assuming all are prime
    for i in xrange(2, int(n**0.5)+1):  
        if A[i]: #if a number is prime, find multiples
            for j in xrange(i**2,n+1,i): #start at i**2 and iterate by i
                A[j] = False #set multiples to not prime
    return [i for i in range(n) if A[i]==True] 

######################################################
#PrimeFactorization
######################################################


def setupPrimeFactorization(n): #Sieve of Eratosthenes not optimized -- not quite  O(n*log(log(n)))
    global sieve_dict
    global primes_set
    sieve_dict = {integer:0 for integer in range(2,n+1)}  # empty dictionary
    #initialize list, assuming all are prime
    for i in xrange(2, n): 
        for j in xrange(i,n+1,i): #start at i and iterate by i
            if sieve_dict[j] == 0:
                sieve_dict[j] = i #not prime
    primes_set = set([x for x in sieve_dict if x==sieve_dict[x]])

def findPrimeFactorization(n): #log(n), after sieve setup
    prime_fact_lst = [] 
    while n not in primes_set: 
        prime_fact_lst.append(sieve_dict[n])
        n /= sieve_dict[n]
    prime_fact_lst.append(n)
    return prime_fact_lst

def calculateTotient(n): #log(n), after sieve setup
    prime_fact_lst = findPrimeFactorization(n) #O(f) after setup
    prime_fact_set = set(prime_fact_lst) #remove duplicates
    for prime_factor in prime_fact_set: #O(s) where s is num unique prime factors
        n *= (1 - 1.0/prime_factor) #euler's totient formula
    return int(round(n,0)) #make sure is integer
#right now finding all factors -- taking too much memory 
#could fix by implementing separate classes -- too slow

###############################
#To time:
###############################

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

def time(n):
    import timeit
    wrapped = wrapper(findNthPrimeNaive,n)
    print timeit.timeit(wrapped, number = 1)
    #wrapped = wrapper(findNthPrimeNaive,n)
    #print timeit.timeit(wrapped, number = 1)

#time(100)
