# given a smaller string s and a bigger string b , 
# design an algorithm to find all permutations of the shorter string within the longer one. 
# print the location of each permutation

s = "abbc"
b = "cbabadcbbabbcbabaabccbabcbbcssabbcaabbcbbaaccbbcaabbccaaabbc"

for index in range(len(b)-3):
	curr_str = b[index:index+4]
	if sorted(curr_str) == sorted(s):
		print("Found {} from index: {}".format(curr_str, index) )