"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('/Users/shehryarbajwa/algorithms-challenges/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('/Users/shehryarbajwa/algorithms-challenges/calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
All columns are equal.


TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

duration_dictionary = {}


for call in calls:
    duration_dictionary[call[0]] = 0
    duration_dictionary[call[1]] = 0
    duration_dictionary[call[0]] = duration_dictionary[call[0]] + int(call[3])
    duration_dictionary[call[1]] = duration_dictionary[call[1]] + int(call[3])

for number, duration in duration_dictionary.items():
    print(number)
    print(duration)

