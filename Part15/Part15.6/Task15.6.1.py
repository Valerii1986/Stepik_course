def convert_to_binary_octal_hex(n):
    binary = bin(n)[2:]
    octal = oct(n)[2:]
    hexadecimal = hex(n)[2:].upper()
    return binary, octal, hexadecimal


decimal_number = int(input())

binary, octal, hexadecimal = convert_to_binary_octal_hex(decimal_number)

print(binary)
print(octal)
print(hexadecimal)
