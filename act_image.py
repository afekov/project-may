from PIL import Image
import numpy as np
from Crypto.Cipher import AES
import io

SIZE = (128, 128)


def decrypt_image(bdata, key):
    data = list(bdata)
    encrypted_data = bytes(data[:, :, 4])
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = cipher.decrypt(encrypted_data)
    return plaintext


def encrypt_image(image, msg, key):
    cipher = AES.new(key, AES.MODE_ECB)
    enc = cipher.encrypt(msg)
    data = np.asanyarray(image)
    data[:, :, 4] = enc
    return bytes(data)
