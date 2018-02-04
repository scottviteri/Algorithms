from Fibonacci import genNthFibonacci

current_fib = 0
total_sum = 0
n = 0
while current_fib <= 4000000:
    total_sum += current_fib    
    current_fib = genNthFibonacci(n)
    n+=3
print total_sum
