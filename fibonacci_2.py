'''
This script is another way to print all Fibonacci numbers from 0 to n, 
this time it is 0(n) time, this technique called memoization, is a very common one to optimise 
exponential time recursive algorithms.
'''

def fib(n, memo):
	if n <= 0:
		return 0
	elif n ==1:
		return 1
	elif memo[n] is not None:
		return memo[n]
	else:
		memo[n] = fib(n-1, memo) + fib(n-2, memo)
		return memo[n]

def all_fib(n):
	memo = [None]*n
	for i in range(n):
		print(fib(i, memo))

all_fib(10)