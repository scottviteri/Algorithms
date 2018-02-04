import sympy 
import math

def newtonsMethod(f, fprime, guess_x, num_steps): #find zero of function, currently log(d)*F(d)
    #could be improved by controlling precision
    current_step = 1
    while current_step <= num_steps:
        delta_x = -1 * float(f(guess_x)) / fprime(guess_x) #F(d), d-digit precision
        guess_x += delta_x
        print current_step, guess_x
        current_step += 1
    return guess_x

def hasKthRoot(n, k): #only for positive integer n, log(n) time
    x = n // k #starting guess
    seen = set([x])
    while n != x**k: #iterate and find the square root
        x = ( x*(k-1) + (n // (x**(k-1)) ) ) // k
        if x in seen:  
            return False #has converged on wrong answer
        seen.add(x)
    return True # n == x**k

def isSquare(n): #only for positive integer n, log(n) time
    x = n // 2 #starting guess
    seen = set([x])
    while n != x**2: #iterate and find the square root
        x = (x+(n//x)) // 2
        if x in seen:  
            return False #think has converged on wrong answer, not 100%
        seen.add(x)
    return True # n == x**2

####################################################
#Example
####################################################

def test():
    x = sympy.Symbol('x')
    f = x**2 - x - 1
    fprime = sympy.lambdify(x, f.diff(x))
    f = sympy.lambdify(x, f)
    newtonsMethod(f, fprime, 1, 6) 
    
#test()
