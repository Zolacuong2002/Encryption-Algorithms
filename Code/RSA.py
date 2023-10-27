from Crypto.PublicKey import RSA

# Generate a new RSA key pair (usually, you'd save these keys for later use)
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

print("Private key: ", private_key)
print("Public key: ", public_key)
# Save the keys to files
with open('private.pem', 'wb') as f:
    f.write(private_key)

with open('public.pem', 'wb') as f:
    f.write(public_key)
