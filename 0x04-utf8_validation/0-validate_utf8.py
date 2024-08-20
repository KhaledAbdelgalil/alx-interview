#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """Determines if a given data set
    represents a valid utf-8 encoding.
    """
    number_bytes = 0

    # Masks to check the most significant bits
    mask_1 = 1 << 7  # 10000000
    mask_2 = 1 << 6  # 01000000

    for num in data:
        # We only care about the last 8 bits of the integer
        byte = num & 0xFF

        if number_bytes == 0:
            # Determine how many bytes are in this UTF-8 character
            mask_byte = 1 << 7
            while mask_byte & byte:
                number_bytes += 1
                mask_byte >>= 1

            # 1-byte characters are represented by 0xxxxxxx, so skip them
            if number_bytes == 0:
                continue

            # UTF-8 characters can only be 1 to 4 bytes long
            if number_bytes == 1 or number_bytes > 4:
                return False
        else:
            # Continuation bytes must start with '10xxxxxx'
            if not (byte & mask_1 and not (byte & mask_2)):
                return False

        # Decrease the number of expected continuation bytes
        number_bytes -= 1

    # If we've processed all bytes correctly, number_bytes should be 0
    return number_bytes == 0
