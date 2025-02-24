import re

def encode_rle(input_string):
    """Encodes a given alphabetic string using Run-Length Encoding (RLE)."""
    if not input_string.isalpha():
        raise ValueError("Input must contain only alphabetic characters.")
    
    encoded_string = []
    i = 0
    while i < len(input_string):
        count = 1
        while i + 1 < len(input_string) and input_string[i] == input_string[i + 1]:
            count += 1
            i += 1
        if count > 1:
            encoded_string.append(f"{input_string[i]}{count}")
        else:
            encoded_string.append(input_string[i])
        i += 1

    return ''.join(encoded_string)

def decode_rle(encoded_string):
    """Decodes an RLE encoded string back to its original form."""
    if encoded_string.startswith("##00"):
        encoded_string = encoded_string[4:]
    
    decoded_string = []
    pattern = re.compile(r"([A-Za-z])(\d*)")
    
    for match in pattern.finditer(encoded_string):
        char, num = match.groups()
        num = int(num) if num else 1
        decoded_string.append(char * num)
    
    return ''.join(decoded_string)

def escape_rle(input_string):
    """Handles escape sequences in RLE encoding where numbers are part of the input."""
    escaped_string = []
    for char in input_string:
        if char.isdigit():
            escaped_string.append(f"#{char}")
        elif char == "#":
            escaped_string.append("##")
        else:
            escaped_string.append(char)
    
    return ''.join(escaped_string)

def unescape_rle(escaped_string):
    """Decodes escape sequences in RLE encoding."""
    return re.sub(r"#(\d)", r"\1", re.sub(r"##", "#", escaped_string))

if __name__ == "__main__":
    # Example usage
    original = "AAABCC"
    encoded = encode_rle(original)
    print(f"Encoded: {encoded}")

    decoded = decode_rle(encoded)
    print(f"Decoded: {decoded}")

    escaped = escape_rle("A3B#C2")
    print(f"Escaped: {escaped}")

    unescaped = unescape_rle(escaped)
    print(f"Unescaped: {unescaped}")
