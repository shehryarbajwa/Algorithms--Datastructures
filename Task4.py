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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

empty = []

for call in calls:
    if call[0] not in empty:
        empty.append(call[0])
for call in calls:
    if call[1] in empty:
        empty.remove(call[1])

for text in texts:
    if text[0] in empty:
        empty.remove(text[0])
for text in texts:
    if text[1] in empty:
        empty.remove(text[1])

empty.sort()

print("These numbers could be telemarketers:")
for number in empty:
    print(number)