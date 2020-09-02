

def count_vowels(string):
    vowels = 0
    consonants = 0

    vowels_arr = ['a', 'e', 'i', 'o', 'u']

    for i in range(len(string)):
        if string[i] in vowels_arr:
            vowels += 1
        elif not string[i].isdigit() and string[i] not in vowels_arr:
            consonants += 1
        else:
            continue
    return consonants

print(count_vowels('aeiddcg'))
            