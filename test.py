import gzip
import binascii

# Input string
input_str = "blueberry"

# Convert string to bytes
input_bytes = input_str.encode('utf-8')

# Compress the bytes
compressed_data = gzip.compress(input_bytes)

# Convert compressed data to hex
hex_encoded_data = binascii.hexlify(compressed_data).decode('utf-8')

print(hex_encoded_data)

