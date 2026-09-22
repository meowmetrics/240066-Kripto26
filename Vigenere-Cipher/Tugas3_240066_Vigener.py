# Praktikum Kriptografi | Tugas 3
# Alesha Naila | 140810240066

def vigenere_encrypt(plaintext, key):
    plaintext = plaintext.upper()
    key = key.upper()

    result = ""
    i = 0

    for char in plaintext:
        if char.isalpha():
            p = ord(char) - ord('A')
            k = ord(key[i % len(key)]) - ord('A')
            c = (p + k) % 26

            print(char, p, k, c, chr(c + ord('A')))

            result += chr(c + ord('A'))
            i += 1
        else:
            result += char

    return result


def vigenere_decrypt(ciphertext, key):
    ciphertext = ciphertext.upper()
    key = key.upper()

    result = ""
    i = 0

    for char in ciphertext:
        if char.isalpha():
            c = ord(char) - ord('A')
            k = ord(key[i % len(key)]) - ord('A')
            p = (c - k) % 26

            result += chr(p + ord('A'))
            i += 1
        else:
            result += char

    return result


plaintext = input("Plain text: ")
key = input("Key: ")

print("\nPT  n(PT)  n(K)  (n(PT) + n(K)) mod 26  CT")
ciphertext = vigenere_encrypt(plaintext, key)

print("\nCiphertext:", ciphertext)

decrypted = vigenere_decrypt(ciphertext, key)
print("Decrypted :", decrypted)