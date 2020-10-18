def quick_select(array, k):
	position = k - 1
	return quick_select_helper(array, position, 0, len(array) - 1)

def quick_select_helper(array, position, start_idx, end_idx):
	while start_idx <= end_idx:
		pivot_idx = start_idx
		left = start_idx + 1
		right = end_idx

		while left <= right:
			if array[left] > array[pivot_idx] and array[right] < array[pivot_idx]:
				swap(array, left, right)

			if array[left] < array[pivot_idx]:
				left += 1

			if array[right] > array[pivot_idx]:
				right -= 1
		swap(array, pivot_idx, right)
		if right == position:
			return array[right]
		elif right > position:
			end_idx = right - 1 
		else:
			start_idx = right + 1

def swap(array, left, right):
	array[left], array[right] = array[right], array[left]



print(quick_select([8,5,2,9,7,6,3],3))


