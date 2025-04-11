from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

def gerar_chaves():
    chave = RSA.generate(2048)
    return chave, chave.publickey()

def criptografar(mensagem, chave_publica):
    cipher = PKCS1_OAEP.new(chave_publica)
    encrypted = cipher.encrypt(mensagem.encode('utf-8'))
    return base64.b64encode(encrypted).decode('utf-8')

def descriptografar(mensagem_criptografada, chave_privada):
    cipher = PKCS1_OAEP.new(chave_privada)
    decrypted = cipher.decrypt(base64.b64decode(mensagem_criptografada))
    return decrypted.decode('utf-8')

# Exemplo
if __name__ == "__main__":
    privada, publica = gerar_chaves()
    msg = "Olá o Felipe Souza estuda na USJT"
    cifrada = criptografar(msg, publica)
    print("Cifrada:", cifrada)
    print("Decifrada:", descriptografar(cifrada, privada))
