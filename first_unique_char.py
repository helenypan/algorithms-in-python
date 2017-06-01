'''
takes a string as input and returns the first non-repeated charcater in the input string. 
If there are no unique characters return None.

if input is 'a', return a;
if input is '112233', return None
if input is 'aabbcdd124', return c
'''

def first_unique(string):
	if len(string) == 1:
		return string[0]
	else:
		for i in range(len(string)):
			if (i == 0 and string[i] != string[i+1]) or \
			(i == len(string)-1 and string[i] not in string[:i]) or \
			(string[i] not in string[:i] and string[i] != string[i+1]):
				return string[i]
		return None

def test_1():
	assert first_unique("s") == "s"
	assert first_unique("aabbcdd") == "c"

def test_2():
	assert first_unique("a") == "s"
	assert first_unique("aabbedd") == "c"