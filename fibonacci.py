'''
This script is to print all Fibonacci numbers from 0 to n.
this methond takes O(2**n) time
'''

def fib(n):
	if n <= 0:
		return 0
	elif n ==1 :
		return 1
	else:
		return fib(n-1) + fib(n-2)

def all_fib(n):
	for i in range(n):
		print(fib(i))

all_fib(10)