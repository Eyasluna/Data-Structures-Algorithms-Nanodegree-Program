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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

list1 = []
list2 = []
for i  in range(len(texts)):
    list1.append(texts[i][0])
    list1.append(texts[i][1])

for j in range(len(calls)):
    list2.append(calls[j][0])
    list2.append(calls[j][1])

set1 = set(list1)
set2 = set(list2)
count = len(set1)+ len(set2)
print("There are", count, "different telephone numbers in the records.")
