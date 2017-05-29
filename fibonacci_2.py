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