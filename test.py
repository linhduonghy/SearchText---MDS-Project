import heapq
from heapq import heappop, heappush
import pickle
 
def isLeaf(root):
    return root.left is None and root.right is None
 
 
# A Tree node
class Node:
    def __init__(self, ch, freq, left=None, right=None):
        self.ch = ch
        self.freq = freq
        self.left = left
        self.right = right
 
    # Override the `__lt__()` function to make `Node` class work with priority queue
    # such that the highest priority item has the lowest frequency
    def __lt__(self, other):
        return self.freq < other.freq
 
 
# Traverse the Huffman Tree and store Huffman Codes in a dictionary
def encode(root, str, huffman_code):
 
    if root is None:
        return
 
    # found a leaf node
    if isLeaf(root):
        huffman_code[root.ch] = str if len(str) > 0 else '1'
 
    encode(root.left, str + '0', huffman_code)
    encode(root.right, str + '1', huffman_code)
 
 
# Traverse the Huffman Tree and decode the encoded string
def decode(root, index, str):
 
    if root is None:
        return index
 
    # found a leaf node
    if isLeaf(root):
        print(root.ch, end='')
        return index
 
    index = index + 1
    root = root.left if str[index] == '0' else root.right
    return decode(root, index, str)
 
 
# Builds Huffman Tree and decodes the given input text
def buildHuffmanTree(text):
 
    # base case: empty string
    if len(text) == 0:
        return
 
    # count the frequency of appearance of each character
    # and store it in a dictionary
    freq = {i: text.count(i) for i in set(text)}
 
    # Create a priority queue to store live nodes of the Huffman tree.
    pq = [Node(k, v) for k, v in freq.items()]
    heapq.heapify(pq)
 
    # do till there is more than one node in the queue
    while len(pq) != 1:
 
        # Remove the two nodes of the highest priority
        # (the lowest frequency) from the queue
 
        left = heappop(pq)
        right = heappop(pq)
 
        # create a new internal node with these two nodes as children and
        # with a frequency equal to the sum of the two nodes' frequencies.
        # Add the new node to the priority queue.
 
        total = left.freq + right.freq
        heappush(pq, Node(None, total, left, right))
 
    # `root` stores pointer to the root of Huffman Tree
    root = pq[0]
 
    # traverse the Huffman tree and store the Huffman codes in a dictionary
    huffmanCode = {}
    encode(root, "", huffmanCode)
 
    # print the Huffman codes
    print("Huffman Codes are:", huffmanCode)
    # with open('data\\huffman.pkl', 'wb') as f:
    #     pickle.dump(huffmanCode, f)
    print("The original string is:", text)
 
    # print the encoded string
    str = ""
    for c in text:
        str += huffmanCode.get(c)
    print(len(str))
    print(len(text) * 8)
    print("The encoded string is:", str)
    print("The decoded string is:", end=' ')
 
    if isLeaf(root):
        # Special case: For input like a, aa, aaa, etc.
        while root.freq > 0:
            print(root.ch, end='')
            root.freq = root.freq - 1
    else:
        # traverse the Huffman Tree again and this time,
        # decode the encoded string
        index = -1
        while index < len(str) - 1:
            index = decode(root, index, str)
 
 
# Huffman coding algorithm implementation in Python
if __name__ == '__main__':
    
    path = 'data\\am-nhac (1).txt'
    with open(path, encoding='utf-8') as f:
        text = f.read()
    text = "Huffman coding is a data compression algorithm."
    buildHuffmanTree(text)