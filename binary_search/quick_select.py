def quickselect(array, k):
    # Write your code here.
    position = k - 1
	return quick_select_helper(array, 0, len(array) - 1, position)

def quick_select_helper(array, start_idx, end_idx, position):
	while True:
		#start > end:
		
		pivot = start_idx
		left = start_idx + 1
		right = end_idx
		
		while left <= right:
			if array[left] > array[pivot] and array[right] < array[pivot]:
				swap(array, left, right)
			if array[left] <= array[pivot]:
				left += 1
			if array[right] >= array[pivot]:
				right -= 1
		swap(array, pivot, right)
		if right == position:
			return array[right]
		elif right < position:
			start_idx = right + 1
		elif right < position:
			end_idx = right - 1
				
def swap(array, left, right):
	array[left], array[right] = array[right], array[left]