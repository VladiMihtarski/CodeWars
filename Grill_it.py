def grille(message, code):
    if not message:
        return ""
    binary = bin(code)[2:].zfill(len(message))
    result = ""
    
    for i in range(len(binary)):
        if binary[i] == '1':
            return += message[i]
            
    return result
    
    
message = ""
code = 1
print(grille(message, code))