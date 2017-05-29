def powersOf2(n):
	if n<1:
		return 0
	elif n ==1:
		print(2)
		return 2
	else:
		prev = powersOf2(n//2)
		curr = prev * 2
		print(curr)
		return curr

powersOf2(64)