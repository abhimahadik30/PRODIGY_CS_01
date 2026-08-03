from PIL import Image


def encrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    pixels = image.load()

    width, height = image.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256

            pixels[x, y] = (r, g, b)

    image.save(output_path)
    print("Image Encrypted Successfully!")


def decrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    pixels = image.load()

    width, height = image.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256

            pixels[x, y] = (r, g, b)

    image.save(output_path)
    print("Image Decrypted Successfully!")


print("===== Image Encryption Tool =====")

image_path = input("Enter image filename: ")
key = int(input("Enter Encryption Key: "))

encrypt_image(image_path, "encrypted_image.png", key)
decrypt_image("encrypted_image.png", "decrypted_image.png", key)

print("\nFiles Generated:")
print("encrypted_image.png")
print("decrypted_image.png")