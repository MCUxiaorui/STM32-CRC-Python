def stm32_crc32(data_bytes):
    POLYNOMIAL = 0x04C11DB7
    INITIAL = 0xFFFFFFFF
    crc = INITIAL

    # Process data as bytes grouped into 32-bit words (little-endian)
    for i in range(0, len(data_bytes), 4):
        chunk = data_bytes[i:i+4]
        word = int.from_bytes(chunk, byteorder='little')
        crc ^= word
        for _ in range(32):
            if crc & 0x80000000:
                crc = (crc << 1) ^ POLYNOMIAL
            else:
                crc = (crc << 1)
            crc &= 0xFFFFFFFF  # Ensure 32-bit

    return crc  # Remove the final XOR

# Test Cases
# Note: For 0x12345678, the format here should be b'\x78\x56\x34\x12'
data1 = b'\x00\x00\x00\x00'
print(hex(stm32_crc32(data1)))  # Output: 0xc704dd7b (matches expectation)

data2 = b'\x99\x99\x99\x99'
print(hex(stm32_crc32(data2)))  # Output: 0x47ec5bd8 (matches expectation)