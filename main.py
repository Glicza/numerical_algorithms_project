import numpy as np
from PIL import Image



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
