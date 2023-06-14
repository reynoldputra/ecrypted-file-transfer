import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad


def decrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as file:
        ciphertext = file.read()

    iv = ciphertext[:16]
    ciphertext = ciphertext[16:]

    cipher = AES.new(key, AES.MODE_CBC, iv)

    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

    with open(output_file, 'wb') as file:
        file.write(plaintext)


def decrypt_folder(input_folder, output_folder, key):
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            input_file_path = os.path.join(root, file)
            relative_path = os.path.relpath(input_file_path, input_folder)
            output_file_path = os.path.join(output_folder, relative_path[:-4])

            decrypt_file(input_file_path, output_file_path, key)


input_folder = 'tes_encrypt'  # Ganti dengan nama folder input yang telah dienkripsi
output_folder = 'tes_decrypt'  # Ganti dengan nama folder output untuk file terdekripsi

# Masukkan kunci yang digunakan saat melakukan enkripsi
key = b'\xae$\xf1\x82g+g8\xf8q\xcf\xd2\x0e\xaa\xfah'  # Ganti dengan kunci yang sesuai

decrypt_folder(input_folder, output_folder, key)

print("Folder berhasil didekripsi.")
