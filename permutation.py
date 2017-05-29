def permutation(str):
	exe_permutation(str, "")


def exe_permutation(str, prefix):
	if len(str) == 0:
		print(prefix)
	else:
		for i in range0, len(str)):
			rem = str[:i] + str[i+1:]
			exe_permutation(rem, prefix + str[i])

permutation("123")