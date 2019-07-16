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
    if call[i] not in different_list:
            different_list.append(call[i])
    if call[i+1] not in different_list:
            different_list.append(call[1])

for text in texts:
    if text[i] not in different_list:
        different_list.append(text[i])

    if text[i+1] not in different_list:
        different_list.append(text[i+1])
        count = len(different_list)


print("There are " + str(count) + ' different telephone numbers in the records.')





