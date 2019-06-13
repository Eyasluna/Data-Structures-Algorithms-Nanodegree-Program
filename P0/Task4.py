"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
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

final = []
text1 = set()
text2 = set()
call1 = set()
call2 = set()

for a in range(len(calls)):
    call1.add(calls[a][0])
    call2.add(calls[a][1])


for j in range(len(texts)):
    text1.add(texts[j][0])
    text2.add(texts[j][1])
# get text numbers into two lists


final = sorted(call1.difference(call2, text1, text2))
# using set to remove duplicates.

print("These numbers could be telemarketers: ")
for elem in final:
    print(elem)

#run time: O(2N) = O(N)

