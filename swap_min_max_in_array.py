'''
This script is to swap the min and max element in an interger array
'''

def swap_min_max(arr):
	print("Old Array:",arr)
	min_index,max_index = get_min_max_index(arr)
	new_arr = swap(arr, min_index, max_index)
	print("New Array:", new_arr)


def get_min_max_index(arr):
	min_index = 0
	max_index = 0
	for i in range(1, len(arr)):
		if arr[i] < arr[min_index]:
			min_index = i
		if arr[i] > arr[max_index]:
			max_index = i
	return min_index, max_index


def swap(arr, index_1, index_2):
	tmp = arr[index_1]
	arr[index_1] = arr[index_2]
	arr[index_2] = tmp
	return arr


swap_min_max([2,3,5,1,3,8,3,2,2,0,6,5,3,23,12,9,6,1,2,4])

