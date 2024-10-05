from PIL import Image

# Function to encrypt the image
def encrypt_image(image_path, key):
    img = Image.open(image_path)
    img = img.convert('RGB')
    pixels = img.load()  

    # Encrypt the image
    width, height = img.size
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            r_enc = r ^ key
            g_enc = g ^ key
            b_enc = b ^ key
            pixels[x, y] = (r_enc, g_enc, b_enc)
    
    encrypted_image_path = "encrypted_image.png"
    img.save(encrypted_image_path)
    print(f"Encrypted image saved as {encrypted_image_path}")

# Function to decrypt the image
def decrypt_image(encrypted_image_path, key):
    img = Image.open(encrypted_image_path)
    img = img.convert('RGB')
    pixels = img.load()  

    # Decrypt the image 
    width, height = img.size
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            r_dec = r ^ key
            g_dec = g ^ key
            b_dec = b ^ key
            pixels[x, y] = (r_dec, g_dec, b_dec)
    
    decrypted_image_path = "decrypted_image.png"
    img.save(decrypted_image_path)
    print(f"Decrypted image saved as {decrypted_image_path}")
    
key = 210
image_path = "img2.jpg"  

encrypt_image(image_path, key)

decrypt_image("encrypted_image.png", key)
