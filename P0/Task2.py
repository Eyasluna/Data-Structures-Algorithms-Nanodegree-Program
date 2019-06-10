"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
times = int(calls[1][3])
for i in range(len(calls)-1):
    if times < int(calls[i+1][3]):
        times = int(calls[i+1][3])
        tel = calls[i+1][1]


print(tel, "spent the longest time,", times,"seconds, on the phone during September 2016." )


k = 0
caller = {}
for i in range(len(calls)):
    if calls[i][0] not in caller:
        caller[calls[i][0]] = int(calls[i][3])
    else:
        caller[calls[i][0]] += int(calls[i][3])


    if calls[i][1] not in caller:
        caller[calls[i][1]] = int(calls[i][3])
    else:
        caller[calls[i][1]] += int(calls[i][3])



print(caller)
max_val = max(caller,key=caller.get)
print(caller[max_val])

print(max_val, "spent the longest time,", caller[max_val],"seconds, on the phone during September 2016." )

#run time:O(N)