def xor_cipher(s: str, key: int) -> str:
    return ''.join([chr(ord(i) ^ key) for i in s])

xor_uncipher = xor_cipher

my_string = 'this is a God'
key = 34543
encrypted_string = xor_cipher(my_string, key)
decpypted_strind = xor_uncipher(encrypted_string, key)
print(my_string)
print(encrypted_string)
print(decpypted_strind)