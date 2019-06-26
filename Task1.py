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

different_list = []

for item in calls[0][0]:
    if item not in different_list:
        different_list.append(item)


for item in calls[0][1]:
    if item not in different_list:
        different_list.append(item)


for item in texts[0][0]:
    if item not in different_list:
        different_list.append(item)

for item in texts[0][1]:
    if item not in different_list:
        different_list.append(item)
        count = len(different_list)


print("There are " + str(count) + ' different telephone numbers in the records.')



"""
Run-time analysis:

The run time for each for-if loop is O(n). The total run time for all 4 loops when run isolated from each other 
will be (m+n). Since the constant values are a miniscule determinant in the run time of the overall program
we can just ignore it and the run time of the entire algorithm will be O(n)

"""




