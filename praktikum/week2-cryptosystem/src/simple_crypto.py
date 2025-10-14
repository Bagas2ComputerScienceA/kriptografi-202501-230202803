def encrypt(plaintext, key):
    result = ""
    for char in plaintext:
        if char.isalpha():
            # Enkripsi Huruf
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        elif char.isdigit():
            # Enkripsi Angka (menggeser dalam rentang 0-9)
            # 48 adalah nilai ASCII untuk '0'
            shift = 48
            # (ord(char) - shift) menghasilkan nilai 0-9 dari digit.
            # Kemudian geser (shift) dengan key, mod 10, dan tambahkan kembali shift.
            result += chr((ord(char) - shift + key) % 10 + shift)
        else:
            # Karakter lain (spasi, tanda hubung, dll.)
            result += char
    return result

def decrypt(ciphertext, key):
    result = ""
    for char in ciphertext:
        if char.isalpha():
            # Dekripsi Huruf
            shift = 65 if char.isupper() else 97
            # Untuk dekripsi, kita kurangi key, kemudian mod 26
            result += chr((ord(char) - shift - key) % 26 + shift)
        elif char.isdigit():
            # Dekripsi Angka
            shift = 48
            # Untuk dekripsi, kita kurangi key, kemudian mod 10
            # Penting: Di Python, operasi modulo (%) dengan angka negatif akan bekerja dengan benar
            # untuk "membungkus" kembali ke angka positif.
            result += chr((ord(char) - shift - key) % 10 + shift)
        else:
            # Karakter lain
            result += char
    return result

if __name__ == "__main__":
    message = "Bagas Enggar Prasetyo - 230202803"
    key = 5

    enc = encrypt(message, key)
    dec = decrypt(enc, key)

    print("Plaintext :", message)
    print("Ciphertext:", enc)
    print("Decrypted :", dec)