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
call = []
f_call = []
final = []
for i in range(len(calls)):
    if calls[i][0] not in calls[i][1]:
        call.append(calls[i][0])


for j in range(len(texts)):
    for k in range(len(call)):
        if call[k] not in texts[j][0] and texts[j][1]:
            f_call.append(call[k])
final = sorted(set(f_call))
# using set to remove duplicates.


print("These numbers could be telemarketers: ")
for elem in final:
    print(elem)

#run time: O(2N) = O(N)

