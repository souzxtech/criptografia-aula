import hashlib

def gerar_hash(texto):
    resultado = hashlib.sha256(texto.encode('utf-8')).hexdigest()
    return resultado

# Exemplo de uso
if __name__ == "__main__":
    texto = "Olá o Felipe Souza estuda na USJT"
    hash_gerado = gerar_hash(texto)
    print("Hash SHA-256:", hash_gerado)
