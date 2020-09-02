
def reverse_string(string):
    #Remove whitespaces

    left = 0
    right = len(string) - 1

    while left <= right and string[left] == ' ':
        left += 1

    while string[right] == ' ':
        right -= 1

    return reverse_words(string[left:right + 1])

def reverse_words(string):

    res = []
    left = 0
    count = 0

    for char in string:
        if char == ' ':
            if count == 1:
                continue
            else:
                count += 1
        else:
            count = 0
        
        res.append(char)
    
    right = len(res) - 1
    while left < right:
        res[left], res[right] = res[right], res[left]
        left += 1
        right -= 1
    
    return reverse_characters(res)

def reverse_characters(array):
    left = 0
    right = len(array) - 1
    word_left = 0

    while left <= right:
        while left <= right and array[left] != ' ':
            left += 1

        word_end = left - 1

        while word_left < word_end:
            array[word_left], array[word_end] = array[word_end], array[word_left]
            word_left += 1
            word_end -= 1

        left += 1
        word_left = left

    return array





print(reverse_string('     sky is blue      '))
# # print(reverse_words('sky  is blue'))
# print(reverse_characters(['e', 'u', 'l', 'b', ' ', 's', 'i', ' ', 'y', 'k', 's']))