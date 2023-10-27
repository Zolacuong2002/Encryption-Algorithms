import hashlib

# Create a SHA-256 hash
data = "Blockchain !!".encode('utf-8')
hash_object = hashlib.sha256(data)
hex_dig = hash_object.hexdigest()

print("SHA-256 Hash:", hex_dig)
