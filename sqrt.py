def sqrt(n):
	return sqrt_helper(n, 1,n)

def sqrt_helper(n, min, max):
	if max < min:
		return -1
	guess = (min + max) // 2
	print(guess)
	if guess * guess == n:
		return guess
	elif guess*guess < n:
		return sqrt_helper(n, guess+1, max)
	else:
		return sqrt_helper(n, min, guess-1)

print(sqrt(25))