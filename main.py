# TASK
'''
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
'''
import numpy
from scipy.io.wavfile import read, write
import io
import struct
import numpy as np


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
    frequencies = [] * len(blocks_array)
    for i, block in enumerate(blocks_array):
        # print(f"Block {i}: {block}")
        no_of_ones = block.count('1')
        no_of_zeros = block.count('0')
        frequencies.append((no_of_ones, no_of_zeros))
    return frequencies


def probability(frequencies_tuples):
    probabilities = [] * len(frequencies_tuples)
    for freq in frequencies_tuples:
        probabilities.append((freq[0] / 8, freq[1] / 8))
    return probabilities


if __name__ == '__main__':
    with open("song.wav", "rb") as wavfile:
        wav_byte_array = wavfile.read()

    bits_array = bytes_to_bits_binary(wav_byte_array)
    bit_blocks = split_to_blocks(bits_array)
    frequencies = extract_frequencies(bit_blocks)  # This variable is an array of tuples for some i-th element of
    # bit_blocks array there is corresponding tuple of (number of ones, number of zeros) in frequencies
    probabilities = probability(frequencies)  # Same as for frequencies but this gives probabilities ->
    # i.e. number of  ones / 8
    print("1")

# Write to file if needed but file is too long
# with open("song_bits_array.txt", "w") as bits_to_txt:
#   bits_to_txt.write(bits_array)
