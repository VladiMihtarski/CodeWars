def grille(message, code):
    binary_code = bin(code)[2:]
    binary_length = len(message)
    binary_code_filled = binary_code.zfill(binary_length)[::-1]  # Обръщаме и запълваме двоичния код
    hidden_message = ""

    for char, bit in zip(message[::-1], binary_code_filled):
        if bit == '1':
            hidden_message += char

    return hidden_message[::-1]
