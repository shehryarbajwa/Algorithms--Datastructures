#Option 1 - Modify state, make a copy of open, close count and recurse
def generate_parenthesis(n):
    result = []
    def backtrack(word):
        open_count = word.count('(')
        closed_count = word.count(')')

        if open_count > n:
            return
        if closed_count > open_count:
            return
        
        if len(word) == 2 * n:
            result.append(word)
        else:
            backtrack(word + '(')
            backtrack(word + ')')
    backtrack('')
    return result


#Option 2

def generate_parenthesis_2(n):
    result = []
    word = []
    def backtrack(opening_count, closing_count):
        if opening_count > n:
            return
        if closing_count > opening_count:
            return
        
        if len(word) == n * 2:
            result.append("".join(word))
        else:
            word.append('(')
            backtrack(opening_count + 1, closing_count)
            word.pop()

            word.append(')')
            backtrack(opening_count, closing_count + 1)
            word.pop()

    backtrack(0, 0)
    return result

print(generate_parenthesis_2(3))