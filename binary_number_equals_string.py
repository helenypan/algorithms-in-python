'''
This Script is to check if the value of a binary number(passed as a string) 
equals the hexadecimal representation of a string
'''

def compare_binary_to_hex(binary, hex):
	n1 = convert_from_base(binary, 2)
	n2 = conbert_from_base(hex, 16)

	if n1<0 or n2<0:
		return False
	return n1 == n2


def convert_from_base(number, base):
	if base <2 or (base >10 and base != 16):
		return -1
	value = 0
	for i in range(len(number)-1, -1, -1):
		digit = digit_to_value(number[i])
		if digit <0 or digit >= base:
			return -1
		exp = len(number) - 1 - i
		value = value + digit * (base ** exp)
	return value

def digit_to_value(c):
	# TODO
	return False

