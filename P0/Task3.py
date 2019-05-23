"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re
import itertools

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
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



#Part A
called_number = []
area_num = []
cell_num = []
area_2 = []
final_1 = []
area3 = []
for i in range(len(calls)-1):
    if "(080)" in calls[i][0]:
        called_number.append(calls[i][1])
#get whole numbers called by 080


for j in range(len(called_number)-1):
    if "(" in called_number[j]:
        area_num.append(called_number[j])
#get fixed phone numbers from called numbers

for elem in called_number:
    if elem[0] == '7'or elem[0] == '8' or elem[0] == '9':
        cell_num.append(elem)
#get cell numbers from called numbers

for keys in area_num:
    keys = keys.strip()
    p = r'\(.*?\)'
    pattern = re.compile(p)
    area_2.append(pattern.findall(keys))
area_2 = set(list(itertools.chain(*area_2)))
for ele in area_2:
    area3.append(ele)
#using regex to find area code from fixed numbers

for mobile in cell_num:
    final_1.append(mobile[:4])
for area in area3:
    final_1.append(area[1:-1])
final_1.append('140')
#collect all area number to one list

final = sorted(set(final_1))
# using set to remove duplicates.
#since I called <sorted> here, the run time for this could be hard to
#calculate for entire program
print("The numbers called by people in Bangalore have codes:")

for elem in final:
    print(elem)
# Part A run time: N+N+N+N+N+N+1= 6N  O(6N)


#Part B
fixed_line = []
for a in range(len(called_number)-1):
    if '(080)' in called_number[a]:
        fixed_line.append(called_number[a])
outcome = round((len(fixed_line)/len(called_number))*100,2)
print(outcome,'percent of calls from fixed lines'
              ' in Bangalore are calls to other fixed lines in Bangalore.')
#run time: O(N)