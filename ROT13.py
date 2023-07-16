def rot13(message):
    decrypted_text = ""
    for char in message:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            decrypted_char = chr((ord(char) - ascii_offset + 13) % 26 + ascii_offset)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

encrypted_text = input()
decrypted_text = rot13(encrypted_text)
print(decrypted_text)
