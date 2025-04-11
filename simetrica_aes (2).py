from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

def pad(text):
    while len(text) % 16 != 0:
        text += ' '
    return text

def encrypt_aes(key, plaintext):
    cipher = AES.new(key, AES.MODE_ECB)
    padded = pad(plaintext)
    encrypted = cipher.encrypt(padded.encode('utf-8'))
    return base64.b64encode(encrypted).decode('utf-8')

def decrypt_aes(key, ciphertext):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = cipher.decrypt(base64.b64decode(ciphertext)).decode('utf-8')
    return decrypted.strip()

# Exemplo de uso
if __name__ == "__main__":
    key = b'1234567890123456'  # 16 bytes
    texto = "Olá o Felipe Souza estuda na USJT"
    criptografado = encrypt_aes(key, texto)
    print("Criptografado:", criptografado)
    print("Descriptografado:", decrypt_aes(key, criptografado))
