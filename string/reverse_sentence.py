

def reverse_sentence(our_string):
    word_list = our_string.split(" ")

    for index in range(len(word_list)):
        word_list[index] = word_list[index][::-1]
    
    return " ".join(word_list)

print(reverse_sentence('Hello World'))

string2 = 'Shehryar'
print(string2[::-1])