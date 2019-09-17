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
    
    #This is a recursive step since when we give it the value 2, it will first run Pascal with 1 and since Pascal at 1 will return again at generateNextRow but this time with
    #0 it will create the first list element of [1]. Now Pascal at index 0 is 1 and we provide this to the generate next row. since it has len of 1 it will be reduced again and thus no middle element which
    #will create the nextRow to be 1,1. Once we have 1,1, then the len becomes 2 so middle row loop will run till end of 1 and middle element becomes i[0] = 1 and i[0+1] = 1
    #so middle element becomes 2 this way
    #Basically the number we provide will keep running backwards recursively until it hits 0 and creates an array [1] and provides that to generate next row function
    #
    return generatenextRow(Pascal(n - 1))
    
print(Pascal(10))