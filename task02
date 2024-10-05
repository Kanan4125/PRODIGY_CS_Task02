from PIL import Image

# Function to encrypt the image
def encrypt_image(image_path, key):
    # Open the image
    img = Image.open(image_path)
    img = img.convert('RGB')
    pixels = img.load()  # Access pixel data

    # Encrypt the image
    width, height = img.size
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            # XOR each color value with the key
            r_enc = r ^ key
            g_enc = g ^ key
            b_enc = b ^ key
            pixels[x, y] = (r_enc, g_enc, b_enc)
    
    encrypted_image_path = "encrypted_image.png"
    img.save(encrypted_image_path)
    print(f"Encrypted image saved as {encrypted_image_path}")

# Function to decrypt the image
def decrypt_image(encrypted_image_path, key):
    # Open the encrypted image
    img = Image.open(encrypted_image_path)
    img = img.convert('RGB')
    pixels = img.load()  # Access pixel data

    # Decrypt the image (same as encryption since XOR is a reversible operation)
    width, height = img.size
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            # XOR each color value with the key to decrypt
            r_dec = r ^ key
            g_dec = g ^ key
            b_dec = b ^ key
            pixels[x, y] = (r_dec, g_dec, b_dec)
    
    decrypted_image_path = "decrypted_image.png"
    img.save(decrypted_image_path)
    print(f"Decrypted image saved as {decrypted_image_path}")

# Example usage
key = 210  # Simple key for encryption/decryption
image_path = "img2.jpg"  # Path to the image you want to encrypt

# Encrypt and save the image
encrypt_image(image_path, key)

# Decrypt and save the image
decrypt_image("encrypted_image.png", key)
