from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Key should be 16, 24, or 32 bytes long for AES-128, AES-192, or AES-256.
key = get_random_bytes(32)
cipher = AES.new(key, AES.MODE_EAX)

# Encryption
plaintext = "This is a secret message".encode('utf-8')
ciphertext, tag = cipher.encrypt_and_digest(plaintext)

# Decryption
decipher = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)
decrypted_text = decipher.decrypt(ciphertext)

print("Original: ", plaintext.decode('utf-8'))

print("Decrypted: ", decrypted_text.decode('utf-8'))
