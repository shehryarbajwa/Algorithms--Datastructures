# Given list of integers that contain numbers in random_order, write a program to find rthe longest
#   sub sequence of consecutive numbers in the array
#   Return the subsequence in sorted array
#   Solution must take O(n) time


def longest_consecutive_subsequence(input_list):
    element_dict = dict()

    for index, element in enumerate(input_list):
        element_dict[element] = index

    max_length = -1
    starts_at = len(input_list)

        #input_list = [1,4,6,2]
    for index, element in enumerate(input_list):
        #current_starts at index = 0, current_starts = 0
        #iter 2, current_starts at 4, current_starts = 1
        #iter 3, current_starts at 6, current_starts = 2
        #iter 4, current_starts at 2, current_starts = 3
        current_starts = index
        #element_dict[1] = -1
        #element_dict[4] = -1
        #element_dict[6] = -1
        #element_dict[2] = -1
        element_dict[element] = -1

        #current_count becomes 1
        #current_count stays 1
        #current_count = 1
        #current_count = 2
        
        current_count = 1
        
        #current becomes 1 + 1 = 2
        #current becomes 4 + 1 = 5
        #current becomes 6 + 1 = 7
        #current becomes 2 + 1 = 3
        current = element + 1

        #Since current not in element_dict, we continue
        #since 5 not in element_dict, we continue
        #since 7 not in element_dict, we continue
        #since 3 not in element_dict, we continue
        while current in element_dict and element_dict[current] > 0:
            current_count += 1
            element_dict[current] = -1
            current = current + 1

        #current = 1 - 1 = 0
        #while 0 not in element_dict ,we continue
        #since 3 not in element_dict, we continue
        #since 5 not in element_dict, we continue
        #since 1 in element_dict, we iterate
        current = element - 1
        while current in element_dict and element_dict[current] > 0:
            #current_starts becomes element_dict[1] = -1
            #current_count becomes 2
            current_starts = element_dict[current]
            current_count += 1
            #element_dict[1] = -1
            element_dict[current] = -1
            #current = 0
            current = current - 1

        #In the first iteration, current_count = 1 >= -1
        #starts_at = 0
        #max_length = 1

        #In the second iteration, current_count = 1 == 1
        #current_count == max_length and current_starts i.e 1 is greater than 0, we continue
        

        #In the third iteration, current_count = 1 == 1
        #current_count == max_length and current_starts i.e 2 > 1
        #we continue

        #In the last iteration, current_count = 2
        #current_count == 
        #
        #
        
        if current_count >= max_length:
            print(current_count)
            print('How many times?')
            print(max_length)
            if current_count == max_length and current_starts > starts_at:
                continue
            starts_at = current_starts
            print(starts_at)
            max_length = current_count
            print(max_length)
    
 
    #start_element = input_list[2]
    start_element = input_list[starts_at]
    return [element for element in range(start_element, start_element + max_length)] 

print(longest_consecutive_subsequence([1,4,6,2]))