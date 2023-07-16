#include <iostream>
#include <string>

std::string decrypt_rot13(const std::string& text) {
    std::string decrypted_text = "";
    for (char c : text) {
        if (isalpha(c)) {
            char ascii_offset = islower(c) ? 'a' : 'A';
            char decrypted_char = ((c - ascii_offset + 13) % 26) + ascii_offset;
            decrypted_text += decrypted_char;
        } else {
            decrypted_text += c;
        }
    }
    return decrypted_text;
}

int main() {
    std::string encrypted_text;
    std::cout << "Enter the encrypted text: ";
    std::getline(std::cin, encrypted_text);

    std::string decrypted_text = decrypt_rot13(encrypted_text);
    std::cout << "Decrypted text: " << decrypted_text << std::endl;

    return 0;
}
