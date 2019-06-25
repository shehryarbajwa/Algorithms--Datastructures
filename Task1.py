"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('/Users/shehryarbajwa/algorithms-challenges/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('/Users/shehryarbajwa/algorithms-challenges/calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

count = 0
count1 = 0
i = 0
j = 1


    

while i < len(calls) - 1:
    if (calls[i][0] != calls[i+1][0]):
        count = count + 1
    i = i + 1

    if(calls[j][0] != calls[j+1][0]):
        count1 = count1 + 1
    j = j + 1

print("There are " + str(count) + ' different telephone numbers in the records.')
print(count1)
