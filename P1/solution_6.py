class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(list1, list2):
    new_set = set()
    current = list1.head
    while current:
        new_set.add(current.value)
        current = current.next
    current = list2.head
    while current:
        new_set.add(current.value)
        current = current.next

    output = LinkedList()
    for a in new_set:
        output.append(a)
    return output

def intersection(list1, list2):
    input1 = set()
    current = list1.head
    while current:
        input1.add(current.value)
        current = current.next
    list_3 = set()
    current = list2.head
    while current:
        list_3.add(current.value)
        current = current.next

    list_new = input1.intersection(list_3)
    output = LinkedList()
    for items in list_new:
        output.append(items)
    return output

# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1,linked_list_2))
print(intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [22, 7, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 65, 11, 21, 1]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print(union(linked_list_5, linked_list_6))
# 65 -> 1 -> 35 -> 4 -> 3 -> 6 -> 7 -> 8 -> 11 -> 21 -> 22 -> 23 ->
print(intersection(linked_list_5, linked_list_6))
# 65 -> 7 ->


# Edge Cases:
# Test case 4
linked_list_7 = LinkedList()
linked_list_8 = LinkedList()