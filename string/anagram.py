"""
Algorithm for deciding whether two strings are anagrams
"""

characters_a = []
characters_b = []

def anagram_checker(str1, str2):

    for character in str1:
        if character not in characters_a:
            characters_a.append(character.lower())
    for character in str2:
        if character not in characters_b:
            characters_b.append(character.lower())
    
    for character in characters_a:
        if character == ' ':
            characters_a.remove(character)
    for character in characters_b:
        if character == ' ':
            characters_b.remove(character)
    
    characters_a.sort()
    characters_b.sort()

    if characters_a == characters_b:
        print("It is a anagram")
    

print(anagram_checker('Time and tide wait for no man', 'Notified madman into water'))