import heapq
from collections import defaultdict


class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_frequency_table(text):
    freq_table = defaultdict(int)
    for char in text:
        freq_table[char] += 1
    return freq_table

def build_huffman_tree(freq_table):
    priority_queue = [HuffmanNode(char, freq) for char, freq in freq_table.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)

    return priority_queue[0]

def build_encoding_table(root):
    encoding_table = {}

    def traverse(node, code=''):
        if node:
            if node.char:
                encoding_table[node.char] = code
            traverse(node.left, code + '0')
            traverse(node.right, code + '1')

    traverse(root)
    return encoding_table

def encode(text, encoding_table):
    encoded_text = ''
    for char in text:
        encoded_text += encoding_table[char]
    return encoded_text

def decode(encoded_text, root):
    decoded_text = ''
    current_node = root
    for bit in encoded_text:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char:
            decoded_text += current_node.char
            current_node = root
    return decoded_text

def huffman_encoding(text):
    if len(text) == 0:
        return '', None

    freq_table = build_frequency_table(text)
    root = build_huffman_tree(freq_table)
    encoding_table = build_encoding_table(root)
    encoded_text = encode(text, encoding_table)
    return encoded_text, root

def huffman_decoding(encoded_text, root):
    if len(encoded_text) == 0:
        return ''

    decoded_text = decode(encoded_text, root)
    return decoded_text


if __name__ == "__main__":
    text = "this is an example for huffman encoding and decoding"
    encoded_text, tree = huffman_encoding(text)
    print("Encoded text:", encoded_text)
    decoded_text = huffman_decoding(encoded_text, tree)
    print("Decoded text:", decoded_text)
