num_chars = 26

def print_sorted_strings(remaining):
	exe_print_sorted_strings(remaining, "")

def exe_print_sorted_strings(remaining, prefix):
	if remaining == 0:
		if is_in_order(prefix):
			print(prefix)
	else:
		for i in range(num_chars):
			c = ith_letter(i)
			exe_print_sorted_strings(remaining-1, prefix + c)


def is_in_order(s):
	for i in range(1, len(s)):
		prev = s[i-1]
		curr = s[i]
		if prev > curr:
			return False
	return True

def ith_letter(i):
	return chr(ord('a') + i)

print_sorted_strings(4)

