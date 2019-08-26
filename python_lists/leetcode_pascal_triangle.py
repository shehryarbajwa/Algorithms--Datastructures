"""
Find and return the nth row of Pascal's triangle in the form a list. n is 0-based.

For exmaple, if n = 4, then output = [1, 4, 6, 4, 1].

"""

def generatenextRow(lastRow):
    
    nextRow = []
    #First row
    nextRow.insert(0, 1)
    
    #Middle row
    for i in range(0, len(lastRow) - 1):
        nextRow.append(lastRow[i] + lastRow[i + 1])
    
    #Last row
    
    nextRow.append(1)
    
    return nextRow
    
def Pascal(n):
    
    #base case
    if n == 0:
        return [1]
    
    return generatenextRow(Pascal(n - 1))
    
print(Pascal(2))