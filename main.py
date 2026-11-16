import numpy as np
from PIL import Image

def encode_image(source_image, message, output_image):
    # Open the image and convert it into a matrix
    image = Image.open(source_image).convert("RGB")
    pixels = np.array(image)

    # Convert the message into binary
    message_bytes = message.encode("utf-8")
    binary_message = ''.join(format(byte, '08b') for byte in message_bytes)

    # Add 32 bits to store the message length
    binary_length = format(len(message_bytes), '032b')
    binary_message = binary_length + binary_message

    # Check if the message fits inside the image
    if len(binary_message) > pixels.size:
        print("Error: Message is too long for this image.")
        return

    # Flatten the image matrix
    flat_pixels = pixels.flatten()

    # Hide each bit inside the last bit of a pixel value
    for i in range(len(binary_message)):
        flat_pixels[i] = (int(flat_pixels[i]) & 254) | int(binary_message[i])

    # Restore the image shape
    encoded_pixels = flat_pixels.reshape(pixels.shape)

    # Save the new image
    encoded_image = Image.fromarray(encoded_pixels)
    encoded_image.save(output_image, format="PNG")

    print("Message successfully hidden in:", output_image)


def main():
    print("=== University Steganography Project (Matrix LSB) ===")
    print("1. Hide a secret message inside an image (Encode)")
    print("2. Extract a secret message from an image (Decode)")
    choice = input("Select an option (1 or 2): ")
    
    if choice == "1":
        source_image = input("Enter the path of the original image: ")
        message = input("Enter the secret message to hide: ")
        output_image = input("Enter the path for the output image: ")
        encode_image(source_image, message, output_image)
    elif choice == "2":
        source_image = input("Enter the path of the image containing the message: ")
        decoded_msg = decode_image(source_image)
        print("\nThe hidden message found inside the matrix is:")
        print(decoded_msg)

if __name__ == "__main__":
    main()
