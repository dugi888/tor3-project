# TASK
'''
Huffman block coding (song) – GROUP N
(Mia Miletić, Anja Pijak and Mirko Dugajlić)
• Find a Waveform Audio File Format (WAVE, or WAV filename
extension) of your favorite song and read the contents of the file into a
byte array.
• Change bytes to bits to obtain a representation of the wav file as a string
of bits.
• Split the obtained sequence of bits into blocks of 8, and find the frequecy
of every possible block, and use the obtained frequencies to estimate the
probability of all possible blocks of 8 bits.
• Use the estimated probability distribution to obtain a Huffman code for
the blocks of 8 bits.
• Use the Huffman code to encode the bit representation of the song.
• Compare the size of the compressed file with the size of an mp3 file of
the same song.
'''
