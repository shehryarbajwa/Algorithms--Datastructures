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

duration_list = []
number_to_call = {}
for call in calls:
    if call[0] not in number_to_call:
        number_to_call[call[0]]=[]
        number_to_call[call[0]].append([call[1], call[3]])
        
    else:
        number_to_call[call[0]].append([call[1], call[3]])
        
sorted_x = sorted(number_to_call.items(), key=lambda kv: kv[1])
maxvalue = max(sorted_x)

"""Extrapolate the duration from the calls and add the value in a seperate list"""
duration = 0
i = 0
while i <= 5:
    duration_list.append(int(maxvalue[1][i][1]))
    i += 1


"""Adding up the durations together for total number of seconds"""

total_durations = sum(duration_list)

print(f'{maxvalue[0]} ' + ' spent the longest time, ' + f'{total_durations}, seconds' + ' on the phone during September 2016')
"""
Call is a list which contains 4 elements
when we do call in calls
We are iterating over a list of list
"""

