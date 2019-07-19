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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# empty = {}
# empty_2 = {}

# for call in calls:
#   if call[0] not in empty:
#     if call[0][0:5] == '(080)':
#       empty[call[0]] = call[1]
#       print(f'The numbers called by people in Bengalore have codes ' + f'{empty[call[0]]}')
#       if call[1][0:5] == '(080)':
#         empty_2[call[0]] = call[1]

# length_1 = (len(empty))
# length_2 = (len(empty_2))

# print(f'{round(length_2 / length_1 , 4) * 100}' + ' percent of calls from fixed lines in Bengalore are calls to other fixed lines in Bengalore.')

def isFromBangalore(number):
  isfromBengalore = number.startswith('(080)')
  return isfromBengalore

def getAreaCode(number):
  # fixed line
  if number.startswith( '(' ):
    fixedcode = number.split(')')[0].strip('()')
    return fixedcode
  # telemarketer
  elif number.startswith( '140' ):
    telemarketer = number.startswith('140')
    return telemarketer
  # mobile
  elif number.find(' ') and number[0] == '7' or number[0] == '8' or number[0] == '9':
    return number[0:5]                  

codes_bangalore = []
total_bangalore_calls_count = 0
local_bangalore_calls_count = 0

for call in calls:
  if isFromBangalore( call[0] ):
    total_bangalore_calls_count += 1
    code = getAreaCode( call[1] )
    if code not in codes_bangalore:
      codes_bangalore.append( code )
    if isFromBangalore( call[1] ):
      local_bangalore_calls_count += 1

codes_bangalore.sort()

print( "The numbers called by people in Bangalore have codes:" )
for code in codes_bangalore:
  print( code )
percentage_local = ( local_bangalore_calls_count / total_bangalore_calls_count ) * 100

print( f"{round(percentage_local,2)} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")
