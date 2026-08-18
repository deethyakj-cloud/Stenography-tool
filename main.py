from PIL import Image
import os


IMAGE_FOLDER = "images"
OUTPUT_FOLDER = "output"


def text_to_binary(text):
    """Convert text into binary."""
    return ''.join(format(ord(char), '08b') for char in text)


def binary_to_text(binary):
    """Convert binary back into text."""
    chars = []

    for i in range(0, len(binary), 8):
        byte = binary[i:i + 8]

        if len(byte) == 8:
            chars.append(chr(int(byte, 2)))

    return ''.join(chars)


def hide_message():
    """Hide a text message inside an image."""

    image_path = os.path.join(IMAGE_FOLDER, "test.png")

    if not os.path.exists(image_path):
        print("\nError: test.png not found in the images folder.")
        return

    message = input("\nEnter the message to hide: ")

    if not message:
        print("\nError: Message cannot be empty.")
        return

    image = Image.open(image_path).convert("RGB")

    binary_message = text_to_binary(message + "###END###")

    pixels = list(image.get_flattened_data())

    if len(binary_message) > len(pixels) * 3:
        print("\nError: Message is too large for this image.")
        return

    new_pixels = []
    bit_index = 0

    for pixel in pixels:
        r, g, b = pixel

        channels = [r, g, b]

        for i in range(3):
            if bit_index < len(binary_message):
                channels[i] = (channels[i] & 254) | int(
                    binary_message[bit_index]
                )
                bit_index += 1

        new_pixels.append(tuple(channels))

    output_image = Image.new("RGB", image.size)
    output_image.putdata(new_pixels)

    output_path = os.path.join(OUTPUT_FOLDER, "stego_image.png")

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    output_image.save(output_path)

    print("\n" + "=" * 60)
    print("          STEGANOGRAPHY TOOL")
    print("=" * 60)
    print("\nMessage successfully hidden!")
    print(f"Output image: {output_path}")


def extract_message():
    """Extract a hidden message from an image."""

    image_path = os.path.join(OUTPUT_FOLDER, "stego_image.png")

    if not os.path.exists(image_path):
        print("\nError: stego_image.png not found.")
        print("Hide a message first using option 1.")
        return

    image = Image.open(image_path).convert("RGB")

    binary_data = ""

    for pixel in image.get_flattened_data():
        r, g, b = pixel

        binary_data += str(r & 1)
        binary_data += str(g & 1)
        binary_data += str(b & 1)

    extracted_text = binary_to_text(binary_data)

    end_marker = "###END###"

    if end_marker in extracted_text:
        message = extracted_text.split(end_marker)[0]

        print("\n" + "=" * 60)
        print("          EXTRACTED MESSAGE")
        print("=" * 60)
        print(f"\nHidden message:\n{message}")
    else:
        print("\nNo hidden message was detected.")


def main():
    while True:

        print("\n" + "=" * 60)
        print("             STEGANOGRAPHY TOOL")
        print("=" * 60)

        print("\n1. Hide message")
        print("2. Extract message")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            hide_message()

        elif choice == "2":
            extract_message()

        elif choice == "3":
            print("\nExiting program...")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()