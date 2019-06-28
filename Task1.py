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
i = 0
count = 0


for call in calls:
    if call[i][0] not in different_list:
            different_list.append(call)
    if call[i][1] not in different_list:
            different_list.append(call)


for text in texts:
    if text[i][0] not in different_list:
        different_list.append(text)

    if text[i][1] not in different_list:
        different_list.append(text)
        count = len(different_list)


print("There are " + str(count) + ' different telephone numbers in the records.')



"""
Run-time analysis:

The run time for each for-if loop is O(n). The total run time for both for loops when run isolated from each other 
will be (m+n). Since the constant values are a miniscule determinant in the run time of the overall program
we can just ignore it and the run time of the entire algorithm will be O(n)

"""




