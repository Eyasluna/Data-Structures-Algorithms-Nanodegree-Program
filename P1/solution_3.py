import sys

def huffman_encoding(data):
    global huff
    huffman = {}
    encode = ''
    tree = {}
    tem = '1'
    for item in data:
        huffman[item] = huffman.get(item, 0) + 1

    for nums in sorted(huffman.items(), key = lambda x: x[1]):
        tree[nums[0]] = tem
        tem = '0' + tem

    for items in data:
        encode += tree[items]

    return encode, tree

def huffman_decoding(data,tree):
    huffman = {}
    for items in tree:
        huffman[tree[items]] = items
    temp = ''
    decode = ''
    for item in data:
        if item == '1':
            decode += huffman[temp + item]
            temp = ''
        else:
            temp += item
    return decode

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))
