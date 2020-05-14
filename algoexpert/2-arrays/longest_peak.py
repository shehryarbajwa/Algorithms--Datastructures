

#Time Complexity O(N)
#Space Complexity O(1)

def longest_peak(array):
    longest_peak = 0
    i = 1

    while i < len(array) - 1:
        isPeak = array[i] > array[i - 1] and array[i] > array[i + 1]
        if not isPeak:
            i += 1
            continue

        left_index = i - 2

        while left_index >= 0 and array[left_index] < array[left_index + 1]:
            left_index -= 1

        right_index = i + 2

        while right_index < len(array) and array[right_index] < array[right_index - 1]:
            right_index += 1
        
        i = right_index
        print('right index:', right_index)
        print('left index:', left_index)
        current_peak_length = (right_index) - (left_index + 1)
        longest_peak = max(current_peak_length, longest_peak)

    return longest_peak

        
print(longest_peak([1,2,3,4,5,6,10,6,4,3,2,1,0]))






            
