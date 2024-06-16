from cryptography.fernet import Fernet
import os

# Função para gerar a chave de criptografia
def generate_key():
    return Fernet.generate_key()

# Função para carregar a chave de um arquivo ou gerar uma nova se não existir
def load_key(key_file):
    if os.path.exists(key_file):
        return open(key_file, 'rb').read()
    else:
        key = generate_key()
        with open(key_file, 'wb') as key_file:
            key_file.write(key)
        return key

# Função para criptografar um arquivo
def encrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, 'rb') as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open(file_path + '.encrypted', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    os.remove(file_path)
    print(f"O arquivo '{file_path}' foi criptografado para '{file_path}.encrypted'.")

# Função para descriptografar um arquivo
def decrypt_file(encrypted_file_path, key):
    fernet = Fernet(key)
    with open(encrypted_file_path, 'rb') as file:
        encrypted = file.read()
    decrypted = fernet.decrypt(encrypted)
    with open(encrypted_file_path[:-10], 'wb') as decrypted_file:
        decrypted_file.write(decrypted)
    os.remove(encrypted_file_path)
    print(f"O arquivo '{encrypted_file_path}' foi descriptografado para '{encrypted_file_path[:-10]}'.")


def main():
    key_file = 'secret.key'  # Nome do arquivo onde a chave será armazenada
    key = load_key(key_file)

    action = input("Você deseja (E)ncriptar ou (D)escriptar um arquivo? ").strip().lower()
    file_path = input("Por favor, insira o caminho do arquivo: ").strip()

    if action == 'e':
        encrypt_file(file_path, key)
    elif action == 'd':
        decrypt_file(file_path, key)
    else:
        print("Ação inválida. Por favor, escolha 'E' para encriptar ou 'D' para descriptar.")


if __name__ == "__main__":
    main()
