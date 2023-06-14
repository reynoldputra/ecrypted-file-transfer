import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes


def encrypt_file(input_file, output_file, key):
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv

    with open(input_file, 'rb') as file:
        plaintext = file.read()

    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

    with open(output_file, 'wb') as file:
        file.write(iv + ciphertext)


def encrypt_folder(input_folder, output_folder, key):
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            input_file_path = os.path.join(root, file)
            relative_path = os.path.relpath(input_file_path, input_folder)
            output_file_path = os.path.join(output_folder, relative_path + '.enc')

            encrypt_file(input_file_path, output_file_path, key)


input_folder = '../../myfiles/plain.txt'  # Ganti dengan nama folder input yang ingin dienkripsi
output_folder = 'tes_encrypt.txt'  # Ganti dengan nama folder output untuk file terenkripsi

# Generate kunci acak dengan panjang 16 byte (128-bit)
# key = get_random_bytes(16)
key = 

encrypt_folder(input_folder, output_folder, key)

print("Folder berhasil dienkripsi.")
