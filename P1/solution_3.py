import sys
import collections


class Node(object):

    def __init__(self, char=None, freq=None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def nodes(node1, node2):

        node = Node()

        if node1.freq <= node2.freq:
            node.left = node1
            node.right = node2
        else:
            node.left = node1
            node.right = node2

        node.freq = node1.freq + node2.freq

        return node

    def __repr__(self):
        return "Node of character: {} | frequency: {}".format(self.char, self.freq)


class Queue(object):
    def __init__(self, string):
        _ = collections.Counter(string)
        self.arr = [Node(char=letter, freq=_[letter]) for letter in _]
        self.sort()

    def sort(self) -> None:

        self.arr = sorted(self.arr, key=lambda x: x.freq, reverse=True)

    def fuse_step(self) -> None:

        node_1 = self.arr.pop()
        node_2 = self.arr.pop()

        self.arr.append(Node.nodes(node1=node_1, node2=node_2))
        self.sort()


class Tree(object):
    def __init__(self, queue: Queue):
        while len(queue.arr) > 1:
            queue.fuse_step()

        self.root = queue.arr[0]

    def binaryze(self) -> None:


        self.root = self.add_binary(self.root)
        self.root.freq = 0

    @staticmethod
    def add_binary(node: Node) -> Node:

        if (node.left is None) and (node.right is None):
            return node

        if node.left is not None:
            node.left.freq = 1
            node.left = Tree.add_binary(node.left)

        if node.right is not None:
            node.right.freq = 0
            node.right = Tree.add_binary(node.right)

        return node


class HuffmanEncoder(object):
    def __init__(self, tree: Tree):
        self.table = self._create_encoding_table(base_code='', node=tree.root)
        self.encode_dict = None
        self.decode_dict = None

        self._create_encoder()
        self._create_decoder()

    def _create_encoder(self) -> None:

        encoder = dict()

        for i, j in enumerate(self.table):
            encoder[j[0]] = j[1]

        self.encode_dict = encoder

    def _create_decoder(self) -> None:

        decoder = dict()

        for i, j in enumerate(self.table):
            decoder[j[1]] = j[0]


        self.decode_dict = decoder

    def encode(self, text: str) -> str:

        ntext = ''
        for char in text:
            ntext += self.encode_dict[char]

        return ntext

    def decode(self, encoded_text: str) -> str:

        new_text = ''
        while len(encoded_text) > 0:
            i_decoder = 1
            while True:
                if encoded_text[:i_decoder] in self.decode_dict.keys():
                    new_text += self.decode_dict[encoded_text[:i_decoder]]
                    encoded_text = encoded_text[i_decoder:]
                    break
                i_decoder += 1

        return new_text

    @staticmethod
    def _create_encoding_table(base_code: str, node: Node) -> list:

        if (node.left is None) and (node.right is None):
            return [(node.char, base_code + str(node.freq))]

        if node.freq == -1:
            current_code = ''
        else:
            current_code = base_code + str(node.freq)

        coding_dict = []

        if node.char is not None:
            coding_dict.append((node.char, current_code + str(node.freq)))

        if node.left is not None:
            coding_dict.extend(HuffmanEncoder._create_encoding_table(current_code, node.left))

        if node.right is not None:
            coding_dict.extend(HuffmanEncoder._create_encoding_table(current_code, node.right))

        return coding_dict


def huffman_encoding(data: str) -> (str, HuffmanEncoder):
    """
    Huffman encoding method
    :param data: text desired to be codified
    :return: text encoded and the corresponding text specific encoder
    """

    if len(data) == 0:
        print("Please introduce a non null string")
        return

    else:
        queue = Queue(string=data)
        tree = Tree(queue=queue)
        tree.binaryze()
        new_encoder = HuffmanEncoder(tree)

        return new_encoder.encode(data), new_encoder


def huffman_decoding(data: str, encoder: HuffmanEncoder) -> str:
    """
    Huffman decoding method
    :param data: text desired to be decoded
    :param encoder: Huffman encoder used to initially encode the text
    :return: text decoded, i.e. originally restored
    """

    return encoder.decode(data)


if __name__ == "__main__":

    # Case 1
    print('Case 1:')

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # The size of the data is: 69
    print("The content of the data is: {}\n".format(a_great_sentence))
    # The content of the data is: The bird is the word

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # encoded data is: 36
    print("encoded data is: {}\n".format(encoded_data))
    # encoded data is: 0001011011101000111001010010011000000001000011101110100110001111010010

    decoded_data = huffman_decoding(encoded_data, tree)

    print("decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # decoded data is: 69
    print("encoded data is: {}\n".format(decoded_data))
    # encoded data is: The bird is the word

    # Case 2
    print('Case 2:')

    a_great_sentence = "I just want to have fun coding"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # The size of the data is: 79
    print("The content of the data is: {}\n".format(a_great_sentence))
    # The size of the data is: 79

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # The size of the encoded data is: 40
    print("The content of the encoded data is: {}\n".format(encoded_data))
    # The content of the encoded data is: 00110110011100010010010111001011000000010111101100111010101000010110100
    # 0110100100010000110111010010111101100000001101

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # The size of the decoded data is: 79
    print("The content of the encoded data is: {}\n".format(decoded_data))
    # The content of the encoded data is: I just want to have fun coding

    # Case 3
    print('Case 3:')

    a_great_sentence = "The sun shines and I go to the beach"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # The size of the data is: 85
    print("The content of the data is: {}\n".format(a_great_sentence))
    # The content of the data is: The sun shines and I go to the beach

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # The size of the encoded data is: 44
    print("The content of the encoded data is: {}\n".format(encoded_data))
    # The content of the encoded data is: 1001011011101000110011001001000111010000001011100010100110010100010110110
    # 01101110000001000010000001000011101110110100111001110101110

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # The size of the decoded data is: 85
    print("The content of the encoded data is: {}\n".format(decoded_data))
    # The content of the encoded data is: The sun shines and I go to the beach

    # Edge Cases
    # Case 4
    print('Edge Cases:')
    print('Case 4:')

    a_not_so_great_sentence = "aaa"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_not_so_great_sentence)))
    # The size of the data is: 52
    print("The content of the data is: {}\n".format(a_not_so_great_sentence))
    # The content of the data is: aaa

    encoded_data, tree = huffman_encoding(a_not_so_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # The size of the encoded data is: 24
    print("The content of the encoded data is: {}\n".format(encoded_data))
    # The content of the encoded data is: 000

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # The size of the decoded data is: 52
    print("The content of the encoded data is: {}\n".format(decoded_data))
    # The content of the encoded data is: aaa

