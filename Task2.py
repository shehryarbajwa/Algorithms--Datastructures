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

# general_call_dict = {}
# for call in calls:
#     #  both aren't entries
    
#     if call[0] not in general_call_dict and call[1] not in general_call_dict:
#         general_call_dict[call[0]] = []
#         general_call_dict[call[1]] = []
#         general_call_dict[call[0]].append(int(call[3]))
#         general_call_dict[call[1]].append(int(call[3]))
#     #  only outgoing number is entered
    
#     # elif call[0] in general_call_dict and call[1] not in general_call_dict:
#     #     general_call_dict[call[0]].append(int(call[3]))
#     #     general_call_dict[call[1]] = []
#     #     general_call_dict[call[1]].append(int(call[3]))
#     # #  only incoming number is entered
    
#     # elif call[0] not in general_call_dict and call[1] in general_call_dict:
#     #     general_call_dict[call[0]] = []
#     #     general_call_dict[call[0]].append(int(call[3]))
#     #     general_call_dict[call[1]].append(int(call[3]))
    
#     elif call[0] in general_call_dict and call[1] in general_call_dict:
#         general_call_dict[call[0]].append(int(call[3]))
#         general_call_dict[call[1]].append(int(call[3]))
# print(general_call_dict)

# number_to_minutes = {}
# for number in general_call_dict:
#     # number_to_minutes[number] = sum(general_call_dict[number])
#     call_duration = 0
#     for iteration in general_call_dict[number]:
#         call_duration += iteration
#         number_to_minutes[number] = call_duration

# max_duration = 0
# for number in number_to_minutes:
#     if number_to_minutes[number] > max_duration:
#         max_duration = number_to_minutes[number]

# print('{0} spent the longest time, {1} seconds, on the phone during '
#       'September 2016.'.format(list(number_to_minutes.keys())[list(
#         number_to_minutes.values()).index(max_duration)], max_duration))

talk_times = {}
longest_talker = None
longest_talk_time = 0

for call in calls:
    if call[0] not in talk_times:
        talk_times[ call[0] ] = 0
    if call[1] not in talk_times:
        talk_times[ call[1] ] = 0
    talk_times[ call[0] ] += int( call[3] )
    talk_times[ call[1] ] += int( call[3] )

for talker, time in talk_times.items():
    if time > longest_talk_time:
        longest_talker = talker
        longest_talk_time = time

print(talk_times)
print( "{0} spent the longest time, {1} seconds, on the phone during September 2016.".format( 
    longest_talker, longest_talk_time ) )