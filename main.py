# TASK
"""
Huffman block coding (song) – GROUP N
(Mia Miletić, Anja Pijak and Mirko Dugajlić)
• Find a Waveform Audio File Format (WAVE, or WAV filename
extension) of your favorite song and read the contents of the file into a
byte array.
• Change bytes to bits to obtain a representation of the wav file as a string
of bits.
• Split the obtained sequence of bits into blocks of 8, and find the frequency
of every possible block, and use the obtained frequencies to estimate the
probability of all possible blocks of 8 bits.
• Use the estimated probability distribution to obtain a Huffman code for
the blocks of 8 bits.
• Use the Huffman code to encode the bit representation of the song.
• Compare the size of the compressed file with the size of an mp3 file of
the same song.
"""


def bytes_to_bits_binary(byte_data):
    bits_data = bin(int.from_bytes(byte_data, byteorder='big'))[2:]
    return bits_data


def split_to_blocks(bits_data):
    chunks, chunk_size = len(bits_data), 8
    num_blocks = chunks // chunk_size
    blocks_array = [''] * (num_blocks + 1)
    j = 0
    for i in range(0, chunks, chunk_size):
        blocks_array[j] = bits_data[i:i + chunk_size]
        j = j + 1
    return blocks_array


def extract_frequencies(blocks_array):
    # Initialize an empty dictionary to store the frequency of each block
    frequency = {}

    # Loop through each block in the blocks_array
    for block in blocks_array:
        # If the block is already in the dictionary, increment its count
        if block in frequency:
            frequency[block] += 1
        # If the block is not in the dictionary, add it with a count of 1
        else:
            frequency[block] = 1

    # Sort the dictionary by frequency
    sorted_frequency = dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True))
    return sorted_frequency


'''
    # Print the frequency of each block
    for block, count in sorted_frequency.items():
        print(f"Block: {block}, Frequency: {count}")
'''


def probability(frequencies_dict, blocks_array):
    probabilities = {}
    for key, value in frequencies_dict.items():
        probabilities[key] = (value / len(blocks_array))
    '''
    # Print the probability of each block
    for block, count in probabilities.items():
        print(f"Block: {block}, Probability: {count}")
    '''
    return probabilities


# Creating tree nodes
class NodeTree(object):

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)


# Main function implementing huffman coding
def huffman_code_tree(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, True, binString + '0'))
    d.update(huffman_code_tree(r, False, binString + '1'))
    return d


def huffman(probabilities):
    nodes = list(probabilities.items())

    while len(nodes) > 1:
        (key1, c1) = nodes[-1]
        (key2, c2) = nodes[-2]
        nodes = nodes[:-2]
        node = NodeTree(key1, key2)
        nodes.append((node, c1 + c2))

        nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

    huffmanCode = huffman_code_tree(nodes[0][0])

   # print(' Char | Huffman code ')
   # print('----------------------')
    ##for char, frequency in probabilities.items():
    ##    print(' %-4r |%12s' % (char, huffmanCode[char]))

    ##print(huffmanCode)
    return huffmanCode


def encode(huffman_code, blocks_array):
    encoding = ""
    for block in blocks_array:
        encoding += str(huffman_code[block])
    return encoding


def bits_to_mb(bits):
    bytes_in_bit = 1 / 8
    kb_in_byte = 1 / 1024
    mb_in_kb = 1 / 1024
    conversion_factor = bytes_in_bit * kb_in_byte * mb_in_kb
    # Convert bits to MB
    mb = bits * conversion_factor
    return mb

if __name__ == '__main__':
    song_name = "star.wav"
    with open(song_name, "rb") as wavfile:
        wav_byte_array = wavfile.read()

    print("Getting bits")
    bits_array = bytes_to_bits_binary(wav_byte_array)
    print("Splitting to blocks")
    bit_blocks = split_to_blocks(bits_array)
    print("Getting frequencies")
    frequencies = extract_frequencies(bit_blocks)  # Dictionary (block, freq_of_block)
    print("Getting probabilities")
    probabilities = probability(frequencies, bit_blocks)  # Dictionary(block, freq_of_block/num_of_blocks)
    print("Making Huffman code")
    huffman_code = huffman(probabilities)
    print("Encoding")
    encoding = (encode(huffman_code, bit_blocks))
    print("\n\n --------------------------------- \n\n")
    print(song_name,":")
    print("Encoded length: ", bits_to_mb(len(encoding)), " MB")
    print("WAV length: ", bits_to_mb(len(bits_array)), " MB")

# Write to file if needed but file is too long
# with open("song_bits_array.txt", "w") as bits_to_txt:
#   bits_to_txt.write(bits_array)
